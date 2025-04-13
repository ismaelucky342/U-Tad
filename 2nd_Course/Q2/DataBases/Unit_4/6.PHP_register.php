<?php
$conexion = new mysqli("localhost", "root", "tu_contraseña", "usuarios_web");

if ($conexion->connect_error) {
    die("Conexión fallida: " . $conexion->connect_error);
}

$username = $_POST['username'] ?? '';
$email = $_POST['email'] ?? '';
$password = $_POST['password'] ?? '';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $stmt = $conexion->prepare("SELECT id FROM USUARIOS WHERE username=? OR email=?");
    $stmt->bind_param("ss", $username, $email);
    $stmt->execute();
    $stmt->store_result();

    if ($stmt->num_rows > 0) {
        echo "❌ El usuario o email ya existen.";
    } else {
        $hash = password_hash($password, PASSWORD_BCRYPT);
        $stmt = $conexion->prepare("INSERT INTO USUARIOS (username, email, password) VALUES (?, ?, ?)");
        $stmt->bind_param("sss", $username, $email, $hash);
        if ($stmt->execute()) {
            echo "✅ Registro exitoso.";
        } else {
            echo "Error: " . $stmt->error;
        }
    }

    
    $stmt->close();
}

$conexion->close();
?>
