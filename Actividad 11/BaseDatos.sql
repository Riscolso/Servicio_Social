CREATE SCHEMA IF NOT EXISTS Actividad11 DEFAULT CHARACTER SET utf8 ;
use Actividad11;

CREATE TABLE IF NOT EXISTS Pregunta (
  IdPregunta INT NOT NULL AUTO_INCREMENT,
  PreguntaJSON VARCHAR(700) NOT NULL,
  PRIMARY KEY (IdPregunta))
ENGINE = InnoDB;

