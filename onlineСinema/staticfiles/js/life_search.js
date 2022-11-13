var viewModel = {
    films : ko.observableArray([]);
};
$.getJSON(`/get_data/`).then(data => {
    viewModel.films(data)
})
ko.applyBindings(viewModel);
