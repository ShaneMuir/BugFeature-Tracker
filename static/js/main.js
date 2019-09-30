$(document).ready(function() {
   //Our on page ready functions
   
   $('#checkout-btn').click( function(e) {
      e.preventDefault();
      $('#checkout-btn').attr('disabled', true);
      $('#alert').append('<div class="container-fluid text-center alert alert-primary">You have no items in your cart!</div>');
      return true;
   });
   
   

	if(localStorage.getItem('featureMsgState') != 'shown') {
  	$('#featureAlert').slideDown('slow');
    localStorage.setItem('featureMsgState', 'shown');
  }
  $('.close').click(function(e){
  	$('#featureAlert').slideUp('slow');
  }); //End of click event
   
   
});