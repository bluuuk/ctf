<?php

function login()
{
    if (empty($_POST["username"]) || empty($_POST["password"])) {
        return "Required field is empty";
    }

    $db = open_db();
    $stmt = $db->prepare("SELECT * FROM clients WHERE username = :username AND passwordhash = :passwordhash;");
    $stmt->bindParam(':username', $_POST["username"], SQLITE3_TEXT);
    $stmt->bindValue(':passwordhash', md5($_POST["password"]), SQLITE3_TEXT);
    $result = $stmt->execute();
    if (empty($result->fetchArray())) {
        return "Wrong login credentials";
    }

    $_SESSION["username"] = $_POST["username"];
    return true;
}

$alert = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $alert = login();
    if ($alert === true) {
        header('Location: index.php?page=account_info');
        exit();
    }
}
?>

<div style="color: red"><?=$alert ?></div>
<div class="login-form">
    <form method="POST">
        <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input class="form-control" name="username">
        </div>
        <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input type="password" class="form-control" name="password">
        </div>
        <input type="submit" class="btn btn-primary" value="Log in">
    </form>
</div>