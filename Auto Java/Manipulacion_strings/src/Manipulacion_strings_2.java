public class Manipulacion_strings_2 {
    public static void main(String[] args) {
        //substring
        String frase = "Hoy es un estupendo dia para aprender a programar en Java";
        
        String frase_resumen = frase.substring(29, 57) + " sabiendo un poco de Python.";     // el indice del inicio y del final +1
        System.out.println(frase_resumen);
        
        
        
        //equals
        String alumno_1, alumno_2;
        alumno_1 = "David";
        alumno_2 = "david";
        
        System.out.println(alumno_1.equals(alumno_2));      // compara si dos cadenas con iguales, true/false
        
        System.out.println(alumno_1.equalsIgnoreCase(alumno_2));    // compara si dos cadenas con iguales, true/false, no distingue entre mayusculas ni minusculass
                
                
        
    }
}
