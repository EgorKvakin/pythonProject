var ViewModel = {
    films: ko.ko.observableArray([]),
    series: ko.observableArray([]),
};
$("#search").on("keyup", function() {
    $.getJSON("/search/",function(data){
    ViewModel.films = data.films
    ViewModel.series = data.series
})
})
ko.applyBindings(ViewModel);
