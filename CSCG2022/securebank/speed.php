<?php

$source_account_number = "source";
$destination_account_number = "destination";
$timestamp = time();
$hash = $amount . $source_account_number . $destination_account_number . $timestamp;
for ($i = 0; $i < 3000000; $i++) {
    $hash = sha1($hash);
}

?>