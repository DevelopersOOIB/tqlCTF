<?php

if (isset($_GET['avatar']) && isset($_GET['return_image'])){
    $avatar = $_GET['avatar'];
    echo file_get_contents("./img/$avatar");
}

?>