var pathArray = location.href.split('/')
var protocol = pathArray[0]
var host = pathArray[2]
var url = protocol + '//' + host + '/'

$(document).ready(function (){
  $('.question-answer-left-a').on('click', function (){
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

    Object.keys(respuestas[idReactivo]).reverse().map(function (key,i) {
      var option = '<option value="'+respuestas[idReactivo][key]+'">'+key+'</option>'
      if (key == currentAnswer) {
        console.log(key)
        option = '<option value="'+respuestas[idReactivo][key]+'" selected>'+key+'</option>'
      }
      $('#respuestasSelect').append(option)
    })

  })

  $('#submit').on('click', function (){
    $('#change-answer').submit()
  })
})
