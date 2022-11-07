const numero1 = document.getElementById("numero_1");
const numero2 = document.getElementById("numero_2");
const numero3 = document.getElementById("numero_3");
const resultado = document.getElementById("resultado");
const base = "El numero mayor entre los 3 ingresados es el: ";
const boton = document.getElementById("boton_calculador");  

boton.addEventListener('click', definir) 

function definir(){
    const num1 = parseFloat(numero1.value);
    const num2 = parseFloat(numero2.value);
    const num3 = parseFloat(numero3.value);

    if(num1 > num2 && num1 > num3 ){
        resultado.style = "color: yellow";
        resultado.innerText = base + num1;
    }
    if(num2 > num1 && num2 > num3){
        resultado.style = "color: blue";
        resultado.innerText = base + num2;
    }
    if(num3 > num1 && num3 > num2){
        resultado.style = "color: red";
        resultado.innerText = base + num3;
    }
};