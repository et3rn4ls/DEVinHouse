INSERT INTO university.alunos(nome, dat_entrada, cotista) VALUES ('Kurt Cobain', '2022-02-11', TRUE);
INSERT INTO university.alunos(nome, dat_entrada, cotista) VALUES ('Dave Grohl', '2022-03-19', FALSE);
INSERT INTO university.alunos(nome, dat_entrada, cotista) VALUES ('Krist Novoselic', '2022-06-23', TRUE);
INSERT INTO university.alunos(nome, dat_entrada, cotista) VALUES ('Serj Tankian', '2022-05-01', TRUE);
INSERT INTO university.alunos(nome, dat_entrada, cotista) VALUES ('Daron Malakian', '2022-01-13', FALSE);
INSERT INTO university.alunos(nome, dat_entrada, cotista) VALUES ('John Dolmanyan', '2022-04-21', TRUE);
INSERT INTO university.alunos(nome, dat_entrada, cotista) VALUES ('Shavo Odadjian', '2022-01-08', FALSE);
INSERT INTO university.alunos(nome, dat_entrada, cotista) VALUES ('Chester Bennington', '2022-03-17', TRUE);
INSERT INTO university.alunos(nome, dat_entrada, cotista) VALUES ('Mike Shinoda', '2022-03-23', FALSE);
INSERT INTO university.alunos(nome, dat_entrada, cotista) VALUES ('Brad Delson', '2022-06-15', TRUE);

INSERT INTO university.cursos(nome_curso) VALUES ('Analise e Desenvolvimento de Sistemas');
INSERT INTO university.cursos(nome_curso) VALUES ('Tecnologia em Redes de Computadores');
INSERT INTO university.cursos(nome_curso) VALUES ('Direito');
INSERT INTO university.cursos(nome_curso) VALUES ('Medicina');
INSERT INTO university.cursos(nome_curso) VALUES ('Odontologia');
INSERT INTO university.cursos(nome_curso) VALUES ('Ciências da Computação');
INSERT INTO university.cursos(nome_curso) VALUES ('Gestão de Tecnologia da Informação');
INSERT INTO university.cursos(nome_curso) VALUES ('Segurança da Informação');
INSERT INTO university.cursos(nome_curso) VALUES ('Administração');
INSERT INTO university.cursos(nome_curso) VALUES ('Veterinária');

INSERT INTO university.departamentos(nome_dpto) VALUES ('Ciências Sociais Aplicadas');
INSERT INTO university.departamentos(nome_dpto) VALUES ('Ciências Exatas');
INSERT INTO university.departamentos(nome_dpto) VALUES ('Ciências Jurídicas');
INSERT INTO university.departamentos(nome_dpto) VALUES ('Ciências da Saúde');
INSERT INTO university.departamentos(nome_dpto) VALUES ('Ciências Humanas');
INSERT INTO university.departamentos(nome_dpto) VALUES ('Ciências da Terra');
INSERT INTO university.departamentos(nome_dpto) VALUES ('Tecnologia');
INSERT INTO university.departamentos(nome_dpto) VALUES ('Artes, Comunicação e Design');
INSERT INTO university.departamentos(nome_dpto) VALUES ('Ciências Agrárias');
INSERT INTO university.departamentos(nome_dpto) VALUES ('Ciências Biológicas');

INSERT INTO university.matriculas(nota, faltas, status) VALUES ('9,50', 4, 'A');
INSERT INTO university.matriculas(nota, faltas, status) VALUES ('6,80', 2, 'A');
INSERT INTO university.matriculas(nota, faltas, status) VALUES ('2,00', 24, 'R');
INSERT INTO university.matriculas(nota, faltas, status) VALUES ('5,50', 1, 'A');
INSERT INTO university.matriculas(nota, faltas, status) VALUES ('7,75', 3, 'A');
INSERT INTO university.matriculas(nota, faltas, status) VALUES ('3,90', 9, 'R');
INSERT INTO university.matriculas(nota, faltas, status) VALUES ('10,00', 0, 'A');
INSERT INTO university.matriculas(nota, faltas, status) VALUES ('8,33', 2, 'A');
INSERT INTO university.matriculas(nota, faltas, status) VALUES ('7,50', 5, 'A');
INSERT INTO university.matriculas(nota, faltas, status) VALUES ('6,45', 38, 'R');

INSERT INTO university.disciplinas(nome_disc, carga_horaria) VALUES ('Direito Penal', 200);
INSERT INTO university.disciplinas(nome_disc, carga_horaria) VALUES ('Anatomia Animal', 180);
INSERT INTO university.disciplinas(nome_disc, carga_horaria) VALUES ('Matemática I', 160);
INSERT INTO university.disciplinas(nome_disc, carga_horaria) VALUES ('Algoritmo', 220);
INSERT INTO university.disciplinas(nome_disc, carga_horaria) VALUES ('Gestão de Projetos', 280);
INSERT INTO university.disciplinas(nome_disc, carga_horaria) VALUES ('Infraestrutura como Código', 300);
INSERT INTO university.disciplinas(nome_disc, carga_horaria) VALUES ('Cloud Computing', 260);
INSERT INTO university.disciplinas(nome_disc, carga_horaria) VALUES ('Gestão de Riscos', 190);
INSERT INTO university.disciplinas(nome_disc, carga_horaria) VALUES ('Endodontia', 120);
INSERT INTO university.disciplinas(nome_disc, carga_horaria) VALUES ('Lógica de Programação', 100);

INSERT INTO university.matrizes_cursos(periodo) VALUES ('MATUTINO');
INSERT INTO university.matrizes_cursos(periodo) VALUES ('VESPERTINO');
INSERT INTO university.matrizes_cursos(periodo) VALUES ('NOTURNO');
INSERT INTO university.matrizes_cursos(periodo) VALUES ('INTEGRAL');
