//This code is meant as a prototype to show how to grab data from the postgresql database.

  GNU nano 2.2.6                          File: prototype_1.php                                                            

<?php
$conn = pg_connect("host=forthepeople.cwjurl03ucof.us-west-2.rds.amazonaws.com port=5432 dbname=DSPeople user=webuser pass$
if (!$conn) {
        echo "an error occurred";
        exit;
}
$result = pg_query($conn, "SELECT * 
FROM (SELECT *
	FROM kill_floor.aiddata3_0
	LIMIT 1) aid_data
INNER JOIN kill_floor.country_information ctry_info
ON aid_data.donor_iso2 = ctry_info.country_iso2
INNER JOIN kill_floor.country_information ctry_info2
ON aid_data.recipient_iso2 = ctry_info.country_iso2;");
$arr = pg_fetch_all($result);
$output = json_encode($arr);
echo ("{aiddata:" . $output ."}");
?>