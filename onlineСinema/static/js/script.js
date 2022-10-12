let active = (evt) => {
   document.querySelector("li.nav-item.active").classList.remove("active")
   evt.target.closest("li.nav-item").classList.add("active")
}
elem = document.querySelectorAll("li.nav-item")
for (i = 0; i < elem.length; i++) {
elem[i].addEventListener("click", active, false);
}

jQuery(function() {
    $("#id_input").on('keyup', function(){
        var value = $(this).val();
        $.ajax({
            url: "{% url 'ajax_autocomplete' %}",
            data: {
              'search': value
            },
            dataType: 'json',
            success: function (data) {
                list = data.list;
                $("#id_input").autocomplete({
                source: list,
                minLength: 3
                });
            }
        });
    });
  });
