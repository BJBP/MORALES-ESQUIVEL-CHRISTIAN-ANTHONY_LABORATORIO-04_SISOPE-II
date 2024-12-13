# Sprint 1

## Objetivos

*   [ ] Implementar la persistencia de datos.
*   [ ] Configurar la base de datos SQLite.
*   [ ] Almacenar los mensajes en la base de datos.
*   [ ] Recuperar el historial de mensajes al iniciar la aplicación.

# Sistema de Chat Distribuido

## Descripción del Proyecto

Este proyecto busca desarrollar una simulación de un chat grupal, implementando características clave de un sistema distribuido. La versión actual del proyecto, basada en un trabajo de laboratorio de la semana 4 del curso de Sistemas Operativos 2, permite la comunicación básica entre clientes y un servidor. El objetivo final es expandir esta base para simular un sistema de chat robusto con las siguientes funcionalidades esenciales:

### Funcionalidades Actuales:

*   [ ] Comunicación cliente-servidor básica mediante sockets.
*   [ ] Implementación de un chat grupal rudimentario.

### Objetivos Principales:

*   [ ] **Persistencia de Datos:** Almacenar y recuperar el historial de conversaciones, de manera que los usuarios puedan acceder a los mensajes previos incluso si cierran y vuelven a abrir la aplicación.
*   [ ] **Tolerancia a Fallos:** Simular la capacidad del sistema para manejar la falla de uno o más servidores, asegurando la continuidad del servicio mediante el respaldo de servidores adicionales.

## Justificación

El proyecto surge de la necesidad de aplicar los conceptos de sistemas distribuidos en un escenario práctico y familiar, como lo es un chat grupal. El objetivo es ir más allá de la comunicación básica cliente-servidor, incorporando aspectos críticos como la persistencia de datos y la tolerancia a fallos, que son fundamentales en sistemas distribuidos del mundo real (como WhatsApp).

## Implementación

### Persistencia de Datos:

*   [ ] Se implementará un mecanismo para almacenar la información de los chats en una base de datos o un sistema de almacenamiento persistente.
*   [ ] Al unirse a un chat o volver a abrir la ventana, los usuarios podrán recuperar el historial de mensajes de manera transparente.

### Tolerancia a Fallos:

*   [ ] Se simulará la presencia de múltiples servidores.
*   [ ] El sistema podrá identificar y adaptarse a la falla de un servidor, redirigiendo la comunicación a un servidor de respaldo.

### Tecnologías

(Aquí irán las tecnologías específicas que utilicen, por ejemplo:)

*   [ ] **Lenguaje:** Python (o el lenguaje que utilices).
*   [ ] **Sockets:** Para la comunicación en red.
*   [ ] **Base de Datos:** (Ej: SQLite, MongoDB).
*   [ ] **Sistema de Gestión de Mensajes:** (Si hay alguno).

## Estado Actual

Actualmente, el proyecto cuenta con la funcionalidad de comunicación cliente-servidor implementada durante la semana 4 de curso. La presente fase se centrará en añadir las funcionalidades de persistencia de datos y tolerancia a fallos.

## Contribuciones

(Aquí pueden poner una sección si esperan contribuciones o cómo sería)

## Licencia
[ ] (Aquí pueden poner la licencia del proyecto)

## Próximos Pasos

*   [ ] Investigación y selección de herramientas para la persistencia de datos.
*   [ ] Implementación de la persistencia de datos.
*   [ ] Diseño y desarrollo del sistema de tolerancia a fallos.
*   [ ] Pruebas exhaustivas.
*   [ ] Refactorización del código.

# Proyecto de Chat

Este proyecto implementa un sistema de chat simple utilizando Python.

Los archivos principales son:

*   [ ] `chat_client.py`: Implementa el cliente de chat.
*   [ ] `chat_server.py`: Implementa el servidor de chat.
*   [ ] `main.py`: El punto de entrada principal del proyecto.

El directorio `0.Informe` contiene documentación adicional sobre el proyecto.

## Instrucciones de Ejecución

1.  [ ] Ejecutar el archivo `main.py`.
2.  [ ] Ingresar el número de clientes que se usarán para la simulación del chat grupal.
3.  [ ] Opcional: Ingresar los nombres ficticios de los clientes o miembros del chat separados por comas.
4.  [ ] Mandar mensajes entre las ventanas de los diferentes clientes.
