document.addEventListener("click",() => {
   elem = document.querySelectorAll("li.nav-item")
   elem.classList.add("active")
   console.log(elem)
});