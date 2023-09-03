from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Configura la conexión a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="calculadora_db"  # Cambia esto al nombre de tu base de datos
)

# Define una ruta para mostrar el formulario y guardar resultados
@app.route('/', methods=['GET', 'POST'])
def calculadora():
    if request.method == 'POST':
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        operacion = request.form['operacion']
        resultado = 0.0

        if operacion == 'sumar':
            resultado = numero1 + numero2
        elif operacion == 'multiplicar':
            resultado = numero1 * numero2
        elif operacion == 'restar':
            resultado = numero1 - numero2

        # Guardar el resultado en la base de datos
        # cursor = db.cursor()
        # cursor.execute("INSERT INTO resultados (operacion, resultado) VALUES (%s, %s)",
        #                (operacion, resultado))
        # db.commit()
        # cursor.close()

    # return render_template('calculadora.html')

# Inicia el servidor en el puerto 5000 por defecto
if __name__ == '__main__':
    app.run()
