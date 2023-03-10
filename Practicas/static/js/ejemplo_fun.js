function factorial (num) {
	let total = 1; 
	for (i=1; i<=num; i++) {
		total = total * i; 
        console.log(total); 
	}
}

function parImpar(numero) {
    if (numero % 2 == 0){
        document.getElementById('respuesta').innerHTML = 'El numero es par'
    }else if (numero % 2 == 1){
        document.getElementById('respuesta').innerHTML = 'El numero es impar'
    }
}


document.addEventListener("DOMContentLoaded", function() { 
    document.getElementById("formulario").addEventListener(submit, validar)
});

function validar (evento) {
    evento.preventDefault();
    var usuario = document.getElementById('nombre').value;
    if (usuario.length == 0) {
        alert('Usuario no puede estar vacio');
        return;
    }
    this.submit
}


