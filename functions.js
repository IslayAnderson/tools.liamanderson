
var replaceSrc = function () {
	x = document.getElementsByClassName('lazy-load-me');
	for (i = 0; i < x.length; i++){
		if (x[i].getBoundingClientRect().top < window.innerHeight) {
			img = x[i]
			if(window.innerWidth < 850 && x[i].getAttribute('mobi-src') != null){
				lazySRC = x[i].getAttribute('mobi-src');
			}else{
				lazySRC = x[i].getAttribute('desk-src');
			}
			if(x[i].tagName == 'VIDEO'){
				x[i].canPlayType("video/mp4");
				x[i].src = lazySRC;
				x[i].load();
				x[i].onload = x[i].play();
				x[i].classList.remove("lazy-load-me");
        x[i].classList.add("fade-in");
			}else{
				x[i].src = lazySRC;
				x[i].classList.remove("lazy-load-me");
        x[i].classList.add("fade-in");
			}
		}
	}
};
replaceSrc();
window.addEventListener('scroll', replaceSrc, false);
if(document.title.split('serps') > -1){
	sq = document.getElementsByName('sq');
	url = document.getElementsByName('url');
	title = document.getElementsByName('title');
	description = document.getElementsByName('description');
	submit = document.getElementsByName('submit');
	pCite = document.querySelector("div.g > div > cite");
	pH3 = document.querySelector("div.g > div > h3");
	pP = document.querySelector("div.g > div > p");

	url[0].onkeyup = function(){
		pCite.innerHTML = url[0].value;
		if(checkOverflow(pCite)){
			pCite.style.color = "red";
		}
	};
	title[0].onkeyup = function(){
		pH3.innerHTML = title[0].value;
		if(checkOverflow(pH3)){
			pH3.style.color = "red";
		}
	};
	description[1].onkeyup = function(){
		pP.innerHTML = description[1].value;
		if(checkOverflow(pP)){
			pP.style.color = "red";
		}
	};
}

function checkOverflow(elem) {
	elem.style.overflow = 'visible';
	elemHeight = elem.clientHeight;
	scrollHeight = elem.scrollHeight;
	elem.style.overflow = 'hidden';
	return elemHeight < scrollHeight
}
