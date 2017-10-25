var pathArray = location.href.split('/')
var protocol = pathArray[0]
var host = pathArray[2]
var url = protocol + '//' + host + '/'

$(document).ready(function () {
	$ ('.preguntas').tooltip()
	$('.preguntas').on('click', function (e) {
		e.preventDefault()
		var id = $(this).attr('data-id')
		$('#pregunta_id').val(id)

		$.ajax(url + 'modify-answer/' + id)
		.done(function (response) {
			var res = parseInt(response)
			if (!isNaN(res) && response.length < 4) {
				var element = `
					  <select name="respuesta" id="respuesta">
              <option value="1">Si</option>
              <option value="0">No</option>
              <option value="0.5">Únicamente respecto a la Ley de Protección de Datos Personales /Derechos ARCO</option>
            </select>
				`
				$('#respuesta').remove()
				$('#edit-answer>div').append(element)
				$('#respuesta').val(response)
			} else {
				$('#respuesta').remove()
				$('#edit-answer>div').append('<textarea name="respuesta" id="respuesta" cols="60" rows="5" style="display:block;"></textarea>')
				$('#respuesta').val(response)
			}
		})

	})

	$('#submit').on('click', function () {
		$('#edit-answer').submit()
	})
})