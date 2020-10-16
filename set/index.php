<?php

$id = filter_var($_GET['id'], FILTER_SANITIZE_STRING, FILTER_FLAG_STRIP_HIGH);
$chanList = filter_var($_GET['list'], FILTER_SANITIZE_STRING, FILTER_FLAG_STRIP_HIGH);

$file = fopen('../ids/' . $id, 'wb');

fwrite('../ids/' . $file, $chanList);

?>

<?php

echo $chanList;

?>