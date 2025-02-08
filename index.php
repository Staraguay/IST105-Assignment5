<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Treasure Hunter</title>
    <link rel="stylesheet" href="css/style.css" type="text/css">
</head>
<body>

    <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {

            session_start();
            if (isset($_POST["inputNumber"]) && isset($_POST["inputText"]))
            {
                $inputNumber = escapeshellarg($_POST["inputNumber"]);
                $inputText = escapeshellarg($_POST["inputText"]);

                $json_response = shell_exec("python3 process/process.py $inputNumber $inputText");
                $response = json_decode($json_response, true);

                // save the data in the session
                if($response)
                {

                    $_SESSION["submited"] = true;
                    $_SESSION["number"] = $response["nPuzzle"];
                    $_SESSION["btext"] = $response["bmessage"];
                    $_SESSION["vowels"] = $response["vocals"];
                    $_SESSION["hunter"] = $response["treasure"];
                }

            }

            // Redirect to the same page to avoid data resending
            header("Location: " . $_SERVER["PHP_SELF"]);
            exit();
        }



        // Display data only if saved in session
        session_start();
        if (isset($_SESSION["submited"])) {

            $nPuzzle = $_SESSION["number"];
            $bMessage = $_SESSION["btext"];
            $vocals = $_SESSION["vowels"];
            $treasure = $_SESSION["hunter"];
        }
    ?>
    <main>
        <div class="container">
            <h1>Treasure Hunt - Assignment 5</h1>
            <form action="index.php" method="POST" class="form">
                <label>Enter a number</label>
                <input id="inputNumber" type="number" name="inputNumber" required>
                <label>Enter a text</label>
                <input id="inputText" type="text" name="inputText" required>
                <input class="btn-submit" type="submit" value="Solve the Puzzle" name="submit">
            </form>
        </div>
        <?php

         if(isset($_SESSION["submited"]))
         {
        print"<div class='container-response'>
            <h2>The results are</h2>
            <p>The result of the number is: <span>$nPuzzle</span></p>
            <p>The text in binary is: <span>$bMessage</span></p>
            <p>The number of vowels is: <span>$vocals</span></p>";
            if($treasure == true)
                {
                 print"<p><span>The number was guessed</span></p>";
                }
            else{
                print"<p><span>The number could not be guessed</span></p>";
            }
        print"</div>";
         }
         unset($_SESSION["submited"]); // Clear session so it doesn't show on reload
        ?>
    </main>
    <footer>
        <div>
            <span>Sebastian Taraguay</span>
        </div>
    </footer>
</body>
</html>