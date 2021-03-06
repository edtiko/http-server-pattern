# http-server-pattern

# Autores
* Edwin Gómez
* Wilmer Renteria


# Objetivo
Construir servidor HTTP desde cero teniendo en cuenta los lineamientos del protocolo HTTP /1.1 especificado en el RFC, y entender el comportamiento interno de este. tomando desiciones de diseño y teniendo un código legible que pueda ser leido facilmente.

# Requisitos
* Implementar la atención de peticiones http. 
* Realizar traza de todas las peticiones que se le realicen aL servidor escribiendo cada petición recibida en un archivo de log.
* Implementar proyecto de pruebas, donde estén definidos los comportamientos esperados.

# Implementación:
La metodología usada para el desarrollo del servidor HTTP es BDD (Behavior Driven Development), donde primero se establecieron los comportamientos esperados de la aplicación, para posteriormente desarrollar cada escenario esperado.
Al ser python un lenguaje intituitivo la curva de aprendizaje no fue tan complejo, sin embargo se presentaron errores que requirieron investigación para solucionarlos.
Las unicas librerias usadas para la implementación fueron socket, mimetypes, logging

![alt text](https://qanalysisblog.files.wordpress.com/2018/06/bdd_pic1.png?w=775)

// Primera Revisión
* Se implemento inicialmente un servidor TCP que atendiera conexiones full duplex con sockets entre el userAgent y el server.

// Segunda Revisión
* Posterior se desarrolla el parseador de los datos recibidos en el socket
* Posterior se implementan 2 metodos HTTP (GET, OPTIONS, POST, PUT, DELETE, PATCH)
* Manejo de errores cuando llegue un metodo no implementado
* Manejo de la traza de cada petición realizada en un archivo llamado http_request.log que se encuentra dentro del proyecto


# Diagrama de Clases

![alt text](https://github.com/edtiko/http-server-pattern/blob/master/class-diagram-final.png)


# Herramientas
* El lenguaje usado para la implementación fue Python 3 y para el proyecto de pruebas Java.
* Visual Studio Code para realizar la implementación en Python.
* Eclipse para realizar el proyecto de pruebas usando Cucumber como dependencia.
* Git para el control de versiones de los dos proyectos.
* Junit para pruebas unitarias
* Cucumber para pruebas de integración y comportamiento
* RestAssured para pruebas del servicio HTTPServer
* StarUML para realizar el diagrama de clases

# Instrucciones de uso:

1. Instalar Python 3: https://www.python.org/downloads/
2. Instalar JDK Java: https://www.oracle.com/technetwork/es/java/javase/downloads/index.html
3. Instalar IDE Visual Studio Code
4. Instalar Eclipse o Intellij
5. Instalar Git
6. Clonar repositorio: https://github.com/edtiko/http-server-pattern.git
7. Abrir consola e ir a la raíz del proyecto /http-server:

 ![alt text](https://github.com/edtiko/http-server-pattern/blob/master/capture-project.PNG)
 
8. Ejecutar comando para iniciar el servidor: py main.py
9. En la consola debe aparecer "Listening at ('127.0.0.1', 8888)"
10. Abrir navegador o Postman para poder realizar peticiones como:
 - HTTP/1.1 GET http://127.0.0.0:8888/index.html
 - HTTP/1.1 OPTIONS http://127.0.0.0:8888
 - las peticiones quedan registradas en un archivo de log http_request.log
 
11. Para ejecutar el proyecto de pruebas es necesario realizar lo siguiente:
 - En el mismo repositorio se encuentra el proyecto /http-server-test
 - Importar como proyecto Maven en Eclipse
 - Ejecutar clase CucumberTest.java
 - Ver resultado de los pasos definidos cómo escenarios 
 - Ejecutar HttpServerTest.java con Junit para validar respuesta del servicio (httpServer)

# Pruebas:
Se implementó un proyecto de pruebas en Java con Cucumber para cubrir los comportamientos esperados del servidor HTTP desarrollado, los escenarios planteados son:
  
//Escenario 1
* Dado el nombre de un recurso index.html 
* Cuando el userAgent realice una petición GET al servidor http 
* Entonces el servidor debe responder código 200
* y con el body de index.html

//Escenario 2
* Dado el nombre de un recurso desconocido 
* Cuando el userAgent realice una petición GET al servidor http 
* Entonces el servidor debe responder código 404
* y con el body de error

//Escenario 3
* Dado el nombre de un recurso index.html 
* Cuando el userAgent realice una petición POST al servidor http 
* Entonces el servidor debe responder código 501
* y con el body de error

# Decisiones de realización

| Definición | Contexto |
| ------ | ------ |
| Restricciones | Solo están implementados los metodos GET y OPTIONS |
| Pruebas | Cucumber, JUnit, RestAssured |
| Librerias usadas implementación | sockets, logging, mimetypes, os |
| Lenguajes de programación     | Python, Java  |
| Arquitectura  | Cliente - Servidor (Stateless) |
| Metodología   | BDD |

# Referencias
RFC HTTP/1.1,  https://tools.ietf.org/html/rfc7230

