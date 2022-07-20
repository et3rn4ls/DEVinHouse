create schema university;

create table university.alunos(
  mat_alu SERIAL primary key,
  nome VARCHAR(100) not null,
  dat_entrada DATE not null,
  cotista BOOLEAN not null
);

create table university.cursos(
  cod_curso SERIAL primary key,
  nome_curso VARCHAR(50) not null
);

create table university.departamentos(
  cod_dpto SERIAL primary key,
  nome_dpto VARCHAR(50) not null
);

create table university.matriculas(
  semestre INT primary key,
  nota DECIMAL(5,2) not null,
  faltas INT not null,
  status VARCHAR(1) not null
);

create table university.disciplinas(
  cod_disc SERIAL primary key,
  nome_disc INT not null,
  carga_horaria INT not null
);

create table university.matrizes_cursos(
  periodo INT not null
);

alter table university.disciplinas alter column nome_disc type varchar(50);
