/*jshint esversion: 6 */
/*globals $:false */

// variables to set 
let mybutton = document.getElementById("backToTopBtn");
jQuery.event.special.touchstart = {
  setup: function( _, ns, handle ){
    if ( ns.includes("noPreventDefault") ) {
      this.addEventListener("touchstart", handle, { passive: false });
    } else {
      this.addEventListener("touchstart", handle, { passive: true });
    }
  }
};

// Doc ready functions, including jquery materialize code Credit CI Tutorial
$(document).ready(function () {

  $(".dropdown-trigger").dropdown({
    coverTrigger: false
  });

  $('.sidenav').sidenav({
    edge: "right"
  });
  $('.collapsible').collapsible();
  $(".tooltipped").tooltip();
  $('.modal').modal();
  $("select").formSelect();
  $('.parallax').parallax();
  $('#location-collection').hide();
  $('#visitor-collection').hide();
  $("#location-view-btn").click(function () {
    $("#location-collection").toggle();
  });
  $("#visitor-view-btn").click(function () {
    $("#visitor-collection").toggle();
  });
  $('.search-container').hide();

  $("#home-search-button").click(function () {
    $(".search-container").toggle();
  });
// to fade out flash message
  $('#flash-msg-close').click(function(){
    $('.flashes').fadeOut(1200);
  });

  // Code for form validation taken from CI Task manager tutorial 
    validateMaterializeSelect();
    function validateMaterializeSelect() {
             let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };      
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
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
// End of doc ready function


/* code for password confirm from this post
https://stackoverflow.com/questions/21727317/how-to-check-confirm-password-field-in-form-without-reloading-page
*/
$('#confirm_password').on('keyup', function () {
  if ($('#password').val() == $('#confirm_password').val()) {
    $('#message').html('Passwords Match. Click register to continue').css('color', '#172A3A');
    $('#register-btn').prop('disabled', false);
  } else {
    $('#message').html('Passwords do not Match').css('color', 'red');
    $('#register-btn').prop('disabled', true);
  }
});

// Function to allow user to clear the Add New form. Triggered with onclick 
function resetAddForm() {
  document.getElementById('add-new-form').reset();
}

// applies to search on home and user pages
function hideSearchForm() {
  document.getElementById('search-form').reset();
  $(".search-container").hide();
}

// js code for search box on users list. Acts as a filter. 
// Found on stack overflow post
// http://jsfiddle.net/JeroenSormani/xhpkfwgd/1/
var $rows = $('#table tr');
$('#search').keyup(function () {
  var val = $.trim($(this).val()).replace(/ +/g, ' ').toLowerCase().split(' ');

  $rows.hide().filter(function () {
    var text = $(this).text().replace(/\s+/g, ' ').toLowerCase();
    var matchesSearch = true;
    $(val).each(function (index, value) {
      matchesSearch = (!matchesSearch) ? false : ~text.indexOf(value);
    });
    return matchesSearch;
  }).show();
});

// Code for back to top icon from a tutorial
// https://www.w3schools.com/howto/howto_js_scroll_to_top.asp


// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction();
};

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

// Upload widget from Cloudinary docs
// image success info is sent to the console log per the docs
// admin can access this here
var myWidget = cloudinary.createUploadWidget({
  cloudName: 'dc9rijkkz',
  uploadPreset: 'mcuus0xs'
}, (error, result) => {
  if (!error && result && result.event === "success") {
    console.log('Done! Here is the image info: ', result.info);
  }
});
document.getElementById("upload_widget").addEventListener("click", function () {
  myWidget.open();
}, false);


// jQuery.event.special.touchmove = {
//   setup: function( _, ns, handle ){
//     if ( ns.includes("noPreventDefault") ) {
//       this.addEventListener("touchmove", handle, { passive: false });
//     } else {
//       this.addEventListener("touchmove", handle, { passive: true });
//     }
//   }
// };

document.addEventListener(document, "touchmove", function(e) {
  console.log(e.defaultPrevented);  // will be false
  e.preventDefault();   // does nothing since the listener is passive
  console.log(e.defaultPrevented);  // still false
}, Modernizr.passiveeventlisteners ? {passive: true} : false);