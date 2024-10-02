# quiz_scripting
Propietario: Lucía Villarreal Lara
# Descripción del proyecto:
Este proyecto es un script en Python que analiza archivos de texto en un directorio y genera un informe con información resumida sobre los archivos encontrados. El script cuenta el número de líneas, palabras y ocurrencias de la palabra "python" en cada archivo de texto.
# Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/tu-repo.git
   cd tu-repo

Asegúrate de tener Python instalado en tu sistema. 
Puedes verificarlo ejecutando:
python --version

# Explicación de la implementación del código:
El script utiliza la biblioteca os para interactuar con el sistema de archivos y la biblioteca sys para acceder a los argumentos de la línea de comandos.
La función analizar_archivo analiza un archivo de texto y devuelve un tupla con el número de líneas, palabras y ocurrencias de la palabra "python". Si no se puede analizar el archivo, devuelve None.
La función generar_informe utiliza la función analizar_archivo para analizar cada archivo de texto en el directorio y genera un informe con la información resumida.

# Imágenes de la ejecución:


# Formato de Markdown:


# Estructura del Código
import os
import sys

def analizar_archivo(trayecto_archivo):
    ...
    
def generar_informe(directorio):
    ...
    
if __name__ == "__main__":
    ...

# Conclusión:
Este script es una herramienta útil para analizar archivos de texto y generar informes con información resumida. Espero que sea de utilidad para ti. ¡Si tienes alguna pregunta o necesitas ayuda, no dudes en preguntar!