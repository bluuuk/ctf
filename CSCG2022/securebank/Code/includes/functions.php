<?php
function open_db()
{
     $db = new SQLite3('bank.db');
     $db->busyTimeout(12000);
     //$db->open('bank.db');
     return $db;
}

function get_logged_in_user()
{
    if (!empty($_SESSION['username'])) {
        return $_SESSION['username'];
    }
    return null;
}