// let es lo mismo que var, pero mejor

// Condicional
let miNumero = 3;
if(miNumero == 3){
    console.log("El numero es 3");
}else{
    console.log("El numero no es 3");
}

// Condicional con == o ===
// Los dos == sirve para verificar si dos variables son iguales, no importa el tipo
let miNumero2 = 20;
if(miNumero2 == "20"){
    console.log("Si");
}else{
    console.log("No");
}

// Los tres === sirve para verificar si dos variables son iguales y que sus tipos tambien lo sean
if(miNumero2 === "20"){
    console.log("Si");
}else{
    console.log("No");
}

// Es distinto? !=
let miNumero4 = 20;
if(miNumero2 != 10){
    console.log("Si, es distinto");
}else{
    console.log("No, es igual");
}

// and == &&
let edad = 17;
let nombre = "Sebastian";
if(edad == 17 && nombre == "Sebastian"){
    console.log("El nombre y la edad son iguales");
}else{
    console.log("El nombre y la edad son erroneos");
}


// or == ||
let edad2 = 20;
let nombre2 = "Juan";
if(edad2 < 17 || nombre2 == "Sebastian"){
    console.log("El nombre y la edad son iguales");
}else{
    console.log("El nombre o la edad son erroneos");
}


// else if
let minumeroTest = -10;
if(minumeroTest >= 1){
    console.log("El numero es positivo");
}else if(minumeroTest === 0){
    console.log("El numero es cero");
}else{
    console.log("El numero es negativo");
}