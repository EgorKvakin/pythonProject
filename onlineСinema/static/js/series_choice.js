console.log("Hello world!");
let activated = (evt) => {
   let attrValue = evt.target.getAttribute('episode_id');
   console.log(attrValue)
   let elements = document.querySelectorAll("source")
   let activeElem = document.querySelector('source[active="True"]')
   console.log(activeElem)
   console.log(elements)
   for(i = 0; i < elements.length; i++){
     console.log(elements[i])
     if(elements[i].getAttribute('episode_id') == attrValue && elements[i] != activeElem){
        activeElem.setAttribute('active', 'False')
        elements[i].setAttribute('active', 'True')
        activeElem.replaceWith(elements[i])
     }
   }
}
elem = document.querySelectorAll("li")
for (i = 0; i < elem.length; i++) {
elem[i].addEventListener("click", activated, false);
}