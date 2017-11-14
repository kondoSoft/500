var modal = document.getElementById('modal-background')
var modalContent = document.getElementById('modal-content')
var btnClose = document.getElementById('close-modal')

var acceptButtons = document.getElementsByClassName('reject')

for (var i = 0; i < acceptButtons.length; i++) {
  acceptButtons[i].addEventListener('click', onAccept)
}

btnClose.addEventListener('click', onClose)

function onAccept (e) {
  if (modal.classList.contains('close-modal')) {
    modal.classList.remove('close-modal')
  }
  var height = modalContent.offsetHeight / 2
  console.log('height>>', height)
  modal.classList.add('open-modal')
  console.log(e)
  modalContent.style.top = (e.pageY - height) + 'px'
  // window.scrollTo(0, (e.pageY/2) + 100)
  // document.getElementsByTagName('body')[0].style.overflow = 'hidden'
}

function onClose (e) {
  modal.classList.remove('open-modal')
  modal.classList.add('close-modal')
  document.getElementsByTagName('body')[0].style.overflow = 'initial'
}
