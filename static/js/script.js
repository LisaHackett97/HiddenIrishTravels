// function to clear registration form 
window.onload = function() {
    document.getElementById("register_form").reset();
    }

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
$('#confirm_password').on('keyup', function () {
    if ($('#password').val() == $('#confirm_password').val()) {     
      $('#message').html('Passwords Match. Click register to continue').css('color', '#172A3A');
      $('#register-btn').prop('disabled', false);
    } else {
      $('#message').html('Passwords do not Match').css('color', 'red');
      $('#register-btn').prop('disabled', true);}
  });

// This code gives msg when switching between pageXOffset, not on brower window close
//   window.onbeforeunload = function (e) {
//     e = e || window.event;

//     // For IE and Firefox prior to version 4
//     if (e) {
//         e.returnValue = 'Sure?';
//     }

//     // For Safari
//     return 'Sure?';
// };


window.onbeforeunload = confirmExit;
function confirmExit(){
    alert("confirm exit is being called");
    return false;
}
