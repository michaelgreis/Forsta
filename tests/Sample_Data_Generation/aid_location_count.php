<?php
$conn = pg_connect("host=forthepeople.cwjurl03ucof.us-west-2.rds.amazonaws.com port=5432 dbname=DSPeople user=webuser pass$
if (!$conn) {
        echo "an error occurred";
        exit;
}
$result = pg_query($conn, "SELECT *
FROM (
SELECT *
FROM kill_floor.aiddata3_0
LIMIT 1) aid_data
INNER JOIN (SELECT * FROM kill_floor.nytimeslocations LIMIT 20) location_count
on aid_data.recipient_iso2 = location_count.country;");
$arr = pg_fetch_all($result);
$output = json_encode($arr);
echo ("{aiddata:" . $output ."}");
?>