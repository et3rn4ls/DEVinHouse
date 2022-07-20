CREATE SCHEMA university;

CREATE TABLE university.alunos(
  mat_alu SERIAL primary key,
  nome VARCHAR(100) not null,
  dat_entrada DATE not null,
  cotista BOOLEAN not null
);

CREATE TABLE university.cursos(
  cod_curso SERIAL primary key,
  nome_curso VARCHAR(50) not null
);

CREATE TABLE university.departamentos(
  cod_dpto SERIAL primary key,
  nome_dpto VARCHAR(50) not null
);

CREATE TABLE university.matriculas(
  semestre INT primary key,
  nota DECIMAL(5,2) not null,
  faltas INT not null,
  status VARCHAR(1) not null
);

CREATE TABLE university.disciplinas(
  cod_disc SERIAL primary key,
  nome_disc INT not null,
  carga_horaria INT not null
);

CREATE TABLE university.matrizes_cursos(
  periodo INT not null
);


ALTER TABLE university.disciplinas ALTER column nome_disc TYPE VARCHAR(50);
ALTER TABLE university.matrizes_cursos ALTER column periodo TYPE VARCHAR(20);
