$( document ).ready(function() {
	$('.delVM').click(function() {
		console.log("shishis")
		console.log($(this))
		var name = "my-seriver"
                $.get('delete/'+name+'/', function (data) {
                });
	})
})
