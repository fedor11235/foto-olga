document.addEventListener('DOMContentLoaded', handlerDOMContentLoaded)

function handlerDOMContentLoaded() {
  const openFormButton = document.getElementById('open-form-button')
  openFormButton.addEventListener('click', hendlerShowEnrollPopup)
}

function hendlerShowEnrollPopup() {
  enrollPopup.style.display='flex'
}

