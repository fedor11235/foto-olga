document.addEventListener('DOMContentLoaded', handlerDOMContentLoaded)

function handlerDOMContentLoaded() {
  const like = document.getElementById('like')
  like.addEventListener('click', hendlerSendingRequestLike)
}

function handlerClickLike() {

}

function hendlerSendingRequestLike() {
  const Request = new XMLHttpRequest()
  Request.onreadystatechange = () => {
    if (Request.readyState == 4) window.location.reload()
  }
  Request.open('GET', '/add_like', true)
  Request.send()
}

