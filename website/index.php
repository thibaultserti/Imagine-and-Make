<?php

require_once 'BddConnection.php';

$bdd = new BddConnection();
$bdd->connect();

$data = $bdd->getData();

$first = $data[0];
?>
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>


<table class="table table-striped">
    <thead class="thead-dark">
    <tr>
        <?php foreach ($first as $key => $value): ?>
            <th><?= $key ?></th>
        <?php endforeach; ?>
        <th>Done</th>
    </tr>
    </thead>

    <tbody>
    <?php
    foreach ($bdd->getData() as $data): ?>
        <tr>
            <?php foreach ($data as $key => $value): ?>
                <td><?= $value ?></td>
            <?php endforeach; ?>
            <td><input type="checkbox"></td>
        </tr>

    <?php endforeach; ?>
    </tbody>
</table>


</body>
</html>
