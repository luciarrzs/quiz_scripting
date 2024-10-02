import os
import sys

def analizar_archivo(trayecto_archivo):
    try:
        with open(trayecto_archivo, 'r') as archivo:
            contenido = archivo.read()
            lineas = contenido.count('\n') + 1
            palabras = len(contenido.split())
            simultaneidad_python = contenido.lower().count('python')
            return lineas, palabras, simultaneidad_python
    except FileNotFoundError:
        return None
    except PermissionError:
        return None

def generar_informe(directorio):
    informe = ""
    archivos_txt = [archivo for archivo in os.listdir(directorio) if archivo.endswith('.txt')]
    if not archivos_txt:
        informe += "No fue posible encontrar archivos de texto\n"
    else:
        for archivo in archivos_txt:
            trayecto_archivo = os.path.join(directorio, archivo)
            resultado = analizar_archivo(trayecto_archivo)
            if resultado is None:
                informe += f"Error: Imposibilidad para analizar el archivo {archivo}\n\n"
            else:
                lineas, palabras, simultaneidad_python = resultado
                informe += f"Archivo: {archivo}\n"
                informe += f"Líneas: {lineas}\n"
                informe += f"Palabras: {palabras}\n"
                informe += f"Simultaneidad de la palabra Python: {simultaneidad_python}\n\n"
    with open(os.path.join(directorio, 'informe.txt'), 'w') as archivo_informe:
        archivo_informe.write(informe)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <directorio>")
        sys.exit(1)
    directorio = sys.argv[1]
    generar_informe(directorio)