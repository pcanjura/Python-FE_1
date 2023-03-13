const txtName = document.getElementById("name")
const txtEmail = document.getElementById("email")
const txtPass = document.getElementById("pass1")
const txtComent = document.getElementById("coment")
const form = document.getElementById("form")
const parrafo = document.getElementById("alertas")

form.addEventListener("submit", e => {
    e.preventDefault()
    let alertas = ""
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    let regexPass = /^(?=.*\d)(?=.*[a-záéíóúüñ]).*[A-ZÁÉÍÓÚÜÑ]/

    if (txtName.value.length < 6) {
        alertas += `El Nombre no es válido <br>`
        entrar = true
    }
    if (!regexEmail.test(txtEmail.value)) {
        alertas += `El Email no es válido <br>`
        entrar = true
    }
    if (txtPass.value.length < 8 && !regexPass.test(txtPass.value)) {
        alertas += `Contraseña invalida <br>`
        entrar = true
    }
    if (txtComent.value.length > 50) {
        alertas += `El comentario es muy largo <br>`
        entrar = true
    }
    if (entrar) {
        parrafo.innerHTML = alertas
    }
})



// Inicio de Ejercicio 4

function convertirMoneda() {
    // Obtener los valores de entrada del usuario
    var cantidad = document.getElementById("cantidad").value;
    var monedaOrigen = document.getElementById("moneda-origen").value;
    var monedaDestino = document.getElementById("moneda-destino").value;

    // Definir las tasas de cambio
    var tasaDolarBitcoin = 0.000049;
    var tasaBitcoinDolar = 22022.40;

    // Realizar la conversión
    var resultado;
    if (monedaOrigen === "USD" && monedaDestino === "BTC") {
        resultado = cantidad * tasaDolarBitcoin;
    } else if (monedaOrigen === "BTC" && monedaDestino === "USD") {
        resultado = cantidad * tasaBitcoinDolar;
    }

    // Mostrar el resultado en la página
    document.getElementById("resultado").innerHTML = resultado;
}





