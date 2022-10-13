package Clases;
public class Persona {
    private String nombre;
    private int edad;
    private int identificacion;
    private String sexo;
    private float peso;
    private float altura;
    
    public Persona(){
        
    }
    
    public String getNombre(){
        return nombre;
    }
    public void setNombre(String valor_nombre){
        this.nombre = valor_nombre;
    }
    
    public int getEdad(){
        return edad;
    }
    public void setEdad(int valor_edad){
        this.edad = valor_edad;
    }
}
