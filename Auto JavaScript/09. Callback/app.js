function callback(id, fn){                  // Funcion comun
    setTimeout(() => {                         // Funcion para que demore un tiempo asignado es ejecutarse una funcionalidad, se pasa funcion y tiempo en milisegundos
        fn("Sebastian Gonzalez Rodriguez");             
    }, 3000);
}

callback("1016712994", (nombre) => {        // Se pasan parametros y se imprime en consola, como esta definido arriba en segundos,                                         
    console.log("Aqui demora 3 segundos");  // se demorara en ejecutar, mientras hace la bucle que le sigue.
    console.log(nombre);                     
});

for (let x = 0; x < 10; x++) {      // Se ejecuta primero, ya que la siguiente funcion se demora, asi que va con esta primero
    console.log(x);
}