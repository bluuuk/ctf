<?php

      if(!isset($_POST['interface'])){
        highlight_file($_SERVER['SCRIPT_FILENAME']);
        exit();
      }

        $iface = escapeshellcmd($_POST['interface']);
        echo "<pre>" . "iw dev | awk -v iface=".$iface." '/^phy#/ { phy = $0 } $1 == \"Interface\" { interface = $2 } interface == iface { print phy }'" . "</pre>\n";
        // get physical device for selected interface
        exec("iw dev | awk -v iface=".$iface." '/^phy#/ { phy = $0 } $1 == \"Interface\" { interface = $2 } interface == iface { print phy }'", $return);
        echo "<pre>" . $return[0] . "<\pre>\n";
        $phy = $return[0];
        exec('iw '.$phy.' info', $info);
    echo "<pre>" . $info[0] . "</pre>\n";

?>