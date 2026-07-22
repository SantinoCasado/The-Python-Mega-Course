import cv2
import time

# Para mas cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)                              # Usar DirectShow en Windows para evitar bloqueos

print("Cámara abierta:", video.isOpened())                              # Verificar si la cámara se abrió correctamente

if not video.isOpened():
    print("ERROR: No se pudo abrir la cámara 0. Intenta con índice 1 o verifica que no esté en uso.")
    video.release()
    exit()

check, frame = video.read()                                             # Leer un cuadro de la cámara

print("Check:", check)                                                  # Indica si la lectura fue exitosa (True/False)
print("Frame shape:", frame if check else "No se capturó frame")        # Muestra las dimensiones del cuadro

grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                                 # Convertir a escala de grises (no se muestra)

print("Esperando 3 segundos...")
time.sleep(3)                                                           # Esperar 3 segundos para que la cámara se inicie correctamente

cv2.imshow("Cámara en Vivo", frame)                                     # Mostrar el cuadro capturado
cv2.imshow("Cámara en Vivo", grey)                                      # Mostrar el cuadro capturado


cv2.waitKey(0)                                                          # Esperar hasta que se presione una tecla
video.release()                                                         # Liberar el objeto de captura de video
cv2.destroyAllWindows()                                                 # Cerrar todas las ventanas abiertas