# Diagrama-de-ojo-Comunicaciones-II
Es una Libreria probada en Python 2.7. Una vez instalada, cuentas con la posibilidad de usar, en cualquier programa de Python 2.7, dos funciones así: 

demo_data(num_symbols, Sps): permite generar una señal de prueba, para comprobar que la siguiente funcion hace bien su trabajo. num_symbols: es el número de simbolos en esa señal: Sps: es el núemro de muestras por simbolo (Samples per simbol). Por ejemplo: y=demo_data(1000, 24) llenará el vector "y" con las muestras de una señal digital demostrativa, con 1000 simbolos y cada uno de a 24 muestras.

eyediagram(y, Sps, offset, graptool): grafica el diagrama de ojo de "y". A continuación, los parámetros que restan por explicar. offset: es un parámetro para desplazar el ojo en offset muestras; graptool: es un parámetro que el tipo de herramienta gráfica a usar entre las que se tienen en python. Esto se verá mejor en el ejemplo de abajo cuando se usa matplolib, pero la idea que que se puedan usar otras.

Proceso a seguir:
1) El proces sería tan simple como inr a la carpeta "Instalacion" y dar el comando:
sudo python setup.py install
El problema es que se requiere librerias preinstaladas en pyhton. De manera que el consejo es que sigas la guia del siguiente enlace: https://www.overleaf.com/read/mxdwhbddzjhv

Prueba preliminar:
Escribe un programa en Pyhton que, usando las dos funciones de la libreria, genere una señal de pruebas y muestre su diagrama de ojo. Ese programa puede ser el siguiente y aparece en la carpeta ejemplo:

from eyediagram.demo_data import demo_data
from eyediagram.mpl import eyediagram
import matplotlib.pyplot as plt

#Generamos senal de ejemplo  
num_symbols = 1000
samples_per_symbol = 24
y = demo_data(num_symbols, samples_per_symbol)

#Llamamos el modulo que instalamos
eyediagram(y, 2*samples_per_symbol, offset=16, cmap=plt.cm.coolwarm)

#Graficamos
plt.show()

Prueba con gnuradio:
Esta aplicción no está integrada a gnuradio, de manera que lo que hacemos es lo siguiente: con un flujograma de gnuradio generamos uno o mas archivos de señales a las cuales queremos ver el diagrama de ojo. Escribimos un programa en python que lea esos esos archivos, importe la libreria y use la función mencionada para generar el diagrama de ojo. En la carpeta "GNU Radio" hemos pusto un ejemplo de flujograma generador y un programa en python para graficar el Ojo. 


Nota: Hemos realizado esta copia a partir de la original, del autor, para realizarle mejoras y complementos para y poder usarla con  propósitos pedagógicos junto con flujogramas de gnuradio. Aspiramos usar parte del codigo para lograr crear un bloque de gnuradio que saque el diagrama de ojo de manera similar a lo que hace esta aplicación, pero que sea parte de gnuradio, pues por ahora funciona deparado de gnuradio.

Como ya se dijo, todas las instrucciones de instalación y pruebas están en: 

https://www.overleaf.com/read/mxdwhbddzjhv
