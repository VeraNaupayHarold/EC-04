from flask import Flask, render_template, request, redirect, session, url_for
from conexion import obtener_conexion

app = Flask(__name__)
app.secret_key = 'secreto_seguro'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/acceder', methods=['POST'])
def acceder():
    usuario = request.form['usuario']
    clave = request.form['clave']

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE usuario = %s AND clave = %s", (usuario, clave))
    resultado = cursor.fetchone()
    conexion.close()

    if resultado:
        session['usuario'] = resultado['usuario']
        return redirect('/inventario')
    else:
        return render_template('login.html', error="Credenciales incorrectas")

@app.route('/inventario')
def inventario():
    if 'usuario' not in session:
        return redirect('/')
    
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM inventario")
    productos = cursor.fetchall()
    conexion.close()
    return render_template('inventario.html', productos=productos)

@app.route('/agregar', methods=['POST'])
def agregar_producto():
    producto = request.form['producto']
    cantidad = int(request.form['cantidad'])
    precio = float(request.form['precio'])

    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Inventario (producto, cantidad, precio) VALUES (%s, %s, %s)", (producto, cantidad, precio))
    conn.commit()
    conn.close()

    return redirect('/inventario')


@app.route('/actualizar', methods=['POST'])
def actualizar():
    id = request.form['id']
    nombre = request.form['producto']
    cantidad = request.form['cantidad']
    precio = request.form['precio']

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE inventario SET producto=%s, cantidad=%s, precio=%s WHERE id=%s", (nombre, cantidad, precio, id))
    conexion.commit()
    conexion.close()

    return redirect('/inventario')

@app.route('/eliminar/<int:id>')
def eliminar(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM inventario WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()

    return redirect('/inventario')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)