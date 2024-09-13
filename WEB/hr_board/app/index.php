<html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    </head>
    <title>HRBoard</title>
    <body>
        <nav class="navbar navbar-warning bg-warning">
        <h1 class="container-fluid justify-content-center text-success" style="margin-top: 15px;">Search new employers for your company!</h1>
            <form class="container-fluid justify-content-center" action="/index.php" method="GET" style="margin-top: 30px;">
              <div class="input-group mb-3" style="width: 33%;">
                <input type="text" class="form-control" placeholder="Search" name="q">
                <button class="btn btn-success" type="submit">Go</button>
              </div>
            </form>
        </nav>

    <?php
    define('DB_SERVER', 'hrboard-mariadb:3306');
    define('DB_USERNAME', 'root');
    define('DB_PASSWORD', 'SuperPupperMariaDbPassw0rdLolWTFHAHAHAHA');
    define('DB_DATABASE', 'hrboard');

    $db = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_DATABASE);

    if (isset($_GET['q'])){
        $q = $_GET['q'];
        $workers = mysqli_query($db, "SELECT * FROM workers WHERE name LIKE '%$q%'");
        if ($workers) {
            $workers = mysqli_fetch_all($workers);
            if (count($workers) != 0){
                foreach($workers as $worker){
    
                echo "<div class=\"d-flex justify-content-center\" style=\"margin-top: 15px; margin-bottom: 15px;\">
                        <div class=\"card text-center\" style=\"width: 36rem;\">
                            <div class=\"card-body\">
                                <h5 class=\"card-title\">
                                    $worker[1]
                                </h5>
                                <p class=\"card-text\">$worker[2]</p>
                                <img src=\"/avatars.php?avatar=$worker[3]&return_image=true\" style=\"width:200px; height:200px;\"/>
                                <p class=\"card-text\">Salary waiting: $worker[4] $</p>
                            </div>
                        </div>
                    </div>";
                }
            }
            else{
                echo "<div class=\"d-flex justify-content-center\" style=\"margin-top: 5%;\">
                        <div class=\"card text-center\" style=\"width: 30rem; padding: 15px;\">
                            <div class=\"card-body\">
                                <div class=\"alert alert-danger\" role=\"alert\">
                                    Not found
                                </div>
                            </div>
                        </div>
                    </div>";
            }
        }

    }

    else{
        $workers = mysqli_query($db, "SELECT * FROM workers");
        $workers = mysqli_fetch_all($workers);
        
        foreach($workers as $worker){
    
            echo "<div class=\"d-flex justify-content-center\" style=\"margin-top: 15px; margin-bottom: 15px;\">
                    <div class=\"card text-center\" style=\"width: 36rem;\">
                        <div class=\"card-body\">
                            <h5 class=\"card-title\">
                                $worker[1]
                            </h5>
                            <p class=\"card-text\">$worker[2]</p>
                            <img src=\"/avatars.php?avatar=$worker[3]&return_image=true\" style=\"width:200px; height:200px;\"/>
                            <p class=\"card-text\">Salary waiting: $worker[4] $</p>
                        </div>
                    </div>
                </div>";
        }
        
    }

    ?>

    </body>
</html>

