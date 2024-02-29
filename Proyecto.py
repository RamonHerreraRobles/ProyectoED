# Aquí en el main importamos las funciones y las llamamos
from Funciones_Proyecto import *
import csv

# Leemos el fichero de liga
datos = LeerPartidos("liga.csv")

# Imprimimos los datos
impClasificacion(datos)

