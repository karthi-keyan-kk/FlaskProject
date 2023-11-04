let id = document.getElementById('id')
let name = document.getElementById('name')
let email = document.getElementById('email')
let role = document.getElementById('role')

let form = document.getElementById('form1')

let btn = document.getElementById('btn')

btn.addEventListener('click', ()=>{
    let value = email.value
    let firstIndex = value.indexOf("@")
    let lastIndex = value.lastIndexOf(".")

    if(value.includes("@") && value.includes(".")){
        if(firstIndex < 1 || ((lastIndex-firstIndex) < 2)){
            alert("Invalid E-mail")
            email.focus()
        }
        else{
            form.setAttribute("method", "post")
        }
    }
})
