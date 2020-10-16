<?php
$top = '<div class="container"><h1 class="tc grey">' . $contentTitle . '</h1>' . $xml->intro . '';
$middle = '';
$i = 1;
while($i <= count($xml->panel)){
	$o = $i-1;
	if($i == count($xml->panel) && $i % 2 != 0){
		$middle .= '<div class="row">
						<a href="' . $xml->panel[$o]->pURL . '">
							<div class="project lighttealbg">
								<div class="pimg lighttealbg">
									<iframe desk-src="' . $xml->panel[$o]->pURL . '" scrolling="no" class="lazy-load-me"></iframe>
								</div>
								<h3 class="navy">' . $xml->panel[$o]->pTitle . '</h3>
								<p class="navy">' . $xml->panel[$o]->pDescription . '</p>
							</div>
						</a>
					</div>';
	}else if($i % 2 != 0){
		$middle .= '<div class="row">
						<a href="' . $xml->panel[$o]->pURL . '">
							<div class="project lighttealbg">
								<div class="pimg lighttealbg">
									<iframe desk-src="' . $xml->panel[$o]->pURL . '" scrolling="no" class="lazy-load-me"></iframe>
								</div>
								<h3 class="navy">' . $xml->panel[$o]->pTitle . '</h3>
								<p class="navy">' . $xml->panel[$o]->pDescription . '</p>
							</div>
						</a>';
	}else{
		$middle .= '<a href="' . $xml->panel[$o]->pURL . '">
						<div class="project lighttealbg">
							<div class="pimg lighttealbg">
								<iframe desk-src="' . $xml->panel[$o]->pURL . '" scrolling="no" class="lazy-load-me"></iframe>
							</div>
							<h3 class="navy">' . $xml->panel[$o]->pTitle . '</h3>
							<p class="navy">' . $xml->panel[$o]->pDescription . '</p>
						</div>
					</a>
				</div>';
	}
	$i ++;
}
$bottom = '</div>';

$templateOutput = $top . $middle . $bottom;

?>
