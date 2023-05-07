let photoPopup

document.addEventListener('DOMContentLoaded', handlerDOMContentLoaded)

function handlerDOMContentLoaded() {
  const photos = document.getElementsByClassName('photo')
  const close = document.getElementById('close')
  for(const photo of photos){ 
    photo.addEventListener('click', handlerClickOnPhoto)
  }
  close.addEventListener('click', handlerClickOnClose)
}

function handlerClickOnPhoto(elem) {
  console.log(elem.target.style.backgroundImage)
  photoPopup = document.getElementById('photo-popup')
  photoPopup.style.display='flex'
}

function handlerClickOnClose() {
  photoPopup.style.display='none'
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