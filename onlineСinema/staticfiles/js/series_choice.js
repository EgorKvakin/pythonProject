console.log("Hello world!");
let active = (evt) => {
   let attrValue = evt.target.getAttribute('episode_id')
   console.log(attrValue)
   let elements = document.querySelectorAll("video.video-js")
   for(elem in elements){
     console.log(elem)
     if(elem.getAttribute('episode_id') == attrValue){
        elem.removeAttribute("hidden")
     }
   }
}
elem = document.querySelectorAll("li")
for (i = 0; i < elem.length; i++) {
elem[i].addEventListener("click", active, false);
}