import Clases.*;
public class Principal {
    public static void main(String[] args) {
        Persona p = new Persona();
        p.setNombre("Sebastian");
        p.setEdad(17);
        
        
        
        System.out.println(p.getNombre());
        System.out.println(p.getEdad());
    }
    
}
