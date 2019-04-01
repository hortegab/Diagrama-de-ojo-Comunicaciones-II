# Diagrama-de-ojo-Comunicaciones-II
Es una Libreria probada en Python 2.7 que sirve para poder usar en la programación en python la función: 

eyediagram(y, Sps,) 

La función recibe una señal de entrada en el parametro y, que se supone que corresponde a una señal digital con Sps muestras por simbolo. Como resultado, la función prodcue la grafica del diagrama de ojo pero la desja lista para que sea mostrada por algunas de las herramientas de visualizacion disponibles como matplolib, entre muchas otras.

Hemos realizado esta copia a partir de la original, del autor, para realizarle mejoras y complementos para y usarla con  propósitos pedagógicos junto con flujogramas de gnuradio. Aspiramos usar parte del codigo para lograr crear un bloque de gnuradio que saque el diagrama de ojo de manera similar a lo que hace esta aplicación. De momento, lo que estamos logrando es esto: un flujograma genera uno o mas archivos de señales de interés, un programa en python lee esos archivos y le aplica la función eyediagram para generar el diagrama de ojo.

Todas las instrucciones de instalación y pruebas están en: 

https://www.overleaf.com/read/mxdwhbddzjhv
