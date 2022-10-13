public class Constantes_and_operadores {
    public static void main(String[] args) {
        // Operadores
        int a = 5;
        
        int b;
        b = 7;
        
        float c = b / a;        // Float porque el resultado es un decimal y no consume tanto como double
        //c ++;   // Incrementa uno
        //c += 10;    // Incrementa un valor en 10, en este caso
        
        System.out.println(c);
        
        
        
        // Consantes
        final int d =  5;   // Ya no se puede alterar esta variable por el final
        System.out.println(d);
        
        
        final double pulgadas = 2.54;
        double cm = 6;
        
        double resultado = cm / pulgadas;
        
        System.out.println("En " + cm + " centimetros hay " + resultado + " pulgadas.");
        
        
        // Variables en una linea
        
        int operador_1, operador_2, resultado_3;
        
        operador_1 = 10;
        operador_2 = 10;
        resultado_3 = operador_1 + operador_2;
        
        System.out.println(resultado_3);
        

    }
    
}
