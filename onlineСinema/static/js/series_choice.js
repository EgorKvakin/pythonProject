var seasonChoice = {
    season: ko.observableArray([])
};
let episode = (evt) => {
    let url = evt.target.getAttribute('data-href')
    console.log(url)
    $.getJSON(url).then(data => {
        episodeChoice.episode(data)
    });
    console.log(episodeChoice.episode)
}

elem = document.querySelectorAll("li.episode")
for (i = 0; i < elem.length; i++) {
elem[i].addEventListener("click", episode, false);
}