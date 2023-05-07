document.addEventListener("DOMContentLoaded", handlerDOMContentLoaded)

function handlerDOMContentLoaded() {
  console.log('page loaded successfully')
}

function sendingRequestToServer(method, url) {
  const Request = new XMLHttpRequest()
  Request.open(method, url, true)
  // Request.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8')
  Request.onreadystatechange = () => {
    if (Request.readyState == 4) {
      console.log('sending to the server was successful')
    }
  }
  Request.send()
}