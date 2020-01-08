<?php


class BddConnection
{
    /**
     * @var PDO $pdo
     */
    private $pdo;
    public $editable_columns = ["Lastname", "Firstname", "Comment"];

    public function connect(): PDO
    {
        if ($this->pdo == null) {
            $this->pdo = new PDO("sqlite:db.sqlite");
        }

        return $this->pdo;
    }
    public function getData() {
        $statement = $this->pdo->query("SELECT * FROM Chambers");
        return $statement->fetchAll(PDO::FETCH_ASSOC);
    }

    public function setChecked(int $id, int $checked) {
        $sql = "UPDATE Chambers SET checked = :checked WHERE id = :id";
        $statement = $this->pdo->prepare($sql);
        return $statement->execute(["checked" => $checked, "id" => $id]);
    } 

    public function setField(int $id, string $field, string $value) {
        assert(in_array($field, $this->editable_columns));
        $sql = "UPDATE Chambers SET `$field` = :value WHERE id = :id"; // OK to inject the variable directly, because we checked its value before
        $statement = $this->pdo->prepare($sql);
        return $statement->execute(["value" => $value, "id" => $id]);
    }
}
