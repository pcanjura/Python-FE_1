function contar(numero){
    for (i=0;i<numero;i++){
        console.log(i);
    }
}
function contar2(numero){
    let i = 0;
    while (i<numero){
        console.log(i);
        i++;
    }
}

function multi_rusa(multiplicador, multiplicando, div){
    let suma = 0;
    let tabla_res = '<table class="tabla01">';
    tabla_res += '<tr><th>Multiplicador</th><th>Multiplicando</th><th>Impar</th><th>Suma</th></tr>';
    while (multiplicador>=1){
        let impar = false;
        let m2 = 0
        if (multiplicador%2!=0){
            suma += multiplicando*1;
            impar = true;
            m2 = multiplicando;
            suma*=1;
        }
        tabla_res += '<tr><td>'+multiplicador+'</td><td>'+multiplicando+'</td>'
        tabla_res += '<td>'+impar+'</td><td>'+m2+'</td></tr>';
        multiplicador=Math.trunc(multiplicador/2);
        multiplicando*=2;
    }
    tabla_res += '<tr><td></td><td></td><td></td><td>'+suma+'</td></tr>';
    tabla_res += '</table>';
    document.getElementById(div).innerHTML = tabla_res
}