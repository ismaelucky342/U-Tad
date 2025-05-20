-- Ejercicios de álgebra relacional

-- Supongamos las siguientes relaciones:
-- Estudiante(DNI, Nombre, Edad, Carrera)
-- Curso(CodCurso, NombreCurso, Creditos)
-- Matricula(DNI, CodCurso, Año)

-- 1. Obtener los nombres de los estudiantes matriculados en el curso 'Bases de Datos'
π_Nombre (σ_NombreCurso='Bases de Datos' (Estudiante ⨝ Matricula ⨝ Curso))

-- 2. Listar los cursos en los que no se ha matriculado ningún estudiante
π_NombreCurso (Curso) - π_NombreCurso (Curso ⨝ Matricula)

-- 3. Obtener los estudiantes que no están matriculados en ningún curso
π_Nombre (Estudiante) - π_Nombre (Estudiante ⨝ Matricula)

-- 4. Listar los nombres de los estudiantes y los cursos en los que están matriculados
π_Nombre,NombreCurso (Estudiante ⨝ Matricula ⨝ Curso)

-- 5. Obtener los DNIs de los estudiantes que se han matriculado en todos los cursos
π_DNI (Estudiante) ÷ π_CodCurso (Curso)

-- 6. Listar los nombres de los estudiantes mayores de 21 años matriculados en algún curso
π_Nombre (σ_Edad>21 (Estudiante ⨝ Matricula))

-- 7. Obtener los nombres de los cursos con más de 5 créditos
π_NombreCurso (σ_Creditos>5 (Curso))

-- 8. Listar los DNIs de los estudiantes que se han matriculado en el año 2024
π_DNI (σ_Año=2024 (Matricula))

-- 9. Obtener los nombres de los estudiantes y los nombres de los cursos en los que se han matriculado en 2023
π_Nombre,NombreCurso (σ_Año=2023 (Estudiante ⨝ Matricula ⨝ Curso))

-- 10. Listar los nombres de los estudiantes que se han matriculado en el curso 'Matemáticas' y en el curso 'Bases de Datos'
π_Nombre (
	(σ_NombreCurso='Matemáticas' (Estudiante ⨝ Matricula ⨝ Curso))
	∩
	(σ_NombreCurso='Bases de Datos' (Estudiante ⨝ Matricula ⨝ Curso))
)

-- 11. Obtener los nombres de los estudiantes que se han matriculado en al menos un curso con más de 6 créditos
π_Nombre (
	Estudiante ⨝ Matricula ⨝ (σ_Creditos>6 (Curso))
)

-- 12. Listar los nombres de los cursos en los que solo se ha matriculado un estudiante
π_NombreCurso (
	σ_count(DNI)=1 (Curso ⨝ Matricula) 
)

-- 13. Obtener los nombres de los estudiantes que no estudian 'Informática'
π_Nombre (
	σ_Carrera<>'Informática' (Estudiante)
)

-- 14. Listar los cursos en los que se han matriculado estudiantes menores de 20 años
π_NombreCurso (
	(σ_Edad<20 (Estudiante) ⨝ Matricula ⨝ Curso)
)

-- 15. Obtener los DNIs de los estudiantes que se han matriculado en exactamente dos cursos
π_DNI (
	σ_count(CodCurso)=2 (Matricula)
)

-- 16. Listar los nombres de los estudiantes que se han matriculado en cursos en ambos años 2023 y 2024
π_Nombre (
	(σ_Año=2023 (Estudiante ⨝ Matricula)) ∩ (σ_Año=2024 (Estudiante ⨝ Matricula))
)

-- 17. Obtener los nombres de los cursos en los que se han matriculado estudiantes de la carrera 'Matemáticas'
π_NombreCurso (
	(σ_Carrera='Matemáticas' (Estudiante) ⨝ Matricula ⨝ Curso)
)

-- 18. Listar los nombres de los estudiantes que se han matriculado en cursos con menos de 4 créditos
π_Nombre (
	Estudiante ⨝ Matricula ⨝ (σ_Creditos<4 (Curso))
)

-- 19. Obtener los nombres de los estudiantes y el número de cursos en los que están matriculados
π_Nombre,count(CodCurso) (
	Estudiante ⨝ Matricula
)

-- 20. Listar los nombres de los cursos en los que no se ha matriculado ningún estudiante de más de 25 años
π_NombreCurso (
	π_NombreCurso (Curso) - π_NombreCurso ((σ_Edad>25 (Estudiante) ⨝ Matricula ⨝ Curso))
)