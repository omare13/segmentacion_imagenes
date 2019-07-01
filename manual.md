# Interfaz de anotaciones
1. Precondiciones
2. Carga de imágenes
3. Edición
4. Guardado

## 1. Precondiciones
Para que el programa funcione adecuadamente, se debe respetar el siguiente árbol de ficheros:

--ejecutables
--etiquetas.txt
--TEST
----ANOTACIONES
-------NOMBRE_1
-------NOMBRE_N
----IMAGENES
-------NOMBRE_1
-------NOMBRE_N

Donde:
- `ejecutables` son una serie de ficheros que forman la aplicación.
- `etiquetas.txt` es el fichero de texto usado para cargar las posibles etiquetas de las anotaciones. Este fichero contiene una etiqueta por línea y se actualiza siempre que se cierra el programa.
- La carpeta `TEST` debe contener las carpetas `IMAGENES` y `ANOTACIONES`. Dentro de cada una de ellas, se deben encontrar los mismos nombres de carpeta tanto para las sub-carpetas que contendrán imágenes como para las sub-carpetas que contengan anotaciones. **Es dentro de las sub-carpetas de ANOTACIONES donde se encontrarán los grafos generados**


## 2. Carga de Imágenes

Existen dos opciones a la hora de cargar imágenes para su anotación: 

- Menú > Abrir Imagen: permite abrir una única imagen para su anotación.
- Menú > Abrir Carpeta: permite cargar todas las imágenes que se encuentren en una sub-carpeta de `IMAGENES`. Para cambiar de una imagen a otra, se deben utilizar los botones superiores `<-` y `->`. Se debe tener en cuenta que **cada vez que se cambia de imagen, se guardará el estado final de las anotaciones y se generará el grafo** de manera automática.
## 3. Edición

Una vez que se dipone de una o varias imágenes cargadas, es posible editarlas. 

En cualquier momento, se podrá ampliar o reducir la imagen cargada aumentando o reduciendo el **zoom**, el cual se sitúa en la parte superior derecha de la ventana. Este puede aumentarse o reducirse con los botones o con la rueda del ratón, siempre que el puntero del ratón esté situado sobre el mismo.

Si se desea que de forma automática el programa reclame al usuario un comentario cada vez que incluye una nueva anotación, será necesario marcar la opción **"Comentario Automático"** situado en la parte superior derecha de la ventana. Esta opción se puede marcar o desmarcar en cualquier momento.

### Incluir anotación
Siempre que se desee añadir una nueva anotación, se debe seleccionar la etiqueta de la anotación del menú desplegable situado a la derecha del botón `Iniciar Edición`.

Seguidamente, pulsamos sobre el botón `Iniciar Edición` para entrar en modo edición. Se debe tener en cuenta que durante este modo, la selección de los elementos visuales presentados sobre la imagen sólo son seleccionables desde los listados de puntos y segmentos laterales.

Para incluir anotaciones:

- Estando en modo edición, hacer click derecho para incluir un **nuevo punto** acorde a la etiqueta seleccionada.
- Estando en modo edición, hacer click izquierdo para comenzar la edición de un **nuevo segmento** acorde a la etiqueta seleccionada.
	- Hacer click derecho para terminar la edición de segmento incluyendo una línea desde el último punto del segmento hasta el punto en el que se hizo click.
	- Pulsar la tecla `ESC` para terminar la edición del segmento hasta el último punto del segmento creado. En este caso, si el segmento creado no contiene líneas, pulsar la tecla `ESC` resultará en la adición de un nuevo punto en base a la etiqueta seleccionada.
- Estando en modo edición, hacer click izquierdo sobre el botón `Parar Edición` para salir del modo edición. Esto permite seleccionar los puntos o segmentos representados sobre la imagen.

Tanto los puntos como los segmentos se mostrarán en el correspondiente listado de la parte derecha de la ventana, quedando estos nombrados según la etiqueta seleccionada y un nombre asignado por el sistema que puede ser modificado.

Si se tiene marcada la opción "Comentario Automático", cada vez que se añada un nuevo segmento o punto, el programa abrirá una ventana para que el usuario pueda cambiar el nombre del elemento así como **incluir un comentario** sobre el mismo.

### Modificación de anotaciones
Cuando se disponen de elementos de anotación (segmentos o puntos), podremos **cambiar su nombre** e **incluir un comentario** haciendo doble click en el ítem de la lista de segmentos o lista de puntos que se desee.

Tabmién podemos acceder a la ventana de comentarios si se realiza doble click sobre uno de los elementos visuales correspondientes a la anotación, **siempre y cuando el modo edición no esté activo**.

Por otra parte, si se desean **eliminar elementos**, se debe hacer click izquierdo sobre el ítem de la lista de segmentos o lista de puntos que se desee eliminar. Una vez seleccionado, el elemento visual correspondiente quedará resaltado en rojo y pulsaremos el botón `DEL` para proceder a su borrado. También es posible seleccionar los elementos visuales haciendo click izquierdo sobre los mismos, quedando seleccionado el ítem de la lista correspondiente y preparado así para su borrado pulsando el botón `DEL`.
### Inclusión de etiquetas
Para añadir una nueva etiqueta no presente en el menú desplegable de la derecha del botón `Iniciar Edición`, basta con editar el texto seleccionado y pulsar `INTRO`. De esta forma, el texto modificado se incluirá como una nueva etiqueta.

## 4. Guardado

Si únicamente se ha abierto una imagen, será necesario seleccionar "Edición > Guardar" para proceder a la generación del grafo y el guardado de todas las anotaciones facilitadas sobre la imagen actual.

Si se ha cargado una carpeta con varias imágenes, el guardado se realizará de manera automática al cambiar de imagen usando los botones `<-` y `->`. De todas formas, también es posible su guardado seleccionando "Edición > Guardar".

El guardado generará hasta tres ficheros por imagen (dentro de la sub-carpeta de `ANOTACIONES` correspondiente):
	- `["nombre_imagen"]_puntos.pickle` : almacena los puntos en formato comprimido si existen (se recomienda no modificar)
	- `["nombre_imagen"]_segmentos.pickle` : almacena los segmentos en formato comprimido si existen (se recomienda no modificar)
	- `["nombre_imagen"]_grafo.txt` : contiene el grafo (nodos y aristas) generado en base a los segmentos y puntos incluidos.

Por otra parte, si se han incluido nuevas etiquetas, estas quedarán automáticamente actualizadas al finalizar el programa, quedando estas recopiladas en `etiquetas.txt`