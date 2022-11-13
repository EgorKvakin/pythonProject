let active = (evt) => {
   document.querySelector("li.nav-item.active").classList.remove("active")
   evt.target.closest("li.nav-item").classList.add("active")
}
elem = document.querySelectorAll("li.nav-item")
for (i = 0; i < elem.length; i++) {
elem[i].addEventListener("click", active, false);
}
