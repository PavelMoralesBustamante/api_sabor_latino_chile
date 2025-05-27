from flask import Flask, jsonify

app = Flask(__name__)

# Datos de clientes
clientes = [
    {"numero_rut":"11111111","dv_rut":"1","primer_nombre":"Juan","segundo_nombre":"Carlos","apellido_paterno":"Pérez","apellido_materno":"González","direccion":"Calle 1 #101","telefono":"+56911110001"},
    {"numero_rut":"11111112","dv_rut":"2","primer_nombre":"María","segundo_nombre":"José","apellido_paterno":"López","apellido_materno":"Ramírez","direccion":"Calle 2 #102","telefono":"+56911110002"},
    {"numero_rut":"11111113","dv_rut":"3","primer_nombre":"Pedro","segundo_nombre":"Antonio","apellido_paterno":"Riquelme","apellido_materno":"Salinas","direccion":"Calle 3 #103","telefono":"+56911110003"},
    {"numero_rut":"11111114","dv_rut":"4","primer_nombre":"Camila","segundo_nombre":"Andrea","apellido_paterno":"Muñoz","apellido_materno":"Vega","direccion":"Calle 4 #104","telefono":"+56911110004"},
    {"numero_rut":"11111115","dv_rut":"5","primer_nombre":"Francisco","segundo_nombre":"Ignacio","apellido_paterno":"Castro","apellido_materno":"Ortega","direccion":"Calle 5 #105","telefono":"+56911110005"},
    {"numero_rut":"11111116","dv_rut":"6","primer_nombre":"Valentina","segundo_nombre":"Isabel","apellido_paterno":"Reyes","apellido_materno":"Silva","direccion":"Calle 6 #106","telefono":"+56911110006"},
    {"numero_rut":"11111117","dv_rut":"7","primer_nombre":"Diego","segundo_nombre":"Alonso","apellido_paterno":"Fernández","apellido_materno":"Carrasco","direccion":"Calle 7 #107","telefono":"+56911110007"},
    {"numero_rut":"11111118","dv_rut":"8","primer_nombre":"Fernanda","segundo_nombre":"Belén","apellido_paterno":"Morales","apellido_materno":"Herrera","direccion":"Calle 8 #108","telefono":"+56911110008"},
    {"numero_rut":"11111119","dv_rut":"9","primer_nombre":"Javier","segundo_nombre":"Esteban","apellido_paterno":"Gutiérrez","apellido_materno":"Campos","direccion":"Calle 9 #109","telefono":"+56911110009"},
    {"numero_rut":"11111120","dv_rut":"K","primer_nombre":"Daniela","segundo_nombre":"Alejandra","apellido_paterno":"Araya","apellido_materno":"Navarro","direccion":"Calle 10 #110","telefono":"+56911110010"},
    {"numero_rut":"11111121","dv_rut":"1","primer_nombre":"Cristian","segundo_nombre":"Eduardo","apellido_paterno":"Vargas","apellido_materno":"Olivares","direccion":"Calle 11 #111","telefono":"+56911110011"},
    {"numero_rut":"11111122","dv_rut":"2","primer_nombre":"Karla","segundo_nombre":"Beatriz","apellido_paterno":"Soto","apellido_materno":"Martínez","direccion":"Calle 12 #112","telefono":"+56911110012"},
    {"numero_rut":"11111123","dv_rut":"3","primer_nombre":"Nicolás","segundo_nombre":"Matías","apellido_paterno":"Bravo","apellido_materno":"Fuentes","direccion":"Calle 13 #113","telefono":"+56911110013"},
    {"numero_rut":"11111124","dv_rut":"4","primer_nombre":"Catalina","segundo_nombre":"Florencia","apellido_paterno":"Gallardo","apellido_materno":"Maldonado","direccion":"Calle 14 #114","telefono":"+56911110014"},
    {"numero_rut":"11111125","dv_rut":"5","primer_nombre":"Andrés","segundo_nombre":"Mauricio","apellido_paterno":"Pizarro","apellido_materno":"Toledo","direccion":"Calle 15 #115","telefono":"+56911110015"},
    {"numero_rut":"11111126","dv_rut":"6","primer_nombre":"Ignacia","segundo_nombre":"Javiera","apellido_paterno":"Fuenzalida","apellido_materno":"Zamora","direccion":"Calle 16 #116","telefono":"+56911110016"},
    {"numero_rut":"11111127","dv_rut":"7","primer_nombre":"Sebastián","segundo_nombre":"Rodrigo","apellido_paterno":"Espinoza","apellido_materno":"Cabrera","direccion":"Calle 17 #117","telefono":"+56911110017"},
    {"numero_rut":"11111128","dv_rut":"8","primer_nombre":"Paula","segundo_nombre":"Josefina","apellido_paterno":"Mora","apellido_materno":"Aguilera","direccion":"Calle 18 #118","telefono":"+56911110018"},
    {"numero_rut":"11111129","dv_rut":"9","primer_nombre":"Rodrigo","segundo_nombre":"Felipe","apellido_paterno":"Alarcón","apellido_materno":"Sanhueza","direccion":"Calle 19 #119","telefono":"+56911110019"},
    {"numero_rut":"11111130","dv_rut":"K","primer_nombre":"Javiera","segundo_nombre":"Antonella","apellido_paterno":"Leiva","apellido_materno":"Cifuentes","direccion":"Calle 20 #120","telefono":"+56911110020"},
    {"numero_rut":"11111131","dv_rut":"1","primer_nombre":"Felipe","segundo_nombre":"Andrés","apellido_paterno":"Navarrete","apellido_materno":"Orellana","direccion":"Calle 21 #121","telefono":"+56911110021"},
    {"numero_rut":"11111132","dv_rut":"2","primer_nombre":"Constanza","segundo_nombre":"Valeria","apellido_paterno":"Bustamante","apellido_materno":"Muñoz","direccion":"Calle 22 #122","telefono":"+56911110022"},
    {"numero_rut":"11111133","dv_rut":"3","primer_nombre":"Tomás","segundo_nombre":"Rafael","apellido_paterno":"Zúñiga","apellido_materno":"Saavedra","direccion":"Calle 23 #123","telefono":"+56911110023"},
    {"numero_rut":"11111134","dv_rut":"4","primer_nombre":"Antonia","segundo_nombre":"Fernanda","apellido_paterno":"Salazar","apellido_materno":"Baeza","direccion":"Calle 24 #124","telefono":"+56911110024"},
    {"numero_rut":"11111135","dv_rut":"5","primer_nombre":"Benjamín","segundo_nombre":"Iván","apellido_paterno":"Ramírez","apellido_materno":"Donoso","direccion":"Calle 25 #125","telefono":"+56911110025"},
    {"numero_rut":"11111136","dv_rut":"6","primer_nombre":"Isidora","segundo_nombre":"Mariana","apellido_paterno":"Rojas","apellido_materno":"Alvear","direccion":"Calle 26 #126","telefono":"+56911110026"},
    {"numero_rut":"11111137","dv_rut":"7","primer_nombre":"Lucas","segundo_nombre":"Cristóbal","apellido_paterno":"Cortés","apellido_materno":"Henríquez","direccion":"Calle 27 #127","telefono":"+56911110027"},
    {"numero_rut":"11111138","dv_rut":"8","primer_nombre":"Daniela","segundo_nombre":"Sofía","apellido_paterno":"Yáñez","apellido_materno":"Caro","direccion":"Calle 28 #128","telefono":"+56911110028"},
    {"numero_rut":"11111139","dv_rut":"9","primer_nombre":"Martín","segundo_nombre":"Leandro","apellido_paterno":"Tapia","apellido_materno":"Astudillo","direccion":"Calle 29 #129","telefono":"+56911110029"},
    {"numero_rut":"11111140","dv_rut":"K","primer_nombre":"Renata","segundo_nombre":"Victoria","apellido_paterno":"Vergara","apellido_materno":"Meza","direccion":"Calle 30 #130","telefono":"+56911110030"},
    {"numero_rut":"11111141","dv_rut":"1","primer_nombre":"Gabriel","segundo_nombre":"José","apellido_paterno":"Acevedo","apellido_materno":"Escobar","direccion":"Calle 31 #131","telefono":"+56911110031"},
    {"numero_rut":"11111142","dv_rut":"2","primer_nombre":"Trinidad","segundo_nombre":"Daniela","apellido_paterno":"Pino","apellido_materno":"Carrera","direccion":"Calle 32 #132","telefono":"+56911110032"},
    {"numero_rut":"11111143","dv_rut":"3","primer_nombre":"Alejandro","segundo_nombre":"Enrique","apellido_paterno":"Molina","apellido_materno":"Godoy","direccion":"Calle 33 #133","telefono":"+56911110033"},
    {"numero_rut":"11111144","dv_rut":"4","primer_nombre":"Josefa","segundo_nombre":"María","apellido_paterno":"Sánchez","apellido_materno":"Escobar","direccion":"Calle 34 #134","telefono":"+56911110034"},
    {"numero_rut":"11111145","dv_rut":"5","primer_nombre":"Maximiliano","segundo_nombre":"Samuel","apellido_paterno":"Barría","apellido_materno":"Ovalle","direccion":"Calle 35 #135","telefono":"+56911110035"},
    {"numero_rut":"11111146","dv_rut":"6","primer_nombre":"Agustina","segundo_nombre":"Elena","apellido_paterno":"Delgado","apellido_materno":"Villagra","direccion":"Calle 36 #136","telefono":"+56911110036"},
    {"numero_rut":"11111147","dv_rut":"7","primer_nombre":"Vicente","segundo_nombre":"David","apellido_paterno":"Ulloa","apellido_materno":"Salinas","direccion":"Calle 37 #137","telefono":"+56911110037"},
    {"numero_rut":"11111148","dv_rut":"8","primer_nombre":"Emilia","segundo_nombre":"Luna","apellido_paterno":"Farías","apellido_materno":"Toro","direccion":"Calle 38 #138","telefono":"+56911110038"},
    {"numero_rut":"11111149","dv_rut":"9","primer_nombre":"Mateo","segundo_nombre":"Julio","apellido_paterno":"Peña","apellido_materno":"Medina","direccion":"Calle 39 #139","telefono":"+56911110039"},
    {"numero_rut":"11111150","dv_rut":"K","primer_nombre":"Amanda","segundo_nombre":"Lucía","apellido_paterno":"Vilches","apellido_materno":"Bravo","direccion":"Calle 40 #140","telefono":"+56911110040"}
]

@app.route("/")
def home():
    return "API de Clientes - Sabor Latino Chile"

@app.route("/clientes", methods=["GET"])
def get_clientes():
    return jsonify(clientes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
