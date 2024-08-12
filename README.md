<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Terminal Chat Application</h1>
    <p>
        Este proyecto implementa una sencilla aplicación de chat basada en terminal utilizando sockets en Python. 
        La aplicación permite que múltiples clientes se conecten a un servidor de chat, intercambiando mensajes en tiempo real.
    </p>
    
  <h2>Archivos Principales</h2>
    
  <h3><code>client.py</code></h3>
    <p>Este archivo contiene el código del cliente de chat. Algunas de las funcionalidades clave incluyen:</p>
    <ul>
        <li><strong>Conexión al servidor</strong>: El cliente se conecta al servidor en <code>127.0.0.1</code> en el puerto <code>9999</code>.</li>
        <li><strong>Recepción de mensajes</strong>: Los mensajes enviados por otros usuarios son recibidos y mostrados en la terminal del cliente.</li>
        <li><strong>Interfaz de usuario</strong>: Muestra un encabezado ASCII en la terminal al iniciar la conexión.</li>
    </ul>
    
  <h3><code>server.py</code></h3>
    <p>Este archivo contiene el código del servidor de chat. Algunas de las funcionalidades clave incluyen:</p>
    <ul>
        <li><strong>Manejo de múltiples clientes</strong>: El servidor puede aceptar conexiones de varios clientes a la vez y distribuir mensajes entre ellos.</li>
        <li><strong>Broadcasting de mensajes</strong>: Cuando un cliente envía un mensaje, el servidor lo retransmite a todos los demás clientes conectados.</li>
        <li><strong>Manejo de conexiones</strong>: El servidor gestiona el ciclo de vida de las conexiones, detectando cuándo un cliente se une o abandona el chat.</li>
    </ul>
    
  <h2>Uso</h2>
    <ol>
        <li><strong>Inicia el servidor</strong>: Ejecuta <code>server.py</code> en una terminal:
            <pre><code>python3 server.py</code></pre>
        </li>
        <li><strong>Inicia el cliente</strong>: Ejecuta <code>client.py</code> en otra terminal:
            <pre><code>python3 client.py</code></pre>
            Ingresa un nombre de usuario cuando se te solicite y comienza a chatear.
        </li>
    </ol>
    
  <h2>Ejemplo de Uso</h2>
    <div align="center">
        <pre style="background-color:#1e1e1e;color:#ffffff;padding:20px;border-radius:10px;font-family:monospace;">
            <span style="color:#00ff00;">Usuario1:</span> Hola, ¿cómo estás?
            <span style="color:#00ff00;">Usuario2:</span> ¡Todo bien! ¿Y tú?
            <span style="color:#00ff00;">Usuario1:</span> Excelente, trabajando en un proyecto de chat en la terminal.
            <span style="color:#00ff00;">Usuario2:</span> ¡Genial! Suena interesante.
        </pre>
    </div>
</body>
</html>
