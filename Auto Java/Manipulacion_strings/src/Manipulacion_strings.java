public class Manipulacion_strings {
    public static void main(String[] args) {
        
        String nombre = "Sebastian";            // Creacion de un objeto tipo String
        System.out.println("Mi nombre es " + nombre);
        
        System.out.println("Mi nombre tiene " + nombre.length() + " letras.");      // Usando un metodo de la clase String
        
        System.out.println("La primer letra de mi nombre es la " + nombre.charAt(0));       // Usando un metodo de la clase String
        
        int ultima_letra = nombre.length();
        System.out.println("La ultima letra de mi nombre es: " + nombre.charAt(ultima_letra -1));
        
    }
    
}
