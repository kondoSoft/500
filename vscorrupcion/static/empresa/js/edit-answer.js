var pathArray = location.href.split( '/' );
var protocol = pathArray[0];
var host = pathArray[2];
var url = protocol + '//' + host+'/';

$(document).ready(function(){
	$('.preguntas').tooltip()
	$('.preguntas').on('click', function (e) {
		e.preventDefault()
		var id = $(this).attr('data-id')
		$('#pregunta_id').val(id)

		$.ajax(url+'modify-answer/'+id)
		.done(function(response){
			$('#respuesta').val(response)
		})

	})

	$('#submit').on('click', function(){
		$('#edit-answer').submit()
	})
})