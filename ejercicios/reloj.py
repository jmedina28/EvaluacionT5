# importo librerias
import datetime
import time
import os

while(True):
	os.system('cls') # cada vez que se ejecute el bucle se borra el print anterior
	dt = datetime.datetime.now() # se obtiene la fecha y hora actual 
	print( "{}:{}:{}".format( dt.hour, dt.minute, dt.second ) ) # se imprime la fecha y hora actual
	time.sleep(1) # se duerme el programa durante 1 segundo