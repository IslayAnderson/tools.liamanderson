
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
