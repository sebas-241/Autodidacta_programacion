create database holamundo;
USE holamundo;
CREATE TABLE animales(
	id int,
    tipo varchar(255),
    estado varchar(255),
    PRIMARY KEY(id)
);
INSERT INTO animales (tipo, estado) VALUE ('Cerdo', 'Feliz');
ALTER TABLE animales MODIFY COLUMN id int auto_increment;

SHOW CREATE TABLE animales;
CREATE TABLE `animales` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(255) DEFAULT NULL,
  `estado` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO animales (tipo, estado) VALUE ('Cerdo', 'Feliz');
INSERT INTO animales (tipo, estado) VALUE ('Neko', 'Hambriento');
INSERT INTO animales (tipo, estado) VALUE ('Inu', 'Repleto');
INSERT INTO animales (tipo, estado) VALUE ('Tori', 'Repleto');

SELECT * FROM animales;
SELECT * FROM animales WHERE id = 4;
SELECT * FROM animales WHERE estado = 'Hambriento';
SELECT * FROM animales WHERE estado = 'Repleto' AND tipo = 'Tori';

UPDATE animales SET estado = 'Triste' where id = 10;
SELECT * FROM animales;

DELETE from animales where id = 3;
SELECT * FROM animales;
-- Error 1175 es que debemos decir el id para eliminar o actualizar algun registro y no la embarremos