let enrollPopup
let close
let menu
let logo
let topBurger
let middleBurger
let bottomBurger

document.addEventListener('DOMContentLoaded', handlerDOMContentLoaded)

function handlerDOMContentLoaded() {
  const like = document.getElementById('like')
  const enroll = document.getElementById('enroll')
  const enrollMenu = document.getElementById('enroll-menu')
  const burger = document.getElementById('burger')
  logo = document.getElementById('logo')
  menu = document.getElementById('menu')
  topBurger = document.getElementById('top-burger')
  middleBurger = document.getElementById('middle-burger')
  bottomBurger = document.getElementById('bottom-burger')
  close = document.getElementById('close-contact')
  enrollPopup = document.getElementById('enroll-popup')
  burger.addEventListener('click', hendlerOpenMenu)
  like.addEventListener('click', hendlerSendingRequestLike)
  enroll.addEventListener('click', hendlerShowEnrollPopup)
  enrollMenu.addEventListener('click', hendlerShowEnrollPopup)
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

function hendlerOpenMenu() {
  if(menu.style.transform) {
    menu.style.transform=''
    logo.style.display=''
    topBurger.style.transform=''
    middleBurger.style.display='block'
    bottomBurger.style.transform=''
  } else {
    menu.style.transform='translateY(0)'
    logo.style.display='none'
    topBurger.style.transform='rotate(45deg) translate(-3px,-1px)'
    middleBurger.style.display='none'
    bottomBurger.style.transform='rotate(-45deg) translate(0px,-2px)'
  }
}

function hendlerShowEnrollPopup() {
  enrollPopup.style.display='flex'
}

function hendlerHideEnrollPopup() {
  enrollPopup.style.display='none'
}


