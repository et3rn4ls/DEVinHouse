UPDATE university.alunos SET nome = 'Anthony Kiedis' WHERE nome = 'Brad Delson';
UPDATE university.alunos SET cotista = TRUE WHERE mat_alu = 9;

UPDATE university.cursos SET nome_curso = 'Gestão de TI' WHERE nome_curso = 'Gestão de Tecnologia da Informação';
UPDATE university.cursos SET nome_curso = 'Engenharia da Computação' WHERE cod_curso = 6;

UPDATE university.departamentos SET nome_dpto = 'Departamento de Ciências Penais' WHERE nome_dpto = 'Ciências Jurídicas';
UPDATE university.departamentos SET nome_dpto = 'Departamento de Ciências Biológicas' WHERE cod_dpto = 10;

UPDATE university.matriculas SET faltas = 36 WHERE semestre = 10;
UPDATE university.matriculas SET status = 'A' WHERE semestre = 10;

UPDATE university.disciplinas SET nome_disc = 'Automação de TI' WHERE cod_disc = 6;
UPDATE university.disciplinas SET carga_horaria = 140 WHERE cod_disc = 6;

UPDATE university.matrizes_cursos SET periodo = 'MAT' WHERE periodo = 'MATUTINO';
UPDATE university.matrizes_cursos SET periodo = 'VESP' WHERE periodo = 'VESPERTINO';
UPDATE university.matrizes_cursos SET periodo = 'NOT' WHERE periodo = 'NOTURNO';
