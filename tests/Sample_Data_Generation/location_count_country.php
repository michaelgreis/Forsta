<?php
$conn = pg_connect("host=forthepeople.cwjurl03ucof.us-west-2.rds.amazonaws.com port=5432 dbname=DSPeople user=webuser pass$
if (!$conn) {
        echo "an error occurred";
        exit;
}
$result = pg_query($conn, "SELECT *
FROM (
SELECT * FROM kill_floor.nytimeslocations LIMIT 20) location_count
INNER JOIN (SELECT * FROM kill_floor.country_information LIMIT 20) ctry_info
ON location_count.country = location_count.country;");
$arr = pg_fetch_all($result);
$output = json_encode($arr);
echo ("{aiddata:" . $output ."}");
?>