// Los objetos son como los diccionarios de Python, Key: value,

let persona1 = {
    nombre: "Sebastian",
    edad: 18,
    masculino: true
}
// Crear propiedad a un objeto: objeto.propiedad_a_crear = "valor"
persona1.comidaFavorita = "Empanadas"

// Mostrar solo una propidad del objeto: objeto.propiedad_a_mostrar
console.log(persona1.nombre)

// Cambiar valor de propiedad por otra: objeto.propiedad_a_cambiar = "nuevo valor"
persona1.nombre = "Juan"
console.log(persona1.nombre)

let persona2 = {
    nombre: "Juana",
    edad: 15,
    masculino: false
}

let arreglodeObjetos = [persona1, persona2]