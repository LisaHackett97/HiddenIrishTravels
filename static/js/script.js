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
    $(".tooltipped").tooltip();
    $('.modal').modal();
    $("select").formSelect();

       // jQuery Select validation from the Code Institute task manager mini-project
       validateMaterializeSelect();
       function validateMaterializeSelect() {
           let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
           let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
           if ($("select.validate").prop("required")) {
               $("select.validate").css({ "display": "none", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
           }
           $(".select-wrapper input.select-dropdown").on("focusin", function () {
               $(this).parent(".select-wrapper").on("change", function () {
                   if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                       $(this).children("input").css(classValid);
                   }
               });
           }).on("click", function () {
               if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                   $(this).parent(".select-wrapper").children("input").css(classValid);
               } else {
                   $(".select-wrapper input.select-dropdown").on("focusout", function () {
                       if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                           if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                               $(this).parent(".select-wrapper").children("input").css(classInvalid);
                           }
                       }
                   });
               }
           });
       }
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
