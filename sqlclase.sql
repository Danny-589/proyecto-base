create database rentacardas;
use rentacardas;

create table cliente (
id_cliente int auto_increment primary key,
ced_cliente varchar(15),
nom_cliente varchar(40),
ape_cliente varchar(40),
sex_cliente char(9),
dir_cliente varchar(40),
tel_cliente varchar(11),
cor_cliente varchar(40),
fec_nac_cliente date
);

INSERT INTO cliente(ced_cliente, nom_cliente, ape_cliente, 
sex_cliente, dir_cliente, tel_cliente, cor_cliente, fec_nac_cliente) VALUES
('1150276572', 'Daniel Sebastián', 'Reátegui Vélez', 'm', 'Une ETAPA I', 
'0983789226', 'danielreateguivelez@gmail.com', '2009-02-16');

INSERT INTO cliente(ced_cliente, nom_cliente, ape_cliente, 
sex_cliente, dir_cliente, tel_cliente, cor_cliente, fec_nac_cliente) VALUES
('1150276580', 'David Eduardo', 'Reátegui Vélez', 'm', 'OPERADORES',
'0998559694', 'dreategui@ladolorosa-loja.edu.ec', '2007-03-02');

create table if not exists auto(
id_auto int auto_increment primary key,
cod_auto varchar(10) not null,
mat_auto varchar(20) not null,
des_auto text,
mar_auto varchar(15),
tip_auto varchar (25),
mod_auto varchar (20),
col1_auto varchar (15),
col2_auto varchar (15),
numpas_auto int (2),
a_auto varchar(4),
comb_auto varchar(10)
);

INSERT INTO auto(cod_auto, mat_auto, des_auto, mar_auto, tip_auto, mod_auto, 
col1_auto, col2_auto, numpas_auto, a_auto, comb_auto) VALUES
('AUCH01', 'LBC7789', 'auto deportivo asientos forrados en cuero', 'CHEVROLET',
 'camioneta', 'Chevrolet rodeo V6', 'azul marino', 'azul rey', 5, '2020', 'gasolina');

INSERT INTO auto(cod_auto, mat_auto, des_auto, mar_auto, tip_auto, mod_auto, 
col1_auto, col2_auto, numpas_auto, a_auto, comb_auto) VALUES
('AUCH02', 'ABE2023', 'auto deportivo y 4 asientos y 1 asiento para bebe',
'CHEVROLET', 'camioneta', 'Chevrolet A. Sport',
'rojo', 'dorado', 5, '2023', 'gasolina');

INSERT INTO auto(cod_auto, mat_auto, des_auto, mar_auto, tip_auto, mod_auto, 
col1_auto, col2_auto, numpas_auto, a_auto, comb_auto) VALUES
('AUCH03', 'LCA2967', 'auto confortable para viaje',
'VOLKSWAGEN', 'auto', 'Virtus Comfortline',
'blanco', 'blanco', 5, '2024', 'gasolina');

INSERT INTO auto(cod_auto, mat_auto, des_auto, mar_auto, tip_auto, mod_auto, 
col1_auto, col2_auto, numpas_auto, a_auto, comb_auto) VALUES
('AUCH04', 'PJD5623', 'auto para pruebas de pista',
'VOLKSWAGEN', 'auto', 'Polo Sport',
'verde', 'verde', 2, '2001', 'gasolina');

select ced_cliente, nom_cliente, ape_cliente 
from cliente;

select mat_auto, mod_auto, a_auto 
from auto 
where mar_auto = 'CHEVROLET';



CREATE TABLE IF NOT EXISTS Reg_alquiler(
id_alquiler INT AUTO_INCREMENT PRIMARY KEY,
cod_alquiler VARCHAR (10) NOT NULL,
ced_cliente VARCHAR (20) NOT NULL,
cod_auto VARCHAR (10) NOT NULL,
fec_alquiler DATE,
obs_alquiler VARCHAR (40),
est_alquiler VARCHAR (1),
km_alquiler VARCHAR (15),
desc_alquiler VARCHAR (40),
val_alquiler VARCHAR (10)
);
INSERT INTO Reg_alquiler(id_alquiler, cod_alquiler, ced_cliente, cod_auto, fec_alquiler, obs_alquiler, est_alquiler, km_alquiler, desc_alquiler, val_alquiler) VALUES 
        ("1","260112001", "1755140744", "AUCH01", "2026-01-13", "Excelente estado", "O", "40000km", "Viaje ida y vuelta a Quito", "$1000");

DROP TABLE IF EXISTS usuarios;
CREATE TABLE usuarios(
id_usuario INT AUTO_INCREMENT PRIMARY KEY,
nombres VARCHAR(100) NOT NULL,
apellidos VARCHAR(100) NOT NULL,
usuario VARCHAR(50) UNIQUE NOT NULL,
fecha_nacimiento DATE,
correo VARCHAR(100) UNIQUE NOT NULL,
numero_recuperacion VARCHAR(20),
password VARCHAR(255) NOT NULL,
rol VARCHAR(20) DEFAULT 'admin'
);