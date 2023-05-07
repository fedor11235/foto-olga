let buttonUploadPhoto
let fileInput

document.addEventListener("DOMContentLoaded", handlerDOMContentLoaded)

function handlerDOMContentLoaded() {
  buttonUploadPhoto = document.getElementById('upload-photo')
  fileInput = document.getElementById('fileInput')
  buttonUploadPhoto.addEventListener('click', handlerClickUploadPhoto)
  fileInput.addEventListener('change', handlerClickChangeFileInput)
}
function handlerClickUploadPhoto() {
  fileInput.click()
}
function handlerClickChangeFileInput(event) {
  const image = event.target.files[0]
  if(!checkSizeCompatibleOne(image)) {
    console.log('файл большого размера')
  }
  if(!checkSizeCompatibleOne(image)) {
    console.log('файл неправильного формата')
  }
  payload = 'image=' + image
  sendingRequestToServer('POST', '/upload_photo', payload)
  event.target.value = ''
}
function sendingRequestToServer(method, url, payload) {
  const Request = new XMLHttpRequest()
  Request.open(method, url, true)
  Request.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8')
  Request.onreadystatechange = () => {
    if (Request.readyState == 4) {
      console.log('sending to the server was successful')
    }
  }
  Request.send(payload)
}
function getFilteredFile(file) {
  if (/\.(jpg|jpeg|png|webp|JPG|PNG|JPEG|WEBP)$/.test(file.name)) {
    return true
  }
  return false
}
function checkSizeCompatibleOne(file) {
  const sizeInMb = (file.size / (1024 * 1024)).toFixed(2)
  if (sizeInMb > 5) {
    return false
  }
  return true
}