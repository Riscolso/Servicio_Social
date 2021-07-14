CREATE SCHEMA IF NOT EXISTS Actividad6 DEFAULT CHARACTER SET utf8 ;
use Actividad6;

CREATE TABLE IF NOT EXISTS Pregunta (
  IdPregunta INT NOT NULL AUTO_INCREMENT,
  PreguntaText VARCHAR(100) NOT NULL,
  Opciones VARCHAR(500) NOT NULL,
  Tipo TINYINT NOT NULL,
  TiempoResp VARCHAR(5) NOT NULL,
  Intentos INT NOT NULL,
  Complejidad INT NOT NULL,
  PRIMARY KEY (IdPregunta))
ENGINE = InnoDB;

#NOTAS
#Formato de las opciones EJEMPLO: OP1-OPCION 1;OP2-OPCION 2;... HASTA OPCION N
#Tipo de pregunta 1- Selección múltiple; 0 - De una sola respuesta
#TiempoResp es una cadena que respresenta los minutos y segundos con forma mm:ss
#Complejidad roda 3 valores: 0 - Básico; 1- Intermedio; 2- Avanzado


INSERT INTO Pregunta values(1, '¿Qué es React?',
  'OP1-Es una librería de JavaScript declarativa para interfaces web
   OP2-Es un lenguaje de programación interpretado
   OP3-Es el nombre de una página web',
  0,
  '00:20',
  1,
  0
  );

INSERT INTO Pregunta values(2, '¿Qué es Pandas?',
  'OP1-Es un lenguaje de programación interpretado
   OP2-Es una biblioteca de software escrita como extensión de NumPy
   OP3-Es el nombre de un animal',
  0,
  '00:20',
  1,
  0
  );

INSERT INTO Pregunta values(3, '¿Qué es Pandas?',
  'OP1-Es un lenguaje de programación interpretado
   OP2-Es una biblioteca de software escrita como extensión de NumPy
   OP3-OP1-Es una librería de JavaScript declarativa para interfaces web',
  0,
  '00:20',
  1,
  0
  );

INSERT INTO Pregunta values(4, '¿Cuáles son algunas de las características de Python?',
  'OP1-Lenguaje interpretado
   OP2-Es una biblioteca de software escrita como extensión de NumPy
   OP3-Fuertemente tipado
   OP4-Totalmente Orientado a Objetos',
  1,
  '00:30',
  2,
  1
  );

INSERT INTO Pregunta values(5, '¿Cuáles son los tipos de datos de pandas?',
  'OP1-DataFrames
   OP2-Series
   OP3-Listas
   OP4-Panel
   OP5-Estructuras',
  1,
  '00:30',
  2,
  3
  );

INSERT INTO Pregunta values(6, '¿Cuáles son los estados de un ciclo de vida en React??',
  'OP1-Destruído
   OP2-Montado
   OP3-Actualización
   OP4-Desmontado
   OP5-Creado',
  1,
  '00:30',
  2,
  3
  );

INSERT INTO Pregunta values(7, '¿Por qué se llama python?',
  'OP1-En nombre del animal homonimo
   OP2-En nombre de una serie llamada "Monty Python Flying Circus"
   OP3-Nunca se ha mencionado',
  0,
  '00:15',
  1,
  0
  );
  
INSERT INTO Pregunta values(8, '¿Qué es numpy?',
  'OP1-Es el nombre de un lenguaje de programación
   OP2-Es una biblioteca para JavaScript que da soporte para crear vectores y matrices grandes multidimensionales"
   OP3-Es una biblioteca para Python que da soporte para crear vectores y matrices grandes multidimensionales',
  0,
  '00:15',
  1,
  0
  );