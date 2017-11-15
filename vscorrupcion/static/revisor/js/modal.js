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
  // window.scrollTo(0, e.pageY)
  // document.getElementsByTagName('body')[0].style.overflow = 'hidden'
}

function onClose (e) {
  e.preventDefault()
  modal.classList.remove('open-modal')
  modal.classList.add('close-modal')
  document.getElementsByTagName('body')[0].style.overflow = 'initial'
}


$(document).ready(function (){
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