<?php 
$top = '<div class="container">' . $contentTitle . '</h1>';
$middle = '';
$i = 1;
while($i <= count($xml->cta)){
	$o = $i-1;
	$middle .= '<div class="row">
						<a href="' . $xml->panel[$o]->pURL . '">
							<div class="project lighttealbg">
								<div class="pimg darktealbg">
									<img src="' . $host . '/IMAGES/' . $xml->panel[$o]->pImage . '" class="coverimg">
								</div>
								<h3 class="navy">' . $xml->panel[$o]->pTitle . '</h3>
								<p class="navy">' . $xml->panel[$o]->pDescription . '</p>
							</div>
						</a>
					</div>';
	$i ++;			
}
$bottom = '</div></div></div>';

$templateOutput = $top . $middle . $bottom;
	
?>