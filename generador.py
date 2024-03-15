import os

def generar_html_lista_archivos():
    # Obtener el directorio actual
    directorio_actual = os.path.dirname(os.path.realpath(__file__))

    # Obtener la lista de archivos en el mismo directorio excluyendo los que empiezan por "index"
    archivos = [archivo for archivo in os.listdir(directorio_actual) if os.path.isfile(os.path.join(directorio_actual, archivo)) and not archivo.startswith("index") and not archivo.startswith(".DS_Store") and not archivo.endswith(".py") and not archivo.startswith(".")]
    archivos =  sorted(archivos)
    # Crear el contenido HTML
    contenido_html = "<html>\n<head>\n<h1>Kodi</h1>\n</head>\n"

    for archivo in archivos:
        contenido_html += f'<li><a href="{archivo}">{archivo}</a></li>\n'

    contenido_html += "</body>\n</html>"

    # Guardar el contenido en un archivo HTML
    with open("index.html", "w") as archivo_html:
        archivo_html.write(contenido_html)

    print("Se ha generado el archivo HTML: index.html")

if __name__ == "__main__":
    generar_html_lista_archivos()




# PRE COMMIT SH
# 
# #!/bin/sh
# 
# 
# # Run your Python script
# python generador.py
# 
# # Add all new files to the commit
# git add --all
# 
# # Continue with the default pre-commit actions
# exit 0