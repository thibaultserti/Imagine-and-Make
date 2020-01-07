<?php


class BddConnection
{
    /**
     * @var PDO $pdo
     */
    private $pdo;

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
}
