$(document).ready(function() {
   //Our on page ready functions
   
   $('#checkout-btn').click( function(e) {
      e.preventDefault();
      $('#checkout-btn').attr('disabled', true);
      $('#alert').append('<div class="container-fluid text-center alert alert-primary">You have no items in your cart!</div>');
      return true;
   });
   
   

	if(localStorage.getItem('msgState') != 'shown') {
  	$('#myAlert').slideDown('slow');
    localStorage.setItem('msgState', 'shown');
  }
  $('.close').click(function(e){
  	$('#myAlert').slideUp('slow');
  }); //End of click event


   
   
});