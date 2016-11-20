<?php
$conn = pg_connect("host=forthepeople.cwjurl03ucof.us-west-2.rds.amazonaws.com port=5432 dbname=DSPeople user=webuser pass$
if (!$conn) {
        echo "an error occurred";
        exit;
}
$result = pg_query($conn, "SELECT country
FROM kill_floor.aiddata3_0;");
$arr = pg_fetch_all($result);
$output = json_encode($arr);
echo ("{aiddata:" . $output ."}");
?>