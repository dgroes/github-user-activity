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