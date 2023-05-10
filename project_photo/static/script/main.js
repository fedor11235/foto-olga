let photoPopup
let photoOrigin

document.addEventListener('DOMContentLoaded', handlerDOMContentLoaded)

function handlerDOMContentLoaded() {
  const photos = document.getElementsByClassName('photo')
  const close = document.getElementById('close-photo')
  photoPopup = document.getElementById('photo-popup')
  photoOrigin = document.getElementById('photo-origin')
  for(const photo of photos){ 
    photo.addEventListener('click', handlerClickOnPhoto)
  }
  close.addEventListener('click', handlerClickOnClose)
}

function handlerClickOnPhoto(elem) {
  const backgroundImage = elem.target.style.backgroundImage
  const to = backgroundImage.length - 2
  url = backgroundImage.substring(5, to)
  photoPopup.style.display='flex'
  photoOrigin.src = url
}

function handlerClickOnClose() {
  photoPopup.style.display='none'
  photoOrigin.style.opacity=''
}
