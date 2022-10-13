create database usuarios;
use usuarios;
CREATE TABLE user(
	id int not null auto_increment,
    name varchar(50) not null,
    edad int not null,
    email varchar(100) not null,
    PRIMARY KEY(id)
);

INSERT INTO user (name, edad, email) values ('Sebastian', 17, 'sebgonrod@gmail.com');
INSERT INTO user (name, edad, email) values ('Juan', 20, 'holamundo@gmail.com');
INSERT INTO user (name, edad, email) values ('Sayaka', 16, 'sayaka2021@hotmail.com');
INSERT INTO user (name, edad, email) values ('Kotori', 14, 'kokoru@gmail.com.jp');

SELECT * FROM  user;
SELECT * FROM user LIMIT 1;
SELECT * FROM user WHERE edad > 15;
SELECT * FROM user WHERE edad >= 17;
SELECT * FROM user WHERE edad >= 17 AND email = 'sebgonrod@gmail.com';
SELECT * FROM user WHERE edad > 17 or email = 'kokoru@gmail.com';
SELECT * FROM user WHERE email != 'sebgonrod@gmail.com';
SELECT * FROM user WHERE edad BETWEEN 14 and 16;
SELECT * FROM user WHERE email like '%hotmail%';
SELECT * FROM user WHERE email like '%.jp';    -- Que comience con cualquier cosa y ermine exclusivamente con lo que se pone.

SELECT * FROM user ORDER by edad asc;
SELECT * FROM user ORDER by edad desc;

SELECT MAX(edad) as edad_maxima FROM user;
SELECT MIN(edad) as edad_minima FROM user;

SELECT id, name FROM user;
SELECT name as nombre FROM user;