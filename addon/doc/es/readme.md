# Complemento de LAMBDA para NVDA #

* Autor: Alberto Zanella y el equipo de lambda-nvda.
* Descargar [versión estable][1]
* Descargar [versión en desarrollo][2]

Este proyecto es un módulo de aplicación para el software Lambda. Ha sido inspirado por el trabajo de Peter Lecky en la Comenius University.
LAMBDA (Linear Access to Mathematic for Braille Device and Audio-synthesis, acceso lineal a las matemáticas mediante pantallas braille y síntesis de audio) es un programa que ayuda a las personas ciegas a leer y escribir matemáticas usando una pantalla braille y/o un sintetizador de audio.
LAMBDA es el resultado de un proyecto EU. Para más información acerca de LAMBDA por favor visite [http://www.lambdaproject.org/](http://www.lambdaproject.org/).  
La versión actual de este complemento tiene tablas braille solo para los
idiomas italiano y español pero su interfaz está disponible en la mayoría de
idiomas oficiales de NVDA, porque el complemento es traducido por la
comunidad de traductores de NVDA.
Si es usted un usuario no italiano de LAMBDA y le gustaría contribuír con
traducciones en su idioma, siéntase libre de contactar al autor (consulte
más abajo) o subscribirse a la lista de correo del proyecto.

**Nota:** Este complemento ha sido desarrollado por Alberto Zanella como una actividad voluntaria. Ni el autor ni los contribuyentes están relacionados con la venta o el desarrollo del programa LAMBDA. si quisiera obtener más información sobre LAMBDA, reportar problemas u obtener soporte, por favor contacte con su distribuidor local (en España, ONCE-CIDAT). Si está encontrando dificultades usando o instalando este complemento, por favor contacte con el autor o use el enlace "Issues" (errores) disponible en la página del proyecto en Github.

### [Repositorio Oficial en GitHub](https://github.com/lambda-nvda/lambdaNvda/)

## Características del complemento

### Soporte para habla:

* Se informa de los menús y diálogos correctamente;
* Soporte para habla natural de las fórmulas matemáticas usando el motor
  interno de LAMBDA (p.ej. "raíz compuesta 3 de raíz compuesta 3 x más 24,
  fin de raíz, menos 3 igual 0");
* Lectura por carácter, palabra, línea y Verbalizar Todo implementada.
* Habla cuando un bloque de texto está seleccionado o es extendido  (usando
  CTRL+B y SHIFT+CTRL+B);
* Habla al moverse por el texto con comandos de Windows y con comandos
  específicos de Lambda;
* Tanto el modo de habla corto como el extendido están soportados (puede
  establecerlo usando el menú Herramientas de LAMBDA);
* Ventanas de diálogos especiales como la del modo estructura, la
  calculadora, y la de matriz son ahora correctamente reportadas y NVDA lee
  correctamente al mover el cursor por ellas o al introducir texto;
* El eco de escritura utiliza el procesador de texto de Lambda, de forma que
  se informará correctamente de símbolos y marcadores.

### Soporte para Braille:

* El complemento instala (dentro del directorio de perfil de usuario) y
  activa un perfil de NVDA con una tabla braille. Esta tabla puede diferir
  en distintos idiomas. La tabla ha sido construida desde la presente en los
  scripts de Jaws para LAMBDA (archivo jbt). Entonces los símbolos y
  marcadores son representados mediante los mismos patrones de puntos;
* El complemento crea un perfil de configuración y establece la
  configuración de braille estándar. De forma que la salida a la tabla
  braille personalizada solo está establecida cuando LAMBDA está activo;
* Los diálogos y menús son correctamente braillificados;
* El contenido del editor es correctamente adaptado para braille y el
  usuario puede moverse usando las teclas de desplazamiento braille y de
  ruta del cursor;
* Empezando desde la versión del complemento 1.1.0 existen dos formas en las
  cuales el contenido es representado: "Modo plano" y "Modo no
  plano". Cuando el "Modo plano" está activado, NVDA usará el Modelo de
  Mostrado para obtener el contenido desde Lambda y para determinar la
  posición del cursor braille. Esto es especialmente beneficioso cuando el
  usuario necesita moverse por la pantalla, incluso por los espacios en
  blanco del editor. Cuando el "Modo plano" está establecido a
  "Desactivado", la representación del texto en la pantalla braille es más
  estable, ya que NVDA usa Windows API para obtenerla. De modo que, cuando
  el usuario se mueve entre espacios en blanco el cursor en la pantalla
  braille no seguirá al cursor real hasta que un espacio no en blanco sea
  insertado por el usuario. 

El "Modo plano" está activo por defecto. Puede alternar el "Modo plano"
entre activado y desactivado pulsando NVDA+SHIFT+F.

Se recomienda vivamente deshabilitar el "Modo plano" cuando se use DPI
personalizado en Windows (opción de Tamaño personalizado), especialmente
cuando se tiene una configuración de pantalla de más de 96 DPI (más largo
que 100%).

* La estructura de los cuadros de diálogo es más sencilla, eliminando
  información repetida;
* La selección es marcada correctamente usando los puntos 7 y 8, y
  correctamente refrescada al presionar comandos estándar de Windows
  (SHIFT+FLECHAS) o comandos específicos de Lambda (CTRL+B, CTRL+SHIFT+B).

## Antes de empezar a usar este complemento.

Este complemento crea un perfil de NVDA nombrado como "lambda" que está
asociado con la aplicación lambda.exe. Este perfil está configurado con
todas las opciones en lo que a las opciones braille, a la tabla braille
personalizada, a la localización del foco y a las opciones del modo plano se
refiere.

Si un perfil previamente existente con el mismo nombre está presente en su
sistema, no será sobreescrito y deberá ajustar manualmente el perfil de
configuración.

Para salir de esta situación, si tiene configuraciones espcíficas que le
gustaría preservar, puede usar el "Asistente de Reversión del perfil
LAMBDA". La tecla rápida para abrir esta herramienta es NVDA+alt+r (cuando
se está dentro de LAMBDA).

Una opción fácil es también borrar viejas versiones del perfil "lambda"
después de la instalación del complemento. Para hacer esto, abra el menú de
NVDA, seleccione el elemento de menú "Perfiles de configuración" y pulse
ENTER.

En el diálogo de Perfiles de configuración, podrá localizar y borrar el
perfil "lambda". El perfil será creado nuevamente la próxima vez que se
inicie Lambda.

Eliminar el perfil "lambda" debería de ser una solución fácil también cuando
encuentre algún fallo que "aparezca" en algún punto mientras se use el
complemento. Por ejemplo, si la tabla braille no está correctamente
establecida, en lugar de configurar manualmente el perfil puede simplemente
borrarlo. El complemento creará uno nuevo la próxima vez que abra el editor
Lambda.

Cada vez que el editor Lambda es arrancado, el complemento verifica si
existe un perfil con el nombre "lambda". Si no existe crea automáticamente
un perfil con la siguiente forma:

``` filename : userData\profiles\lambda.ini :

[braille]
	readByParagraph = False
	tetherTo = focus
	translationTable = path-to-the-addon-brailleTable-dir\tableName

[lambda]
	brailleFlatMode = True

```

Donde :

* path-to-the-addon-brailleTable-dir : Es la ruta absoluta del directorio
  del complemento + "\brailleTables"
* tableName : Depende del idioma seleccionado. Actualmente las tablas
  braille italiana y española, "lambda-ita.utb" y "lambda-esp.utb"
  respectivamente, están presentes.

## Teclas Rápidas del Complemento:

* **NVDA+Shift+f**: Alterna el modo plano de braille entre activado y
  desactivado;
* **NVDA+alt+r**: Abre el "Asistente de Reversión del Perfil LAMBDA";
* **NVDA+d**: Duplicar líneas, use esto en lugar de CTRL+d.

## Errores conocidos:

Debido a un error presente en LAMBDA; el complemento proporciona una lógica
adicional que informa de los espacio en blanco. Esta lógica puede fallar en
las siguientes situaciones:

* Cuando palabras como "space", "spazio", "espacio", etc. son insertadas en
  el texto, éstas pueden ser reportadas en el idioma del NVDA del usuario.
* El motor de habla de LAMBDA no informa de líneas en blanco. el usuario
  escuchará la traducción de la palabra "espacio" en su lugar. Esto puede
  ser tanto una línea en blanco como una línea conteniendo solamente la
  palabra "espacio".

## Consejos útiles

Este es un conjunto de consejos que le ayudará a usar este complemento de
una manera más eficiente:

* Lectura caracter por caracter: normalmente, cuando está escribiendo
  matemáticas le gusta que NVDA diga aquello que está escribiendo caracter
  por caracter. Para hacer esto, hay unos cuantos simples pasos: asegúrese
  de tener focalizada la ventana de LAMBDA o una de sus variantes (la
  representación en seis puntos, por ejemplo); presione NVDA+2 (número dos)
  o navegue a menú NVDA>Preferencias>Opciones de teclado y marque la casilla
  para reportar caracteres al escribir; diríjase a
  LAMBDA>Herramientas>Parámetros de voz y asegúrese de que la casilla "Eco"
  está marcada, de otro modo NVDA no recibirá nada del motor de voz mientras
  usted escribe. Y hecho, NVDA leerá los caracteres escritos, pero no se
  preocupe, solo en LAMBDA, los ajustes de otras aplicaciones serán dejados
  como estaban.

## Lista de correo del complemento:

Para reportar errores, sugerencias o si quiere contribuir puede subscribirse
al grupo del complemento (en inglés). Puede subscribirse desde el sitio web:
<https://groups.io/g/lambda-nvda>.

## Registro de cambios

Abajo se encuentra una lista de cambios entre las diferentes versiones del
complemento. Al lado del numero de versión, entre paréntesis, está el estado
de desarrollo. La versión actualmente en desarrollo no se incluye ya que
podría haber cambios hasta que sea marcada como estable o descartada como
candidata.

### Versión 1.2.1 (estable)

* Añadida compatibilidad con la manera que NVDA 2017.3 usa para administrar
  el Braille. Compatibilidad con versiones antiguas mantenida.
* Arregladas varias incidencias relacionadas con el braille.

### Versión 1.2.0 (desarrollo)

Esta versión no fue publicada como estable porque la 1.2.1 incluía arreglos
importantes.

* Nuevos idiomas. Traducciones actualizadas.

### Versión 1.1.8 (estable)

* Primera versión estable.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=lambda

[2]: http://addons.nvda-project.org/files/get.php?file=lambda-dev
