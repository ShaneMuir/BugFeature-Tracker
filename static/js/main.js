$(document).ready(function() {
   //Our on page ready functions
   
   $('#checkout-btn').click( function(e) {
      e.preventDefault();
      $('#checkout-btn').attr('disabled', true);
      $('#alert').append('<div class="container-fluid text-center alert alert-primary">You have no items in your cart!</div>');
      return true;
   });
   
   
   
});