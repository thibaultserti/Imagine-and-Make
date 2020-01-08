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
    </tr>
    </thead>

    <tbody>
    <?php
    foreach ($bdd->getData() as $data): ?>
        <tr data-id="<?= $data["id"] ?>">
            <?php foreach ($data as $key => $value): ?>
                <?php if ($key == "checked") continue ?>
                <td data-field="<?= $key ?>">
                    <?php if (in_array($key, $bdd->editable_columns)): ?>
                        <input type="text" value="<?= $value ?>">
                    <?php else: ?>
                        <?= $value ?>
                    <?php endif; ?>
                </td>
            <?php endforeach; ?>
            <td><input type="checkbox" <?= $data["checked"] == 0 ? "" : "checked" ?>></td>
        </tr>

    <?php endforeach; ?>
    </tbody>
</table>

<script>
  document.querySelectorAll('input[type="text"]').forEach(element => {
    element.addEventListener("keypress", event => {
      if (event.key === "Enter") {
        const lineId = element.closest("tr").dataset.id
        const key = element.closest("td").dataset.field
        const value = element.value
        fetch(`/api.php?id=${lineId}&field=${key}&value=${value}`)
      }
    })
  })

  document.querySelectorAll('input[type="checkbox"]').forEach(element => {
    element.addEventListener("click", event => {
      const lineId = element.closest("tr").dataset.id
      const checked = element.checked ? "1" : "0"
      fetch(`/api.php?id=${lineId}&field=checked&value=${checked}`)
    })
  })

</script>


</body>
</html>
