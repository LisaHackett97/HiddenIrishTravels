/*jshint esversion: 6 */
/*globals $:false */

let contactForm = document.getElementById("contact-form");

function sendMail(contactForm) {
    emailjs.send("service_fhjfpgq", "contactForm", {
            to_name: "Lisa",
            from_name: contactForm.name.value,
            from_email: contactForm.email.value,
            message: contactForm.message.value
        })
        .then(
            function (response) {
                $('#emailModal').show();
            },
            function (error) {
                confirm("We're sorry, your message couldn't be sent at this time", error);
            }
        );
    return false; //to block from loading a new page
}

// function to clear from. called when close button on email confirmation button selected
function clearForm() {
    document.getElementById("contact-form").reset();
}