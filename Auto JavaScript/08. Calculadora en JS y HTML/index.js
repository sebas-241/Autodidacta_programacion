// Agarrar elementos del HTML
const opera1 = document.getElementById("operador1");    // dentro del parentesis va el "id" del html a capturar
const opera = document.getElementById("operador"); 
const opera2 = document.getElementById("operador2"); 
const botonCalcular = document.getElementById("calcular"); 
const resul = document.getElementById("resultado");

// Se le agrega un evento al boton, al hacer 'click', para la funcion
botonCalcular.addEventListener('click', calcular) 


function calcular(){
    const operador = opera.value;
    const operador1 = parseFloat(opera1.value);
    const operador2 = parseFloat(opera2.value);
    
    if((operador == '+' || operador == '-' || operador == '*' || operador == '/') && !isNaN(operador1) && !isNaN(operador2)){
        let resultado;
        switch(operador){
            case "+":
                resultado = operador1 + operador2;    
                break;          // El break, para en el caso que se cumpla y sale del switch
            case "-":
                resultado = operador1 - operador2;
                break;
            case "*":
                resultado = operador1 * operador2;
                break;
            case "/":
                resultado = operador1 / operador2;
                break;    
        }
        resul.style = "color: black";
        resul.innerText = "= " + resultado;
    }
    else{
        resul.style = "color: red";
        resul.innerText = "EL calculo no es posible";
    }
}