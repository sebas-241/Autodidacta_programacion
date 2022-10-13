package Clases;
public class Proceso {
    int id_producto;
    int valor_recibido;
    String producto;
    
    public Proceso(){
        id_producto = 0;
    }
        
    public Proceso(int id_producto){
        this.id_producto = id_producto;
    }
    
    
    public String NombreProducto(){
        switch (id_producto) {
            case 1:{
                producto = "Jabon de loza";
                break;
            }
            case 2:{
                producto = "Cerveza importada";
                break;
            }
            case 3:{
                producto = "Papas picantes nacionales";
                break;
            }
            case 4:{
                producto = "Shampoo anticaspa";
                break;
            }
            case 5:{
                producto = "Aceite de oliva";
                break;
            }
        }
        
        return producto;
    }
    
    
    
    public int calcularProducto(){
        switch (id_producto) {
            case 1:{
                valor_recibido = 3000;
                break;
            }
            case 2:{
                valor_recibido = 5500;
                break;
            }
            case 3:{
                valor_recibido = 3500;
                break;
            }
            case 4:{
                valor_recibido = 10000;
                break;
            }
            case 5:{
                valor_recibido = 15000;
                break;
            }
        }
        
        return valor_recibido;
    }
}
