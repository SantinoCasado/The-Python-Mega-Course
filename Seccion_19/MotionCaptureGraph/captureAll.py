import cv2
import time
import pandas
from datetime import datetime 

# Para mas cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

firstFrame = None                                                               # Inicializar el primer cuadro para la detección de movimiento   

status_list = [None, None]                                                      # Lista para almacenar el estado de movimiento
times = []                                                                      # Lista para almacenar los tiempos de movimiento
df = pandas.DataFrame(columns=["Start", "End"])                             # DataFrame para almacenar los intervalos de movimiento

# Tiempo límite para la captura (en segundos)
CAPTURE_DURATION = 30  # 30 segundos de captura
start_time = time.time()

print(f"Iniciando captura de movimiento por {CAPTURE_DURATION} segundos...")
print("Presiona 'q' para salir antes del tiempo límite")

# Intentar con diferentes índices de cámara
camera_found = False
for camera_index in range(3):  # Intentar índices 0, 1, 2
    video = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)                                      # Usar DirectShow en Windows para evitar bloqueos
    if video.isOpened():
        print(f"Cámara encontrada en índice {camera_index}")
        camera_found = True
        break
    else:
        video.release()

if not camera_found:
    print("ERROR: No se pudo abrir ninguna cámara. Creando datos de prueba...")
    # Crear datos de prueba si no hay cámara
    from datetime import datetime, timedelta
    now = datetime.now()
    df = pandas.DataFrame({
        "Start": [now, now + timedelta(seconds=10)],
        "End": [now + timedelta(seconds=5), now + timedelta(seconds=15)]
    })
    df.to_csv("Times.csv", index=False)
    print("Archivo Times.csv creado con datos de prueba")
else:
    while True:
        # Verificar tiempo límite
        if time.time() - start_time > CAPTURE_DURATION:
            print(f"\nTiempo de captura completado ({CAPTURE_DURATION} segundos)")
            if status == 1:
                times.append(datetime.now())
            break
            
        check, frame = video.read()                                                 # Leer un cuadro de la cámara
        status = 0

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                              # Convertir el cuadro a escala de grises
        gray = cv2.GaussianBlur(gray, (21, 21), 0)                                  # Aplicar desenfoque gaussiano para reducir ruido aumenta la precisión de la detección de movimiento

        if firstFrame is None:                                                      # Si es el primer cuadro, inicializarlo
            firstFrame = gray
            continue    # Saltar al siguiente cuadro

        delta_frame = cv2.absdiff(firstFrame, gray)                                 # Calcular la diferencia absoluta entre el primer cuadro y el actual para detectar movimiento
        thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]    # Aplicar umbral para resaltar las diferencias significativas

        thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)                 # Dilatar la imagen umbral para llenar los agujeros

        print("Frame shape:", frame.shape if check else "No se capturó frame")      # Muestra las dimensiones del cuadro

        # Buscamos el contorno de las áreas con movimiento para poder resaltarlas y analizarlas en un detector de cara por ejemplo
        (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # ,_ = sin interés en la jerarquía de contornos | RETR_EXTERNAL = solo contornos externos | CHAIN_APPROX_SIMPLE = compresión de contornos

        for contour in cnts:                                                         # Iterar sobre los contornos encontrados
            if cv2.contourArea(contour) < 10000:                                      # Ignorar contornos pequeños para reducir falsas detecciones
                continue
            status = 1                                                               # Indicar que se ha detectado movimiento
            (x, y, w, h) = cv2.boundingRect(contour)                                 # Obtener el rectángulo delimitador del contorno
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)             # Dibujar un rectángulo verde alrededor del área con movimiento
        
        status_list.append(status)                                                  # Agregar el estado actual a la lista de estados

        status_list = status_list[-2:]                                              # Mantener solo los últimos dos estados en la lista

        # Mejorar la detección de transiciones para evitar falsos positivos
        if len(status_list) == 2:
            if status_list[-1] == 1 and status_list[-2] == 0:                       # Detectar transición de sin movimiento a con movimiento
                print("Movimiento detectado!")
                times.append(datetime.now())                                        # Registrar el tiempo de inicio del movimiento
            elif status_list[-1] == 0 and status_list[-2] == 1:                     # Detectar transición de con movimiento a sin movimiento
                print("Movimiento detenido!")
                times.append(datetime.now())                                        # Registrar el tiempo de fin del movimiento

        cv2.imshow("Cámara en Vivo", frame)                                         # Mostrar el cuadro capturado
        cv2.imshow("Diferencia Absoluta", delta_frame)                              # Mostrar la diferencia absoluta
        cv2.imshow("Umbral de Diferencia", thresh_frame)                            # Mostrar el umbral de la diferencia

        key = cv2.waitKey(1)                                                        # Esperar hasta que se presione una tecla

        if key == ord('q'):                                                         # Salir del bucle si se presiona 'q'
            if status == 1:
                times.append(datetime.now())                                        # Registrar el tiempo si se está detectando movimiento al salir
            print("\nSaliendo del bucle por presionar 'q'...")
            break

    # Procesar los tiempos para crear intervalos válidos
    print(f"Procesando {len(times)} timestamps registrados...")
    
    # Determinar si cada timestamp corresponde a inicio o fin de movimiento
    intervals = []
    current_start = None
    
    for i, timestamp in enumerate(times):
        # Determinar si es inicio o fin basándose en la posición en la lista
        is_movement_start = (i % 2 == 0)
        
        if is_movement_start:
            if current_start is None:
                current_start = timestamp
                print(f"Inicio de movimiento: {timestamp}")
            else:
                # Hay un inicio previo sin cerrar, crear intervalo con timestamp anterior
                if i > 0:
                    intervals.append({"Start": current_start, "End": times[i-1]})
                    print(f"Intervalo forzado: {current_start} - {times[i-1]}")
                current_start = timestamp
                print(f"Nuevo inicio de movimiento: {timestamp}")
        else:  # es fin de movimiento
            if current_start is not None:
                intervals.append({"Start": current_start, "End": timestamp})
                print(f"Fin de movimiento: {timestamp} (Duración: {(timestamp - current_start).total_seconds():.2f}s)")
                current_start = None
            else:
                print(f"Fin de movimiento sin inicio previo ignorado: {timestamp}")
    
    # Si quedó un movimiento sin cerrar, usar el último timestamp o el tiempo actual
    if current_start is not None:
        end_time = datetime.now()
        intervals.append({"Start": current_start, "End": end_time})
        print(f"Movimiento final cerrado automáticamente: {current_start} - {end_time}")
    
    # Convertir intervalos a DataFrame
    for interval in intervals:
        df = df._append(interval, ignore_index=True)

    df.to_csv("Times.csv", index=False)
    print(f"Archivo Times.csv actualizado con {len(df)} intervalos de movimiento")

    video.release()                                                                 # Liberar el objeto de captura de video
    cv2.destroyAllWindows()                                                         # Cerrar todas las ventanas abiertas