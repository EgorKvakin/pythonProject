var episodeChoice = {
    seasons: ko.observableArray([]),
    series: ko.observableArray([]),
    episode: ko.observableArray([])
};
let episode = (evt) => {
   $.getJSON(`/get_data_series/`).then(data => {
        episodeChoice.series(data)
    });
}

elem = document.querySelectorAll("li")
for (i = 0; i < elem.length; i++) {
elem[i].addEventListener("click", episode, false);
}