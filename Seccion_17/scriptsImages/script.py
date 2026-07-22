import cv2

# Leer la imagen
imgColor = cv2.imread('Seccion_17/images/galaxy.jpg', 1) # El '1' indica que se lee en color
imgGray = cv2.imread('Seccion_17/images/galaxy.jpg', 0) # El '0' indica que se lee en escala de grises
imgAlpha = cv2.imread('Seccion_17/images/galaxy.jpg', -1) # El '-1' indica que se lee con canal alfa si existe (transparencia)

print("Dimensiones de la imagen en color:", imgColor.shape)             # Output: (alto, ancho, canales)
print("Dimensiones de la imagen en escala de grises:", imgGray.shape)   # Output: (alto, ancho)
print("Dimensiones de la imagen con canal alfa:", imgAlpha.shape)       # Output: (alto, ancho, canales)

print(imgColor)                                                         # Muestra los valores de los píxeles
print("Dimensiones de la imagen en color:", imgColor.ndim)              # Output: 3 (canales de color BGR)
cv2.imshow('Imagen en Color', imgColor)
cv2.waitKey(0)                                                          # Espera hasta que se presione una tecla
cv2.destroyAllWindows()


print("-------------------------------")
print(imgGray)                  
print("Dimensiones de la imagen en escala de grises:", imgGray.ndim)    # Output: 2 (solo intensidad)
cv2.imshow('Imagen en Escala de Grises', imgGray)   
cv2.waitKey(3000)                                                       # Espera 3000 ms (3 segundos)                          
cv2.destroyAllWindows()

print("-------------------------------")
print(imgAlpha)
print("Dimensiones de la imagen con canal alfa:", imgAlpha.ndim)
cv2.imshow('Imagen con Canal Alfa', imgAlpha)
cv2.waitKey(3000)
cv2.destroyAllWindows()

print("-------------------------------")
resizedImg = cv2.resize(imgColor, (1000, 600))               # Redimensionar la imagen a 1000x600 píxeles
cv2.imshow('Imagen Redimensionada', resizedImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Seccion_17/images/galaxy_resized.jpg', resizedImg)  # Guardar la imagen redimensionada
