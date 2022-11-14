var viewModel = {
    films: ko.observableArray([]),
    series: ko.observableArray([]),
    film: ko.observableArray([]),
    episode: ko.observable()
};
$.getJSON(`/get_data_films/`).then(data => {
    viewModel.films(data)
});
$.getJSON(`/get_data_series/`).then(data => {
    viewModel.series(data)
});
$(document).ready(function(){
  $("#search").on("keyup", function() {
        let val = $(this).val().toLowerCase();
        if (val != ''){
            viewModel.films(viewModel.films().filter(item => item.film_title.toLowerCase().search(val) != -1 ));
            viewModel.series(viewModel.series().filter(item => item.series_title.toLowerCase().search(val) != -1 ));
        }
        else {
            $.getJSON(`/get_data_films/`).then(data => {
                viewModel.films(data)
            });
            $.getJSON(`/get_data_series/`).then(data => {
                viewModel.series(data)
            });
        }
  })
})
let episode = (evt) => {
    let url = evt.target.getAttribute('data-href')
    console.log(url)
    $.getJSON(url).then(data => {
        viewModel.episode(data)
    });
    videoNode = videojs('my-video');
    videoNode.load()
}

elem = document.querySelectorAll("li.episode")
for (i = 0; i < elem.length; i++) {
elem[i].addEventListener("click", episode, false);
}
ko.applyBindings(viewModel);
