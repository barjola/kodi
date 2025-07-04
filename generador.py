import os

def generar_html(directorio):
    archivos = [archivo for archivo in os.listdir(directorio) if not archivo.startswith("index") and not archivo.startswith(".DS_Store") and not archivo.endswith(".py") and not archivo.startswith(".")]
    archivos =  sorted(archivos)
    
    contenido_html = "<html>\n<head>\n<h1>Kodi</h1>\n</head>\n"

    for archivo in archivos:
        if os.path.isfile(os.path.join(directorio, archivo)):
            if archivo == "persianas.html":
                contenido_html += f'<li><a href="{archivo}" download>{archivo}</a></li>\n'
            else:
                contenido_html += f'<li><a href="{archivo}">{archivo}</a></li>\n'
        else:
            generar_html(os.path.join(directorio, archivo))
            contenido_html += f'<li><a href="{archivo}/">{archivo}/</a></li>\n'

    contenido_html += "</body>\n</html>"

    # Guardar el contenido en un archivo HTML
    with open(directorio + "/index.html", "w") as archivo_html:
        archivo_html.write(contenido_html)

    print("Se ha generado el archivo HTML: " + directorio + "/index.html")

def generar_html_lista_archivos():
    directorio_actual = os.path.dirname(os.path.realpath(__file__))

    generar_html(directorio_actual)

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