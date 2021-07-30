const burgerBtn = document.querySelector('.burger')
const burgerMenu = document.querySelector('.burger_menu')
const burgerBg = document.querySelector('.burger_bg')
const burgerClose = document.querySelectorAll('.burger_close')
burgerBtn.addEventListener('click', function() {
    burgerMenu.classList.add('burger_active')
    burgerBg.classList.add('burger_active')

})


for(let i = 0; i < burgerClose.length; i++){
    burgerClose[i].addEventListener('click', function() {
        burgerMenu.classList.remove('burger_active')
        burgerBg.classList.remove('burger_active')
    })

}
