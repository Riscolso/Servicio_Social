create database IF NOT EXISTS grupo;
use grupo;

CREATE TABLE IF NOT EXISTS Alumno (
  IdAlumno INT NOT NULL AUTO_INCREMENT,
  Nombre VARCHAR(45) NOT NULL,
  Calificacion DECIMAL(4,2) NOT NULL,
  PRIMARY KEY (IdAlumno))
ENGINE = InnoDB;

INSERT INTO Alumno values(1, 'Alan Brito', 4.5);
INSERT INTO Alumno values(2, 'Alex Tintor', 6.5);
INSERT INTO Alumno values(3, 'Helen Chufe', 7.2);
INSERT INTO Alumno values(4, 'Elsa Capunta', 8.9);
INSERT INTO Alumno values(5, 'Victor Tilla', 8.5);


