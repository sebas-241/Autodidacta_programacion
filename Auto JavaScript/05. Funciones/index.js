//funcion sin argumentos 
// Tambien se puede utilizar la funcion antes de utilizarla 
// saludar();
function saludar(){
    console.log("Hola mundo");
}
saludar();  //Usar la funcion

// Funcion con argumentos
function saludarcon(nombre, edad){
    console.log("Hola, mi nombre es: " + nombre);
    console.log("y mi edad es: " + edad);
}
saludarcon("Sebastian", 18)      // Se puede pasar cualquier tipo de dato

function multiplicacion(num1, num2){
    let resultado = num1 * num2;        // Let restringue el uso de la variable
    return resultado;
}

console.log(multiplicacion(2, 5))       // Mostrar el return por consola