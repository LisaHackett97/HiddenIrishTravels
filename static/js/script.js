// function to clear registration form 
// window.onload = function() {
//     document.getElementById("register_form").reset();
  
// }
/*
doc ready functions, including  materialize validate
*/
$(document).ready(function () {
    $(".dropdown-trigger").dropdown({
        coverTrigger: false});
    $('.sidenav').sidenav({
        edge: "right" });
    $('.collapsible').collapsible();
    $(".tooltipped").tooltip();
    $('.modal').modal();
    $("select").formSelect(); 

    $("#location-view-btn").click(function () {
        $("#location-collection").toggle()
        });
    $("#visitor-view-btn").click(function () {
        $("#visitor-collection").toggle()
        });

    
    $('.search-container').hide();
    $("#home-search-button").click(function(){
        $(".search-container").toggle(); 
            })
  
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

// applies to search on home and user pages
function hideSearchForm() {
    document.getElementById('search-form').reset();
    $(".search-container").hide();
}

// js code for search box onusers. Found on stack overflow post
// http://jsfiddle.net/JeroenSormani/xhpkfwgd/1/
var $rows = $('#table tr');
$('#search').keyup(function() {
  var val = $.trim($(this).val()).replace(/ +/g, ' ').toLowerCase().split(' ');

  $rows.hide().filter(function() {
    var text = $(this).text().replace(/\s+/g, ' ').toLowerCase();
    var matchesSearch = true;
    $(val).each(function(index, value) {
      matchesSearch = (!matchesSearch) ? false : ~text.indexOf(value);
    });
    return matchesSearch;
  }).show();
});

// Code for back to top icon from a tutorial
// https://www.w3schools.com/howto/howto_js_scroll_to_top.asp

mybutton = document.getElementById("backToTopBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
