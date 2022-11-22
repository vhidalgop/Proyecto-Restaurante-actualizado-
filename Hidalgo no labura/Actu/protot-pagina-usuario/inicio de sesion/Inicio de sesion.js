var boton = document.querySelector(".button")
let input = document.getElementById("usuario")
let contraseña = document.getElementById("contraseña")
let server = "http://127.0.0.1:5000";
let user = ""
contraseña.addEventListener("blur",()=>{
    
})
input.addEventListener("blur",(e)=>{

})
console.log(contraseña)
function registrate (){

}
boton.addEventListener("click", async function  submit(e) {
    let contra = contraseña.value
    console.log(contra)
    let user = input.value
    console.log(user)
    e.preventDefault()
    const respuesta = await fetch(`${server}/inicio_sesion`,{
      method:["POST"],
      headers:{"Content-Type":"application/json"
    },
    body: JSON.stringify ({
        user,
        contra
   
    })
    })
})