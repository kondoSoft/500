var pathArray = location.href.split('/')
var protocol = pathArray[0]
var host = pathArray[2]
var url = protocol + '//' + host + '/'

var data = new Array()

$(document).ready(function () {
  $('.question-answer-left-a.open-modal').on('click', function () {
    var question = $(this).html()
    var idReactivo = $(this).attr('id')
    var currentAnswer = $(this).attr('current-answer')
    var preguntaPk = $(this).attr('pk')

    $('#pregunta-pk').val(preguntaPk)
    $('#pregunta-modal').html(question)
    $('#modal1').modal()

    var respuestas = $('#respuestas-preguntas').val()
    respuestas = JSON.parse(respuestas)
    $('#respuestasSelect').html('')

    Object.keys(respuestas[idReactivo]).reverse().map(function (key, i) {
      var option = '<option value="'+respuestas[idReactivo][key]+'">'+key+'</option>'
      if (key == currentAnswer) {
        option = '<option value="'+respuestas[idReactivo][key]+'" selected>'+key+'</option>'
      }
      $('#respuestasSelect').append(option)
    })

  })

  $('#submit').on('click', function (e) {
    var respuestaId = $('#respuestasSelect').val()
    var questionText = $('#respuestasSelect option:selected').text()
    var preguntaId = $('#pregunta-pk').val()
    var evidencia = $('#url-evidencia').val()
    if (evidencia.length > 0) {
      $('#'+preguntaId).html(questionText)
      var question = {
        preguntaId: preguntaId,
        respuestaId: respuestaId,
        evidencia: evidencia
      }
      if (data.length > 0) {
        if (!isDuplicate(question, data)) {
          data = replaceItem(data, question)
        }
      } else {
        data.push(question)
      }
      $('#modal1').modal('hide')
    } else {
      $('#aviso-evidencia').fadeIn(300)
    }
  })

  $('#save-data').on('click', function () {
    $('#modal2').modal('show')
  })

  $('#modal2 #submit').on('click', function (e) {
    sendData(data)
  })
  $('#cancel').click(function () {
    result = confirm('Quiere cancelar los cambios?')
    if (result) {
      window.location.reload()  
    }
  })
  $('#modal1').on('hide.bs.modal', function () {
    $('#url-evidencia').val('')
    $('#aviso-evidencia').css('display', 'none')
  })
})

function isDuplicate (question, array) {
  var isDuplicate = array.some(function (item) {
    return question.preguntaId == item.preguntaId && question.respuestaId == item.respuestaId
  })
  
  return isDuplicate
}

function replaceItem (array, item) {
  var result = []
  Object.keys(array).map(function (key, i) {
    if (array[key].preguntaId == item.preguntaId) {
      array.splice(i, i+1)
      array.push(item)
      result = array
    } else {
      array.push(item)
      result = array
    }
  })
  return result
}

function sendData (questions) {
  var csrftoken = getCookie('csrftoken');
  var datos = JSON.stringify(questions)
  $.ajax({
    url: url+'empresa/',
    headers: {
        'X-CSRFToken': csrftoken,
        'Content-Type':'application/json'
    },
    method: 'POST',
    dataType: 'json',
    data: datos,
    success: function(data){
      if (data['ok']) {
        window.location.reload()
        window.scrollTo(0, 0)
      }
    }
  });
  $('#modal2').modal('hide')
}


function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
  var cookies = document.cookie.split(';');
  for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
      }
    }
  }
  return cookieValue;
}
