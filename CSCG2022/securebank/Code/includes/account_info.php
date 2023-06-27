<?php

$db = open_db();
$stmt = $db->prepare("SELECT * FROM accounts WHERE client = :username;");
$stmt->bindValue(':username', get_logged_in_user(), SQLITE3_TEXT);
$result_accounts = $stmt->execute();

while ($account = $result_accounts->fetchArray(SQLITE3_ASSOC)):
    ?>
    <h3><?=$account['account_number']?> - <?=$account['name']?></h3>
    <b>Balance:</b> <?=number_format($account['balance'] / 100, 2) ?> EUR
    <?php
    $sql = "SELECT * FROM transactions WHERE source_account_number = '" . $account['account_number'] . "' OR destination_account_number = '" . $account['account_number'] . "' ORDER BY timestamp DESC LIMIT 25;";
    $result_transactions = $db->query($sql);
    ?>
    <table>
        <tr>
            <th>Account number</th>
            <th>Amount</th>
            <th>Date</th>
        </tr>
    <?php 
    while ($transaction = $result_transactions->fetchArray(SQLITE3_ASSOC)):
        $direction = $transaction['source_account_number'] == $account['account_number'] ? 'out' : 'in';
        ?>
        <tr>
            <td><?=$direction=='out' ? $transaction['destination_account_number'] : $transaction['source_account_number']?></td>
            <td><?=$direction=='out' ? '-' : '' ?><?=number_format($transaction['amount'] / 100, 2) ?> EUR</td>
            <td><?=date('Y-m-d H:i', $transaction['timestamp'])?></td>
        </tr>
        <?php
    endwhile;
    ?>
    </table>
    <?php
endwhile;