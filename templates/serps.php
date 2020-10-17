<?php
$top = '<div class="container"><h1 class="tc grey">' . $contentTitle . '</h1>';
$middle = '
<link href="' . $host . '/google.css" rel="stylesheet">
<link href="' . $host . '/google-hard.css" rel="stylesheet">
<div class="row">
<div class="form">
	<form class="sim" id="sim">
		<input type="text" id="sq" name="sq" value="Search Queries"></input>
		<input type="text" id="url" name="url" value="liamanderson.co.uk"></input>
		<input type="text" id="title" name="title" value="Liam Anderson - Profile, Portfolio and Project"></input>
		<textarea id="description" name="description" value="Liam Anderson Full-Stack Web developer | Lancashire, Lancaster">Liam Anderson Full-Stack Web developer | Lancashire, Lancaster</textarea>
		<input type="submit" name="submit" id="submit" value="goooogle.."></input>
	</form>
</div>
<div class="google">
	<cite>liamanderson.co.uk</cite>
	<h3>Liam Anderson - Profile, Portfolio and Project</h3>
	<p class="d">Liam Anderson Full-Stack Web developer | Lancashire, Lancaster</p>
</div>
</div>
';
$bottom = '</div>';

$templateOutput = $top . $middle . $bottom;

?>
