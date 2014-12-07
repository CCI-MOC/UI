function update() {

	if(!$('.modal').hasClass('act')) {
	$.ajax({
	  url: '',
	  success: function(data) {	
		$('body').html(data);
	  }
	});
	} else {
	}
}
setTimeout(update,5000)

$('.modal').on('hidden.bs.modal', function (e) {
	$('.modal').removeClass('act')
<<<<<<< HEAD
	setTimeout(update,1000)
=======
	setTimeout(update,5000)
>>>>>>> UI/master
})
$('.modal').on('show.bs.modal', function (e) {
	$(this).addClass('act')
})
<<<<<<< HEAD


=======
>>>>>>> UI/master
