$(document).ready(function() {
  $(":input").inputmask();
  $("#phone").inputmask({"mask": "(999) 999-9999"});

  $('#payment-form').hide();
  $('#new-card-msg').hide();

//slide down the payment form
  $("#add-new-card-button").click(function() {
    $("#payment-form").slideDown(1000);
    $("#new-card-msg").fadeIn(1000);
  });

  $("#cancel-button").click(function() {
    $("#payment-form").slideUp(4000);
  });


  var min = new Date().getFullYear(),
      max = min + 20,
      select = document.getElementById('exp_year');

  for (var i = min; i<=max; i++){
      var opt = document.createElement('option');
      opt.value = i;
      opt.innerHTML = i;
      select.appendChild(opt);
  }



});
