CREATE TABLE IF NOT EXISTS Academico_docentes (
    codigo VARCHAR(6) PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    materia VARCHAR(150) NOT NULL,
    ciudad VARCHAR(150) NOT NULL
);
INSERT INTO `Academico_docentes` (`codigo`, `nombre`, `materia`, `ciudad`) VALUES ('10', 'Luis', 'Simulacion', 'Loja');
INSERT INTO `Academico_docentes` (`codigo`, `nombre`, `materia`, `ciudad`) VALUES ('11', 'Veronica', 'Ingles', 'Loja');
INSERT INTO `Academico_docentes` (`codigo`, `nombre`, `materia`, `ciudad`) VALUES ('12', 'Mario', 'Redes', 'Loja');