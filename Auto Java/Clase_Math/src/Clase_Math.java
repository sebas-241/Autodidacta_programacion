public class Clase_Math {
    public static void main(String[] args) {
        // Raiz cuadrada de un numero
        double raiz = Math.sqrt(9);     // double por el metodo
        System.out.println(raiz);
        
        // Redondear un numero
        double num1 = 5.85;
        int resultado = (int)Math.round(num1);      // Convertir dato a otro para que sea compatible con la variable "Refundicion"
        System.out.println(resultado);
        
        // Potenciacion
        double base = 5;
        double exponente = 3;
        
        int resultado2 = (int)Math.pow(base, exponente);    // Convertir dato a otro para que sea compatible con la variable "Refundicion"
        System.out.println(resultado2);
    }
    
}
