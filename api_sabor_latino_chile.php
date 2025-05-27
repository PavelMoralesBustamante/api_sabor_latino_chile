<?php
// Configurar cabeceras para permitir acceso desde cualquier origen (CORS)
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");


$jsonClientes = '[
  {"numero_rut":"11111111","dv_rut":"1","primer_nombre":"Juan","segundo_nombre":"Carlos","apellido_paterno":"Pérez","apellido_materno":"González","direccion":"Calle 1 #101","telefono":"+56911110001"},
  {"numero_rut":"11111112","dv_rut":"2","primer_nombre":"María","segundo_nombre":"José","apellido_paterno":"López","apellido_materno":"Ramírez","direccion":"Calle 2 #102","telefono":"+56911110002"},
  {"numero_rut":"11111113","dv_rut":"3","primer_nombre":"Pedro","segundo_nombre":"Antonio","apellido_paterno":"Riquelme","apellido_materno":"Salinas","direccion":"Calle 3 #103","telefono":"+56911110003"},
  {"numero_rut":"11111114","dv_rut":"4","primer_nombre":"Camila","segundo_nombre":"Andrea","apellido_paterno":"Muñoz","apellido_materno":"Vega","direccion":"Calle 4 #104","telefono":"+56911110004"},
  {"numero_rut":"11111115","dv_rut":"5","primer_nombre":"Francisco","segundo_nombre":"Ignacio","apellido_paterno":"Castro","apellido_materno":"Ortega","direccion":"Calle 5 #105","telefono":"+56911110005"},
  {"numero_rut":"11111116","dv_rut":"6","primer_nombre":"Valentina","segundo_nombre":"Isabel","apellido_paterno":"Reyes","apellido_materno":"Silva","direccion":"Calle 6 #106","telefono":"+56911110006"},
  {"numero_rut":"11111117","dv_rut":"7","primer_nombre":"Diego","segundo_nombre":"Alonso","apellido_paterno":"Fernández","apellido_materno":"Carrasco","direccion":"Calle 7 #107","telefono":"+56911110007"},
  {"numero_rut":"11111118","dv_rut":"8","primer_nombre":"Fernanda","segundo_nombre":"Belén","apellido_paterno":"Morales","apellido_materno":"Herrera","direccion":"Calle 8 #108","telefono":"+56911110008"},
  {"numero_rut":"11111119","dv_rut":"9","primer_nombre":"Javier","segundo_nombre":"Esteban","apellido_paterno":"Gutiérrez","apellido_materno":"Campos","direccion":"Calle 9 #109","telefono":"+56911110009"},
  {"numero_rut":"11111120","dv_rut":"K","primer_nombre":"Daniela","segundo_nombre":"Alejandra","apellido_paterno":"Araya","apellido_materno":"Navarro","direccion":"Calle 10 #110","telefono":"+56911110010"}
]';

$clientes = json_decode($jsonClientes, true);

// Devuelve el JSON
echo json_encode($clientes, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
?>
