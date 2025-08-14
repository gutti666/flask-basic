# Mi primera aplicación web con Flask
from flask import Flask, render_template_string
import datetime
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title> Mi Primera App Docker</title>
        <style>
            body { font-family: Arial; margin: 40px; background-color: #f0f0f0; }
            .container { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            .info { background: #e7f3ff; padding: 15px; border-radius: 5px; margin: 10px 0; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1> ¡Hola desde Docker!</h1>
            <p>Esta es mi primera aplicación web ejecutándose en un contenedor.</p>
            
            <div class="info">
                <h3> Información del contenedor:</h3>
                <ul>
                    <li><strong>Hora actual:</strong> {{ tiempo }}</li>
                    <li><strong>Hostname:</strong> {{ hostname }}</li>
                    <li><strong>Estado:</strong>  Funcionando correctamente</li>
                </ul>
            </div>
            
            <p> <strong>¡Tu aplicación Docker está funcionando!</strong></p>
        </div>
    </body>
    </html>
    ''', tiempo=datetime.datetime.now(), hostname=socket.gethostname())

@app.route('/api')
def api():
    return {
        "mensaje": "¡API funcionando!",
        "tiempo": datetime.datetime.now().isoformat(),
        "container": socket.gethostname(),
        "status": "success"
    }

if __name__ == '__main__':
    print(" Iniciando aplicación Docker...")
    print(" Aplicación disponible en: http://localhost:5000")
    print("Cambio pull reuqes")
    app.run(host='0.0.0.0', port=5000, debug=True)
