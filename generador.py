import os

def getPrefix(archivo):
    if archivo.startswith("plugin.video.cristalazul-"):
        return "Cristal Azul - "
    elif archivo.startswith("plugin.video.moestv-"):
        return "Moestv - "
    elif archivo.startswith("plugin.video.movistarplus"):
        return "Movistarplus - "
    elif archivo.startswith("repository.GTKing-Matrix-"):
        return "Repo GTKing-Matrix - "
    elif archivo.startswith("repository.KODIvertiDO_TEAM-"):
        return "Repo KODIvertiDO_TEAM - "
    elif archivo.startswith("repository.Luar"):
        return "Repo Luar - "
    elif archivo.startswith("repository.alfa-addon-"):
        return "Repo alfa - "
    elif archivo.startswith("repository.bugatsinho-"):
        return "Repo bugatsinho (sports) - "
    elif archivo.startswith("repository.elementumorg-"):
        return "Repo elementum - "
    elif archivo.startswith("script.limpiarkodi-"):
        return "Script limpiar kodi - "
    elif archivo.startswith("script.luar-"):
        return "Luar - "
    elif archivo.startswith("script.module.horus-"):
        return "Horus - "
    elif archivo.startswith("script.module.ttml2ssa-"):
        return "Script Ttml2ssa - "
    elif archivo.startswith("script.module.resolveurl-"):
        return "Script Resolveurl - "
    else:
        return ""

def generar_html_lista_archivos():
    # Obtener el directorio actual
    directorio_actual = os.path.dirname(os.path.realpath(__file__))

    # Obtener la lista de archivos en el mismo directorio excluyendo los que empiezan por "index"
    archivos = [archivo for archivo in os.listdir(directorio_actual) if os.path.isfile(os.path.join(directorio_actual, archivo)) and not archivo.startswith("index") and not archivo.startswith(".DS_Store") and not archivo.endswith(".py")]
    archivos =  sorted(archivos)
    # Crear el contenido HTML
    contenido_html = "<html>\n<head>\n<h1>Kodi</h1>\n</head>\n"

    for archivo in archivos:
        prefix = getPrefix(archivo)
        contenido_html += f'<li><a href="{archivo}">{prefix}{archivo}</a></li>\n'

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