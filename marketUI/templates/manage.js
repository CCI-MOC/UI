console.log("manage.js loaded")
$( document ).ready(function() {
	$('.delVM').click(function() {
		console.log("shishis")
		console.log($(this))
		var name = "my-seriver"
                $.get('delete/'+name+'/', function (data) {
                });
	})
})


function update() {

	if(!$('.modal').hasClass('act')) {
	$.ajax({
	  url: '',
	  success: function(data) {	
		console.log('fresh')
		$('body').html(data);
	  }
	});
	} else {
	console.log('modalopen')
	}
}
setTimeout(update,5000)

$('.modal').on('hidden.bs.modal', function (e) {
	$('.modal').removeClass('act')
	console.log('hide')
	setTimeout(update,1000)
})
$('.modal').on('show.bs.modal', function (e) {
	console.log('show')
	$('.modal').addClass('act')
})

$('.vnc').click(function() {
	console.log("hihihi")
})

