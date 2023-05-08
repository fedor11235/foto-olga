let buttonUploadPhoto
let fileInput

document.addEventListener("DOMContentLoaded", handlerDOMContentLoaded)

function handlerDOMContentLoaded() {
  const photosDelete = document.getElementsByClassName('delete')
  buttonUploadPhoto = document.getElementById('upload-photo')
  fileInput = document.getElementById('fileInput')
  buttonUploadPhoto.addEventListener('click', handlerClickUploadPhoto)
  fileInput.addEventListener('change', handlerClickChangeFileInput)
  for(const photoDelete of photosDelete){ 
    photoDelete.addEventListener('click', handlerClickPhotoDelete)
  }
}

function handlerClickPhotoDelete(event) {
  const fileName = event.target.dataset.fileName
  sendingRequestPhotoDeleted(fileName)
}

function handlerClickUploadPhoto() {
  fileInput.click()
}

function handlerClickChangeFileInput(event) {
  const image = event.target.files[0]
  if(!image) {
    alert('файл не выбран')
    return
  }
  if(!checkSizeCompatibleOne(image)) {
    alert('файл большого размера')
    return
  }
  if(!checkSizeCompatibleOne(image)) {
    alert('файл неправильного формата')
    return
  }
  const formData = new FormData
  formData.append('image', image)

  const res = fetch('/upload_photo', {
    method: 'POST',
    body: formData
  })
  res.then(() => window.location.reload())
  event.target.value = ''
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

function sendingRequestPhotoDeleted(fileName) {
  const Request = new XMLHttpRequest()
  Request.open('POST', '/deleted_photo', true)
  Request.onreadystatechange = () => {
    if (Request.readyState == 4) window.location.reload()
  }
  Request.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8')
  const payload = 'fileName=' + fileName
  Request.send(payload)
}