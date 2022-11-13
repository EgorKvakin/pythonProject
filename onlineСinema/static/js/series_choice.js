var episodeChoice = {
    seasons: ko.observableArray([]),
    series: ko.observableArray([]),
    episode: ko.observableArray([])
};
let episode = (evt) => {
   var episode = evt.target.getAttribute('episode_id');
   var season = evt.target.getAttribute('season_id');
   var series_id = evt.target.getAttribute('series_id')
   var default_season = evt.target.getAttribute('default_season')
   var default_episode = 1
   console.log(series_id)
   $.getJSON(`/get_data_series/`).then(data => {
        episodeChoice.series(data)
    });
    episodeChoice.series(episodeChoice.series().filter(item => item.id.search(series_id) != -1));
    console.log(episodeChoice.series(episodeChoice.series().filter(item => item.id == series_id)));
}

elem = document.querySelectorAll("li")
for (i = 0; i < elem.length; i++) {
elem[i].addEventListener("click", episode, false);
}