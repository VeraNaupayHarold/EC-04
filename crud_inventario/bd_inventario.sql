CREATE DATABASE IF NOT EXISTS bd_inventario;
USE bd_inventario;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL,
    clave VARCHAR(100) NOT NULL
);

INSERT INTO usuarios (usuario, clave) VALUES ('admin', 'admin123');

CREATE TABLE inventario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    cantidad INT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL
);