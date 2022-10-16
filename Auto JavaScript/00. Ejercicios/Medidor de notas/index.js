const nota = document.getElementById("nota");
const verifi = document.getElementById("boton");
const final = document.getElementById("mensaje");


verifi.addEventListener('click', logica);

function logica(){
    const notaF = parseFloat(nota.value);

    if(!isNaN(notaF)){
        let resultado;
        switch(notaF){
            case 10:
                resultado = "Su nota es bastante mala.";
                break;
            case 20:
                resultado = "Su nota no es suficiente para pasar";
                break;
            case 30:
                resultado = "Su nota es apenas suficiente para pasar";
                break;
            case 40:
                resultado = "Tiene una buena nota, ha pasado.";
                break;
            case 50:
                resultado = "Aprobo con la mejor nota.";
                break;
        }
        final.style = "color: black";
        final.innerText = resultado;
    }
    else{
        final.style = "color:red";
        final.innerText = "El valor que ha ingresado es errorneo. Vuelva a intentarlo. Recuerde los datos que debe ingresar: (10, 20, 30, 40, 50).";
    }
}
