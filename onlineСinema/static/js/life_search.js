var viewModel = {
    films: ko.observableArray([]),
    series: ko.observableArray([]),
    film: ko.observableArray([])
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
ko.applyBindings(viewModel);
