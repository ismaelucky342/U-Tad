# Guión para Video de Demostración

**Duración**: 15-20 minutos

## Estructura

### 1. INTRO (30 seg)
```
"Hola, en este video demuestro Mini Twitter, una aplicación 
con AWS Lambda, RDS, S3 y API Gateway."
```

### 2. REGISTRO DE USUARIO (+2 pts) - 4 min

**a) BD ANTES**
```sql
SELECT * FROM users;
-- Mostrar usuarios actuales
```

**b) Crear usuario en web**
- Ir a register.html
- Usuario: test_[fecha]
- Password: password123
- Registrar

**c) BD DESPUÉS**
```sql
SELECT * FROM users ORDER BY created_at DESC LIMIT 1;
-- Mostrar nuevo usuario
```

**d) Código Lambda**
- Abrir userRegister en AWS Console
- Explicar: recibe datos, valida, inserta en BD

### 3. LOGIN (+2 pts) - 4 min

**a) Página web**
- Mostrar login.html
- Tabla users con passwords

**b) Código Lambda**  
- Abrir userLogin en AWS Console
- Explicar: busca user, compara password, devuelve OK/KO

**c) Demo login**
- Login con usuario creado
- Mostrar redirección a postComment

### 4. CREAR COMENTARIO (obligatorio) - 5 min

**a) BD y S3 ANTES**
```sql
SELECT * FROM comments ORDER BY created_at DESC LIMIT 3;
```
- Mostrar bucket S3

**b) Crear comentario**
- En postComment.html
- Texto: "Comentario de demostración [hora]"
- Adjuntar video
- Publicar

**c) BD y S3 DESPUÉS**
```sql
SELECT * FROM comments ORDER BY created_at DESC LIMIT 1;
```
- Verificar video en S3

**d) Código Lambda**
- Mostrar twitterPost
- Explicar: recibe datos, guarda en BD

### 5. LEER COMENTARIOS (obligatorio) - 3 min

**a) Ver timeline**
- Abrir readComment.html
- Mostrar comentarios

**b) Crear y actualizar**
- Crear otro comentario
- Refrescar página
- Mostrar nuevo comentario

**c) Código Lambda**
- Mostrar twitterRead
- Explicar: SELECT all, devuelve JSON

### 6. BÚSQUEDA (+1 pt) - 3 min

**a) Query BD**
```sql
SELECT username, COUNT(*) FROM comments GROUP BY username;
```

**b) Código Lambda**
- Mostrar searchByUser
- Explicar: filtra por username

**c) Demo web**
- Buscar usuario en searchUser.html
- Mostrar resultados

### 7. DISEÑO (+1 pt) - 2 min
- Tour de páginas
- Mostrar diseño consistente
- Colores, botones, cards

### 8. CIERRE (1 min)
```
"Implementé:
- RDS con 2 tablas
- 5 funciones Lambda
- S3 hosting + videos
- API Gateway
- Sistema completo funcionando
Total: 10/10 puntos"
```

---

## Checklist Pre-Grabación

- [ ] RDS funcionando con datos
- [ ] Lambda functions deployadas
- [ ] S3 con sitio web activo
- [ ] Video de prueba listo (< 10MB)
- [ ] MySQL Workbench abierto
- [ ] AWS Console en Lambda
- [ ] Navegador limpio

## Tips

- Habla claro y pausado
- Muestra URLs completas
- Zoom si es necesario
- No te apresures
- Practica antes
- 15-20 min es ideal
