

#############################################################
#############################################################
# OrganizaDescargas
#############################################################
# -> Autor
#############################################################
# Script by @VictorMVila [GitHub]
#############################################################
# -> Descripcion
#############################################################
# Script que organiza en carpetas de escritorio el contenido
# del directorio Descargas según el formato de los ficheros.
#############################################################
# -> Soporte
#############################################################
# Windows
#############################################################

import os
import shutil
import time
import sys
import getpass

try:
    from zipfile import ZipFile
except ImportError: 
    print("Error. ZipFile module is required")
    time.sleep(1)
    print("Execute 'pip install zipfile' in cmd")
    time.sleep(1)
    exit()

try:
    from rarfile import RarFile
except ImportError:
    print("Error. RarFile module is required")
    time.sleep(1)
    print("Execute 'pip install rarfile' in cmd")
    time.sleep(1)
    exit()

# Se cierran clientes P2P que puedan tener ficheros en uso del directorio a organizar.
os.chdir("C:/Windows/system32")
if not os.system("taskkill /f /im qbittorrent.exe") == 128:
    print("Cliente P2P QBittorrent cerrado")        
if not os.system("taskkill /f /im utorrent.exe") == 128:
    print("Cliente P2P Utorrent cerrado")

# Rutas
nombreUsuario = getpass.getuser()
rutaDescargas = "C:/Users/" + nombreUsuario + "/Downloads"
nombreCarpetaVideos = "Peliculas"
pathCarpetaVideos = "C:/Users/" + nombreUsuario + "/Desktop/" + nombreCarpetaVideos
pathCarpetaDocumentos = "C:/Users/" + nombreUsuario + "/Desktop/Documentos"

# Si no existen los directorios que guardarán los ficheros de Descargas, se crean
if not os.path.isdir(pathCarpetaVideos):
    os.mkdir(pathCarpetaVideos)    
if not os.path.isdir(pathCarpetaDocumentos):
    os.mkdir(pathCarpetaDocumentos) 

print("#########################")
print("#######BIENVENIDO########")
print("#########################")
time.sleep(1)
print("")
print("##VAMOS A EXAMINAR EL DIRECTORIO " + rutaDescargas)
print("")


# Recorremos recursivamente los directorios de rutaDescargas utilizando os.walk
# os.walk reproduce tres tuplas: 

# --> dirpath o rutas que se van encontrando,
# --> dirnames o nombres de los directorios que se van encontrando,
# --> y filenames o nombres de los ficheros que se van encontrando.

for dirpath, dirnames, filenames in os.walk(rutaDescargas):
    #Directorio actual
    os.chdir(dirpath)
    time.sleep(0.5)
    #Recorremos los ficheros del directorio
    for f in filenames:
        print("-> Fichero " + f)
        #Splitext divide en nombre y extension un fichero
        nombre, extension = os.path.splitext(f)
        #Si la extension es MKV, AVI, MP4, MPG o MOV, se procede a mover 
        if (extension==".mkv" or extension==".avi" or extension==".mp4" 
            or extension==".mpg" or extension==".mov"):
            print("##########################################")
            print("#############VIDEO DETECTADO##############")
            print("##########################################") 
            time.sleep(1)
            #El modulo shutil permite realizar operaciones con ficheros.
            #Recibe el path str (ruta de origen del fichero) y el path dst (ruta de destino)
            try:
                shutil.move(os.path.abspath(f),pathCarpetaVideos)
                print("Se ha movido el fichero " + f + " a la carpeta Videos")
            except shutil.Error:
                print("El archivo ya existe en el directorio de destino")
            
            time.sleep(1)
        if (extension==".pdf" or extension==".doc" or extension==".docx" or extension==".odt" 
            or extension==".xls" or extension==".xlsx" or extension=="pptx" or extension=="ppt"):
            print("##########################################")
            print("###########DOCUMENTO DETECTADO############")
            print("##########################################") 
            time.sleep(1)
            shutil.move(os.path.abspath(f),pathCarpetaDocumentos)
            print("Se ha movido el fichero " + f + " a la carpeta Documentos")
            time.sleep(1)
        if extension==".zip" or extension==".rar":
            print("##########################################")
            print("#######FICHERO COMPRIMIDO DETECTADO#######")
            print("##########################################")
            time.sleep(1)
            print("Contenido:")
            time.sleep(1)
            if extension==".rar":
                try:
                    os.rename(f,nombre+".zip")
                except FileExistsError:
                    print("Se intenta renombrar un archivo cuyo nombre corresponde al de otro ya existente")
                
            with ZipFile(f,'r') as zip:
                zip.printdir()
                time.sleep(1)
                print("Extrayendo archivos")
                zip.extractall(nombre)
                time.sleep(1)
                print("Extracción completada")
                
            time.sleep(1)
            
print("")
time.sleep(0.5)
print("Examen de directorio finalizado")
print("")
time.sleep(0.5)
print("¿Desea vaciar el contenido de la carpeta " + rutaDescargas + "? [Y/N]",end="")
orden = input()

end = False
while not end:
    if orden=="Y" or orden=="y":
        print("Se procede al borrado de la carpeta " + rutaDescargas)
        time.sleep(1)
        ignore_errors  = (sys.platform=="win32")
        #Shutil también permite borrar todo el árbol de directorios que surge de uno,
        #así como sus ficheros
        shutil.rmtree(rutaDescargas, ignore_errors = ignore_errors)
        time.sleep(1)
        print("Borrado completo")
        time.sleep(1)
        end=True
    elif orden=="N" or orden=="n":
        print("No se borrará el contenido de la carpeta " + rutaDescargas)
        time.sleep(1)
        print("Programa finalizado")
        time.sleep(1)
        end=True
    else: 
        print("Orden inválida. Introduzca de nuevo [Y/N]: ", end="")
        orden=input()
        
