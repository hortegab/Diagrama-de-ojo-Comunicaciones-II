# Diagrama-de-ojo-Comunicaciones-II
Es una Libreria probada en Python 2.7. Una vez instalada, cuentas con la posibilidad de usar, en cualquier programa de Python 2.7, la función que permite graficar el diagrama de ojo de una señal y con Sps muestras por símbolo: 

eyediagram(y, Sps,) 

Algunas observacione:
1) y es el vector que contiene las muestras de la señal para la cual se desea graficar el diagrama de ojo. 
2) Se supone que corresponde a una señal digital con Sps muestras por simbolo.
3) Para poder usar esa función, tu código de python debe importar previamente la libreria.
4) Esta aplicción no está integrada a gnuradio, de manera que lo que hacemos es lo siguiente: con un flujograma de gnuradio generamos uno o mas archivos de señales a las cuales queremos ver el diagrama de ojo. Escribimos un programa en python que lea esos esos archivos, importe la libreria y use la función mencionada para generar el diagrama de ojo.


Nota: Hemos realizado esta copia a partir de la original, del autor, para realizarle mejoras y complementos para y poder usarla con  propósitos pedagógicos junto con flujogramas de gnuradio. Aspiramos usar parte del codigo para lograr crear un bloque de gnuradio que saque el diagrama de ojo de manera similar a lo que hace esta aplicación, pero que sea parte de gnuradio, pues por ahora funciona deparado de gnuradio.

Todas las instrucciones de instalación y pruebas están en: 

https://www.overleaf.com/read/mxdwhbddzjhv
