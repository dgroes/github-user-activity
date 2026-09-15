# C01: urllib
Mas info: [Documentación](https://docs.python.org/es/3/library/urllib.request.html)

El módulo **urllib.request** define funciones y clases que ayudan a abrir URL (principalmente HTTP) en un mundo complejo: autenticación básica y digest, redirecciones, cookies y más.
Permite enviar solicitudes web, descargar páginas, interactuar con **APIs** (usando **HTTP/HTTPS**) y gestionar tareas como redirecciones y autenticación básica sin instalar dependencias externas
Caracteristicas:
- **Uso nativo**: Al ser parte de Python, no requiere comandos adicionales como pip install para funcionar.
- **Funciones comunes**: Utiliza métodos como `urlopen()` para abrir conexiones y `Request` para personalizar los encabezados (**headers**) y el método HTTP (**GET, POST**).
- **Extensibilidad**: Permite añadir manejadores (**handlers**) y abridores (**openers**) para gestionar cookies, servidores proxy y otros protocolos personalizados.
# C02: GitHub API REST
La API de REST de GitHub es una interfaz que permite a los desarrolladores interactuar con GitHub mediante programación para automatizar flujos de trabajo, crear aplicaciones y gestionar recursos como repositorios, incidencias (issues), solicitudes de extracción (pull requests) y usuarios mediante solicitudes HTTP estándar.

**Características Principales**:
- **Formato de datos**: Intercambia información utilizando el formato estándar **JSON**, lo que facilita su lectura y análisis en casi cualquier lenguaje de programación
- **Autenticación**: Puedes realizar peticiones públicas sin iniciar sesión, pero para modificar datos o acceder a repositorios privados, requiere autenticación mediante tokens (como los Personal Access Tokens).
- **Diseño REST**: Sigue los principios arquitectónicos **REST**, utilizando métodos HTTP habituales como `GET` (para obtener datos), `POST` (para crear), `PUT/PATCH` (para actualizar) y `DELETE` (para eliminar)
# C03: Colores en terminal
Generador de estilos para la terminal: [ANSI Color Code Generator](https://ansi-generator.pages.dev/)<br>
Para que la terminal entienda que le vas a dar una orden de diseño (como cambiar a negrita o poner color rojo) y que no deseas imprimir el texto literalmente, necesitas iniciar la instrucción con este caracter invisible.
- `\033`: (**Octal**): Es la representación del caracter de escape en el sistema numérico octal (base 8). Es el método más tradicional, compatible y utilizado en los scripts de Python.
- `\x1b` (**Hexadecimal**): Es el mismo caracter de escape, pero escrito en el sistema numérico hexadecimal (base 16). La letra b equivale al número 11 en hexadecimal (27 en decimal). Es sumamente común en lenguajes como JavaScript o Node.js.
- `\e`: (**Atajo**): Es un alias o "atajo" directo para la palabra Escape. Es una forma más corta y legible de escribirlo, muy utilizada en scripts de Bash (la terminal de Linux) o comandos directos de consola. Nota: En Python estándar \e no funciona de forma nativa y te dará un error de sintaxis si lo pones dentro de un string.
## Formas de escribir colores
Los colores reales que admiten las terminales no dependen de la secuencia de escape anterior, sino de los números que pones después de ella. Existen tres formatos estándar de color:
- **Colores de 3 y 4 bits** (16 Colores básicos):
    - Es el sistema clásico que estamos usando en tus ejemplos (31 para rojo, 94 para azul brillante).
    - Funciona absolutamente en cualquier terminal.
- **Colores de 8 bits** (Tabla de 256 colores):
    - Utiliza una paleta fija indexada del 0 al 255.
    - Se escribe con la estructura: \033[38;5;NUMEROm. Por ejemplo, el 38;5;208m es un color naranja muy vivo.
- **Colores de 24 bits** (True Color - RGB real):
    - Permite usar más de 16 millones de colores exactos usando combinaciones numéricas de Rojo, Verde y Azul (de 0 a 255).
    - Se escribe con la estructura: \033[38;2;R;G;Bm. Es ideal si buscas tonos muy específicos o pasteles.