/*
jquery for materialize
*/

$(document).ready(function () {
    $(".dropdown-trigger").dropdown({
        coverTrigger: false
    });
    $('.sidenav').sidenav({
        edge: "right"
    });
    $(".collapsible").collapsible();
});