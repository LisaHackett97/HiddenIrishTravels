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

/* code for password confirm from this post
https://stackoverflow.com/questions/21727317/how-to-check-confirm-password-field-in-form-without-reloading-page
*/

$('#password, #confirm_password').on('keyup', function () {
    if ($('#password').val() == $('#confirm_password').val()) {
      $('#message').html('Passwords Match. Click register to continue').css('color', '#172A3A');
    } else 
      $('#message').html('Passwords do not Match').css('color', 'red');
  });