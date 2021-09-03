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
    $("select").formSelect();
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
  
// Function to allow user to clear the Add New form. Triggered with onclick 
  function resetAddForm(){
      document.getElementById('add-new-form').reset();
  }

