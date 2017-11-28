var modal = document.getElementById('modal-background')
var modalContent = document.getElementById('modal-content')
var btnClose = document.getElementById('close-modal')

var acceptButtons = document.getElementsByClassName('reject')

for (var i = 0; i < acceptButtons.length; i++) {
  acceptButtons[i].addEventListener('click', onReject)
}

btnClose.addEventListener('click', onClose)

function onReject (e) {
  if (modal.classList.contains('close-modal')) {
    modal.classList.remove('close-modal')
  }
  var preguntaPk = e.currentTarget.getAttribute('pk')
  $('#question-pk').val(preguntaPk)
  var height = modalContent.offsetHeight / 2
  modal.classList.add('open-modal')
  modalContent.style.top = (e.pageY - height) + 'px'
  var value = window.scrollY
  var interval = setInterval(function(){
    var up, down
    if (value <= e.pageY - 400) {
      up = true
      value += 5
    } else {
      down = true
      value -= 5
    }
    if (value >= e.pageY - 400 && up) {
      up = false
      clearInterval(interval)
    }
    if (value <= e.pageY - 400 && down) {
      down = false
      clearInterval(interval)
    }
    window.scrollTo(0, value)
    
  },60/1000)
  document.getElementsByTagName('body')[0].style.overflow = 'hidden'
}

function onClose (e) {
  e.preventDefault()
  modal.classList.remove('open-modal')
  modal.classList.add('close-modal')
  document.getElementsByTagName('body')[0].style.overflow = 'initial'
}


$(document).ready(function (){
  $('#id_respuestaPersonalizada').attr('disabled', 'false')
  $('#id_comentarios').attr('disabled', 'false')
  $('#id_respuestaPersonalizada').css('background', '#ECF1F1')
  $('#id_comentarios').css('background', '#ECF1F1')
  $('#id_motivo').on('change', function (e){
    var value = e.currentTarget.value
    if (value != 4) {
      $('#id_respuestaPersonalizada').attr('disabled', 'true')
      $('#id_comentarios').attr('disabled', 'true')
      $('#id_respuestaPersonalizada').css('background', '#ECF1F1')
      $('#id_comentarios').css('background', '#ECF1F1')
    } else {
      $('#id_respuestaPersonalizada').removeAttr('disabled')
      $('#id_comentarios').removeAttr('disabled')
      $('#id_respuestaPersonalizada').css('background', '#FFF')
      $('#id_comentarios').css('background', '#FFF')
    }
  })
  $('.accept').click(function (){
    $('#modalAccept').modal()
    var idPregunta = $(this).attr('pk')
    $('#pregunta-pk').val(idPregunta)
    $('#status').val('1')
    console.log(idPregunta)
  })
  $('.submit').click(function (){
    $('#accept-question').submit()
  })
})