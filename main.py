from Modelo.organizador import GestorCartera, Exportador
import os
lista = []
booleano = False
while booleano != True:
    archivo = str(input("Ingrese el nombre del archivo proporcionado: "))
    gestor = GestorCartera(archivo)
    lista, booleano, mensaje = gestor.procesar_datos()
    print(mensaje)
nombre_excel = str(input("Que nombre desea ponerle al archivo de excel: "))+".xlsx"
exportador = Exportador(lista, nombre_excel)
mensaje = exportador.exportar_a_excel()
print(mensaje)
os.system(nombre_excel)