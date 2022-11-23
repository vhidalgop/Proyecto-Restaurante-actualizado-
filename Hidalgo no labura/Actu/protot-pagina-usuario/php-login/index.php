<?php
  session_start();

  require 'database.php';

  if (isset($_SESSION['users_id'])) {
    $records = $conn->prepare('SELECT id, email, password FROM users WHERE id = :id');
    $records->bindParam(':id', $_SESSION['users_id']);
    $records->execute();
    $results = $records->fetch(PDO::FETCH_ASSOC);

    $user = null;

    if (count($results) > 0)  {
      $users = $results;
    }
  }
?>

<!DOCTYPE html>
<html><
  <head>
    <meta charset="utf-8">
    <title>Mesas al toque</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
    <link rel="stylesheet" href="./assets/css/style.css">
  </head>
  <body>
    <?php require './partials/header.php' ?>

    <?php if(!empty($users)): ?>
      <br> Bienvenido. <?= $users['email']; ?>
      <br>Pudiste acceder exitosamente a tu cuenta
      <a href="../index.html">
        Volver a pagina principal
      </a>
      <br>¿O desea cerrar sesión?
      <a href="./logout.php">
        Logout
      </a>

    <?php else: ?>
      <h1>Por favor inicia sesion o crea una cuenta</h1>

      <a href="./login.php">Login</a> or
      <a href="./signup.php">SignUp</a>
    <?php endif; ?>
  </body>
</html>