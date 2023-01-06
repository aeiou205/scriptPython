import exifread

# Abre la imagen
with open('re.jpeg', 'rb') as f:
    # Lee los metadatos de la imagen
    tags = exifread.process_file(f)
    # Muestra todos los metadatos
    print(tags)
    #modelo = tags['Image Model']