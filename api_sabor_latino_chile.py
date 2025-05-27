from flask import Flask, jsonify

app = Flask(__name__)

# Datos de clientes
clientes = [
    {"numero_rut": "11111111", "dv_rut": "1", "primer_nombre": "Juan", "segundo_nombre": "Carlos", "apellido_paterno": "Pérez", "apellido_materno": "González", "direccion": "Calle 1 #101", "telefono": "+56911110001"},
    {"numero_rut": "11111112", "dv_rut": "2", "primer_nombre": "María", "segundo_nombre": "José", "apellido_paterno": "López", "apellido_materno": "Ramírez", "direccion": "Calle 2 #102", "telefono": "+56911110002"},
    {"numero_rut": "11111113", "dv_rut": "3", "primer_nombre": "Pedro", "segundo_nombre": "Antonio", "apellido_paterno": "Riquelme", "apellido_materno": "Salinas", "direccion": "Calle 3 #103", "telefono": "+56911110003"},
    # ... (agrega los demás registros aquí, si quieres el JSON completo dime y lo pongo) ...
]

@app.route("/")
def home():
    return "API de Clientes - Sabor Latino Chile"

@app.route("/clientes", methods=["GET"])
def get_clientes():
    return jsonify(clientes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
