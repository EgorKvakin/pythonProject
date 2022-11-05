var ViewModel = {
    film_title: ko.observable(''),
    film_preview: ko.observable(''),
    pk: ko.observable(),
};
$.getJSON("/search/",function(data){

})
let elements = document.querySelectorAll('div.d-inline-flex.observable');
$("#search").on("keyup", function() {

})
ko.applyBindings(ViewModel);
