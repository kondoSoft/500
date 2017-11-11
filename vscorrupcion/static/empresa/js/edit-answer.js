var pathArray = location.href.split('/')
var protocol = pathArray[0]
var host = pathArray[2]
var url = protocol + '//' + host + '/'

$(document).ready(function (){
	$('.question-answer-left-a').on('click', function (){
		var question = $(this).html()
		var idReactivo = $(this).attr('id')
		$('#pregunta-modal').html(question)
		$('#modal1').modal()
		var respuestas = $('#respuestas-preguntas').val()
		respuestas = JSON.parse(respuestas)
		$('#respuestasSelect').html('')
		Object.keys(respuestas[idReactivo]).map(function (key,i) {
			$('#respuestasSelect').append('<option value="'+respuestas[idReactivo][key]+'">'+key+'</option>')
		})
	})
})
