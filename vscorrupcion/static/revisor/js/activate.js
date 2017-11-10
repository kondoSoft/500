$(document).ready(function (){
  $('.activate').on('click', function (e){
    var id = $(this).attr('data-user-id')
    var email = $(this).attr('data-user-email')
    $('#user-id').val(id)
    $('#user-email').val(email)
    $('#accept-modal').modal()
  })

  $('#update-user').on('click', function (e){    
    $('#accept-modal').modal('hide')
    $('#update-user-status').submit()
  })
})