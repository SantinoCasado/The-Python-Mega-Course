import cv2

# Para mas cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # Cargar el clasificador preentrenado para detección de rostros

img = cv2.imread('Seccion_17/images/photo.jpg')                                 # Leer la imagen donde se buscarán rostros
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                    # Convertir la imagen a escala de grises (mejora la detección)

twoFaces = cv2.imread('Seccion_17/images/news.jpg')  
twoFacesGray = cv2.cvtColor(twoFaces, cv2.COLOR_BGR2GRAY)                       # Convertir la otra imagen a escala de grises

faces = face_cascade.detectMultiScale(                                          # Detectar rostros en la imagen
                                        gray, 
                                        scaleFactor=1.05,                       # Factor de escala para el tamaño de la imagen (1.05 = 5% más pequeña en cada escala)
                                        minNeighbors=5                          # Número mínimo de vecinos que debe tener un rectángulo candidato para ser retenido
                                        )

multiplefaces = face_cascade.detectMultiScale(
                                        twoFacesGray, 
                                        scaleFactor=1.1,                        # Con 1.05 dectaria la mano del hombre de la dercha como un rostro, con 1.1 solo el de la mujer
                                        minNeighbors=5
                                        )


print(f"Se encontraron {len(faces)} rostros")                                   # Imprimir el número de rostros detectados
print(f"Faces: {faces}")                                                        # Imprimir las coordenadas de los rostros detectados

print(f"Se encontraron {len(multiplefaces)} rostros en la segunda imagen")
print(f"Faces: {multiplefaces}")

for x, y, w, h in faces:                                                        # Dibujar rectángulos alrededor de los rostros detectados
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)            # Dibujar rectángulo verde con grosor 2
    gray = cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)          # Dibujar rectángulo verde en la imagen en escala de grises

for x, y, w, h in multiplefaces:
    twoFaces = cv2.rectangle(twoFaces, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Dibujar rectángulo azul en la otra imagen con dos rostros

resized= cv2.resize(img, (int(img.shape[1]//3), int(img.shape[0]//3)))          # Redimensionar la imagen para mejor visualización

cv2.imshow('Gray image', gray)                                                  # Mostrar la imagen en escala de grises
cv2.imshow('Original image', img)                                               # Mostrar la imagen original con los rostros detectados
cv2.imshow('Detected Faces', resized)                                           # Mostrar la imagen con los rostros detectados
cv2.imshow('Two Faces', twoFaces)                                               # Mostrar la otra imagen con dos rostros detectados
cv2.waitKey(0)
cv2.destroyAllWindows()
