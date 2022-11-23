<?php

  session_start();

  if (isset($_SESSION['users_id'])) {
    header('Location: /php-login');
  }
  require './database.php';

  if (!empty($_POST['email']) && !empty($_POST['password'])) {
    $records = $conn->prepare('SELECT id, email, password FROM users WHERE email = :email');
    $records->bindParam(':email', $_POST['email']);
    $records->execute();
    $results = $records->fetch(PDO::FETCH_ASSOC);

    $message = '';

    if (count($results) > 0 && password_verify($_POST['password'], $results['password'])) {
      $_SESSION['users_id'] = $results['id'];
      header("Location: ./index.php");
    } else {
      $message = 'Lo lamento, las credenciales no funcionan';
    }
  }

?>

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Login</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
    <link rel="stylesheet" href="./assets/css/style.css">
  </head>
  <body>
    <?php require './partials/header.php' ?>

    <?php if(!empty($message)): ?>
      <p> <?= $message ?></p>
    <?php endif; ?>

    <h1>Login</h1>
    <span>or <a href="./signup.php">SignUp</a></span>

    <form action="./login.php" method="POST">
      <input name="email" type="text" placeholder="Ingresa una direccion de mail: ">
      <input name="password" type="password" placeholder="Ingresa la contraseña: ">
      <input type="submit" value="Submit">
    </form>
  </body>
</html>