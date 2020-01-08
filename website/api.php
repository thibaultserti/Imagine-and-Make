<?php

include_once "BddConnection.php";

$id = $_GET["id"];
$field = $_GET["field"];
$value = $_GET["value"];

$bdd = new BddConnection();
$bdd->connect();

if ($field == "checked") {
    $bdd->setChecked((int)$id, (int)$value);
} else {
    $bdd->setField((int)$id, $field, $value);
}
