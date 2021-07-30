const input = document.querySelector('#input__file');
const btnbg = document.querySelector('#input__filed');
const btncom = document.querySelector('#input__file-com')
const block = document.querySelector('#com-bg')
const bgavatar = document.getElementById("bg-avatar")
const avatar = document.getElementById("avatar")


input.onchange = (e) => {
    readURL(e.target)
}


function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            console.log(e.target.result);
            avatar.style.background = `url(${e.target.result})`;
            avatar.style.backgroundSize = `cover`;
        };

        reader.readAsDataURL(input.files[0]);
    }
}



btnbg.onchange = (e) => {
    readURLbg(e.target)
}


function readURLbg(btnbg) {
    if (btnbg.files && btnbg.files[0]) {
        let other = new FileReader();
        other.onload = function (e) {
            // console.log(e.target.result);
            bgavatar.style.background = `url(${e.target.result})`;
            bgavatar.style.backgroundSize = `cover`;
        };

        other.readAsDataURL(btnbg.files[0]);
    }
}



btncom.onchange = (e) => {
    readURLcom(e.target)
}


function readURLcom(btncom) {
    if (btncom.files && btncom.files[0]) {
        let old = new FileReader();
        old.onload = function (e) {
            console.log(e.target.result);
            block.style.background = `url(${e.target.result})`;
            block.style.backgroundSize = `cover`;
        };

        old.readAsDataURL(btncom.files[0]);
    }
}