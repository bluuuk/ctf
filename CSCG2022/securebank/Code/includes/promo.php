<h3>Promotion</h3>
<p>If your savings account reaches 25 euro or more you receive a free gift. Visit this page after you have saved 25 euro to claim your gift.</p>

<?php
$db = open_db();
$stmt = $db->prepare("SELECT balance FROM accounts WHERE name = 'Savings account'  AND client = :username;");
$stmt->bindValue(':username', get_logged_in_user(), SQLITE3_TEXT);
$balance = $result = $stmt->execute()->fetchArray(SQLITE3_ASSOC)["balance"];

if ($balance >= 2500):
?>
<h3>Your gift</h3>
<p>Congratulations! You have saved 25 euro. Your gift code is <b><?=$_ENV["PROMOCODE"] ?></b></p>
<?php
endif;