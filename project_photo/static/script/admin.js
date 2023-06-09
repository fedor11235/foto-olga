let buttonUploadPhoto
let buttonUploadAvatar
let photoInput
let avatarInput

document.addEventListener("DOMContentLoaded", handlerDOMContentLoaded)

function handlerDOMContentLoaded() {
  const photosDelete = document.getElementsByClassName('delete')
  const customersDelete = document.getElementsByClassName('delete-customer')
  buttonUploadPhoto = document.getElementById('upload-photo')
  photoInput = document.getElementById('photoInput')
  buttonUploadAvatar = document.getElementById('upload-avatar')
  avatarInput = document.getElementById('avatarInput')
  buttonUploadPhoto.addEventListener('click', handlerClickUploadPhoto)
  buttonUploadAvatar.addEventListener('click', handlerClickUploadAvatar)
  photoInput.addEventListener('change', (event) => handlerClickChangeInput(event, '/upload_photo'))
  avatarInput.addEventListener('change', (event) => handlerClickChangeInput(event, '/upload_avatar'))
  for(const customerDelete of customersDelete){ 
    customerDelete.addEventListener('click', handlerClickCustomerDelete)
  }
  for(const photoDelete of photosDelete){ 
    photoDelete.addEventListener('click', handlerClickPhotoDelete)
  }
}

function handlerClickPhotoDelete(event) {
  const fileName = event.target.dataset.fileName
  sendingRequestPhotoDeleted(fileName)
}

function handlerClickCustomerDelete(event) {
  const customerId = event.target.dataset.customerId
  sendingRequestCustomerDeleted(customerId)
}

function handlerClickUploadPhoto() {
  photoInput.click()
}

function handlerClickUploadAvatar() {
  avatarInput.click()
}

function handlerClickChangeInput(event, url) {
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

  const res = fetch(url, {
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

function sendingRequestCustomerDeleted(customerId) {
  const Request = new XMLHttpRequest()
  Request.open('POST', '/deleted_customer', true)
  Request.onreadystatechange = () => {
    if (Request.readyState == 4) window.location.reload()
  }
  Request.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8')
  const payload = 'customerId=' + customerId
  Request.send(payload)
}