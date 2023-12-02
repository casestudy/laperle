<?php
$servername = "localhost";
$username = "root";
$password = "nderuth";
$dbname = "contacts";
ini_set('error_reporting', E_ALL);

try {
    $conn = new PDO("mysql:host=$servername; dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $stmt = $conn->prepare("SELECT id, password, username, email FROM users");
    $stmt->execute();

    $result = $stmt->setFetchMode(PDO::FETCH_ASSOC);
    $data=$stmt->fetchAll();    

    $email = "";
    foreach($data as $d){
        $email =$d['email'];
    }

    echo $email;
} catch(PDOException $e){
    echo "Error: " . $e->getMessage();
}
?>