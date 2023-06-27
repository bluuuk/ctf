<?php
include_once 'includes/functions.php';
error_reporting(E_ALL);
ini_set("display_errors", 1);
ob_start();
session_start();
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>SecureBank</title>
    </head>
    <body>
        <?php
        if (get_logged_in_user() !== null):
        ?>
        <div class="menu">
            <a href="/?page=account_info">Account info</a> - <a href="/?page=transfer">Transfer money</a> - <a href="/?page=promo">Promotion</a> - <a href="/?page=logout">Logout</a>
        </div>
        <?php
        endif;
        
        $page = isset($_GET['page']) ? $_GET['page'] : 'login';
        if ($page !== "login" && get_logged_in_user() === null):
        ?>
            Please <a href="/?page=login">login</a> to view this page.
        <?php
        else:
            $valid_pages = ['login', 'logout', 'account_info', 'transfer', 'promo'];
            if (!in_array($page, $valid_pages, true)) {
                http_response_code(404);
                echo "Page not found";
            } else {
                include_once 'includes/' . $page . '.php';
            }
            endif;
        ?>
    </body>
</html>