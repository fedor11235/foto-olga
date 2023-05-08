let enrollPopup
let close

document.addEventListener('DOMContentLoaded', handlerDOMContentLoaded)

function handlerDOMContentLoaded() {
  const like = document.getElementById('like')
  const enroll = document.getElementById('enroll')
  close = document.getElementById('close-contact')
  enrollPopup = document.getElementById('enroll-popup')
  like.addEventListener('click', hendlerSendingRequestLike)
  enroll.addEventListener('click', hendlerShowEnrollPopup)
  close.addEventListener('click', hendlerHideEnrollPopup)
}

function hendlerSendingRequestLike() {
  const Request = new XMLHttpRequest()
  Request.onreadystatechange = () => {
    if (Request.readyState == 4) window.location.reload()
  }
  Request.open('GET', '/add_like', true)
  Request.send()
}

function hendlerShowEnrollPopup() {
  enrollPopup.style.display='flex'
}

function hendlerHideEnrollPopup() {
  enrollPopup.style.display='none'
}


