import cv2
import time
import pandas
from datetime import datetime 

# Para mas cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

firstFrame = None                                                               # Inicializar el primer cuadro para la detección de movimiento   

status_list = [None, None]                                                      # Lista para almacenar el estado de movimiento
times = []                                                                      # Lista para almacenar los tiempos de movimiento
df = pandas.DataFrame(columns=["Start", "End"])                             # DataFrame para almacenar los intervalos de movimiento

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)                                      # Usar DirectShow en Windows para evitar bloqueos

print("Cámara abierta:", video.isOpened())                                      # Verificar si la cámara se abrió correctamente

if not video.isOpened():
    print("ERROR: No se pudo abrir la cámara 0. Intenta con índice 1 o verifica que no esté en uso.")
    video.release()
    exit()

while True:
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
    if status_list[-1] == 1 and status_list[-2] == 0:                           # Detectar transición de sin movimiento a con movimiento
        print("Movimiento detectado!")
        times.append(datetime.now())                                            # Registrar el tiempo de inicio del movimiento
    elif status_list[-1] == 0 and status_list[-2] == 1:                         # Detectar transición de con movimiento a sin movimiento
        print("Movimiento detenido!")
        times.append(datetime.now())                                            # Registrar el tiempo de fin del movimiento

    cv2.imshow("Cámara en Vivo", frame)                                         # Mostrar el cuadro capturado
    cv2.imshow("Diferencia Absoluta", delta_frame)                              # Mostrar la diferencia absoluta
    cv2.imshow("Umbral de Diferencia", thresh_frame)                            # Mostrar el umbral de la diferencia

    key = cv2.waitKey(1)                                                        # Esperar hasta que se presione una tecla

    print(delta_frame)                                                          # Imprimir la matriz de diferencia absoluta
    if key == ord('q'):                                                         # Salir del bucle si se presiona 'q'
        if status == 1:
            times.append(datetime.now())                                        # Registrar el tiempo si se está detectando movimiento al salir
        print("Saliendo del bucle...")
        break

for i in range(0, len(times), 2):                                              # Iterar sobre los tiempos en pares
    df = df._append({"Start": times[i], "End": times[i + 1]}, ignore_index=True) # Agregar los intervalos de movimiento al DataFrame

df.to_csv("../Seccion_18/Times.csv")                                                          # Guardar los tiempos en un archivo CSV

video.release()                                                                 # Liberar el objeto de captura de video
cv2.destroyAllWindows()                                                         # Cerrar todas las ventanas abiertas