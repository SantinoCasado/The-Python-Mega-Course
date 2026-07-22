import cv2
import os
import glob

# Directorio con las imágenes originales
img_dir = "Seccion_17/images"
# Directorio donde se guardarán las redimensionadas
output_dir = "Seccion_17/imagesResized"

# Obtener todas las imágenes del directorio (jpg, png, jpeg)
images = glob.glob(os.path.join(img_dir, "*.jpg"))

# Dimensiones para redimensionar
new_width = 100
new_height = 100

# Procesar cada imagen
for img_path in images:
    # Excluir galaxy_resized
    if "galaxy_resized" in img_path:
        print(f"Saltando: {img_path}")
        continue
    
    # Leer la imagen
    img = cv2.imread(img_path)
    
    if img is None:
        print(f"No se pudo leer: {img_path}")
        continue
    
    # Redimensionar a 100x100
    img_resized = cv2.resize(img, (new_width, new_height))
    
    # Crear nombre del archivo redimensionado
    filename = os.path.basename(img_path)
    name, ext = os.path.splitext(filename)
    output_path = os.path.join(output_dir, f"{name}_resized{ext}")
    
    # Guardar la imagen redimensionada
    cv2.imwrite(output_path, img_resized)
    print(f"Redimensionada: {filename} -> {name}_resized{ext}")

print("\n¡Proceso completado!")
