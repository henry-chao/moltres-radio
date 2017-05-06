function validateAndSubmit(){
  var password = $("#password");
  var verify_password = $("#verify_password");
  var registrationForm = $("#registrationForm");

  if( password.val() != verify_password.val() ){
    verify_password.removeClass("valid");
    verify_password.addClass("invalid");
    Materialize.toast('Passwords do not match', 4000);
  } else {
    if( registrationForm[0].checkValidity() ){
      registrationForm.submit();
    } else {
      Materialize.toast('Form incomplete!', 4000);
    }
  }
};
