<?php

function get_account_numbers_for_current_user()
{
    $db = open_db();
    $stmt = $db->prepare("SELECT account_number FROM accounts WHERE client = :username;");
    $stmt->bindValue(':username', get_logged_in_user(), SQLITE3_TEXT);
    $result = $stmt->execute();
    $accounts = [];
    while ($account = $result->fetchArray(SQLITE3_ASSOC)) {
        $account_numbers[] = $account["account_number"];
    }
    return $account_numbers;
}

function transfer()
{
    if (empty($_POST["source"]) || empty($_POST["destination"]) || empty($_POST["amount"])) {
        return "Required field is empty";
    }

    $_POST["source"] = mb_strtoupper($_POST["source"]);
    $_POST["destination"] = mb_strtoupper($_POST["destination"]);

    if ($_POST["source"] == $_POST["destination"]) {
        return "Destination account number should be different from source account number";
    }

    if (!in_array($_POST["source"], get_account_numbers_for_current_user())) {
        return "Invalid source account number";
    }

    if (!is_numeric($_POST["amount"]) || $_POST["amount"] < 0) {
        return "Invalid amount";
    }

    if (mb_strlen($_POST["destination"]) < 10) {
        return "Invalid destination account number";
    }

    if (mb_substr($_POST["destination"],0,2) !== "EU" || mb_substr($_POST["destination"],4,4) !== "SECB") {
        return "Transfers currently limited to accounts within SecureBank";
    }
    
    $db = open_db();
    $stmt = $db->prepare("SELECT * FROM accounts WHERE account_number = :destination_account_number;");
    $stmt->bindParam(':destination_account_number', $_POST["destination"], SQLITE3_TEXT);
    $result = $stmt->execute();
    if (empty($result->fetchArray())) {
        return "Destination account doesn't exist";
    }
    
    $amount = floor($_POST["amount"] * 100);

    $stmt = $db->prepare("SELECT balance FROM accounts WHERE account_number = :source_account_number;");
    $stmt->bindParam(':source_account_number', $_POST["source"], SQLITE3_TEXT);
    $result = $stmt->execute();
    $current_balance = $result->fetchArray(SQLITE3_ASSOC)["balance"];
    if ($current_balance < $amount) {
        return "Insufficient funds";
    }
    $db->close();

	$source_account_number = $_POST["source"];
	$destination_account_number = $_POST["destination"];
	$timestamp = time();
	$hash = $amount . $source_account_number . $destination_account_number . $timestamp;
    for ($i = 0; $i < 3000000; $i++) {
        $hash = sha1($hash);
    }
    
    $db = open_db();
    $stmt = $db->prepare("INSERT INTO transactions (amount, source_account_number, destination_account_number, timestamp, hash)
    VALUES (:amount, :source_account_number, :destination_account_number, :timestamp, :hash)");
    $stmt->bindParam(':amount', $amount, SQLITE3_INTEGER);
    $stmt->bindParam(':source_account_number', $source_account_number, SQLITE3_TEXT);
    $stmt->bindParam(':destination_account_number', $destination_account_number, SQLITE3_TEXT);
    $stmt->bindParam(':timestamp', $timestamp, SQLITE3_INTEGER);
    $stmt->bindParam(':hash', $hash, SQLITE3_TEXT);
    $stmt->execute();

    $new_balance = $current_balance - $amount;
    $stmt = $db->prepare("UPDATE accounts SET balance=:balance WHERE account_number = :account_number");
    $stmt->bindParam(':balance', $new_balance, SQLITE3_INTEGER);
    $stmt->bindParam(':account_number', $_POST["source"], SQLITE3_TEXT);
    $stmt->execute();

    $stmt = $db->prepare("UPDATE accounts SET balance=balance + :amount WHERE account_number = :account_number");
    $stmt->bindParam(':amount', $amount, SQLITE3_INTEGER);
    $stmt->bindParam(':account_number', $_POST["destination"], SQLITE3_TEXT);
    $stmt->execute();

    return "";
}

$alert = "";
$success = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $alert = transfer();
    if (empty($alert)) {
        $success = "Transaction completed";
    }
}
?>

<div style="color: red"><?=$alert ?></div>
<div style="color: green"><?=$success ?></div>
<form method="POST">
    <div class="mb-3">
        <label for="source" class="form-label">Transfer from</label>
        <select name="source">
            <?php foreach (get_account_numbers_for_current_user() as $account_number): ?>
            <option value="<?=$account_number ?>"><?=$account_number ?></option>
            <?php endforeach; ?>
        </select>
    </div>
    <div class="mb-3">
        <label for="destination" class="form-label">Transfer to</label>
        <input class="form-control" name="destination">
    </div>
    <div class="mb-3">
        <label for="amount" class="form-label">Amount (EUR)</label>
        <input class="form-control" name="amount" placeholder="0.00">
    </div>
    <input type="submit" class="btn btn-primary" value="Transfer">
</form>