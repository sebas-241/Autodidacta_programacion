package leyendo;

import java.io.FileReader;          // Librerias importantes para menejo de excepciones y para el file reader
import java.io.IOException;

public class Archivo_externo {
    public static void main(String[] args) {
        
        Leer accediendo = new Leer();       // crear un nuevo objeto
        accediendo.lee();                   // usando el metodo leer
    }
    
    
}

class Leer {                    // se crea una clase externa de la principal
    public void lee(){      // crear un metodo
        try {           // se crea un try y un catch para que funcione el File Reader y no error
            FileReader entrada = new FileReader("C:\\Users\\sebgo\\OneDrive\\Escritorio\\Autodidacta_programacion\\Auto Java\\Tratamiento_de_datos_externos\\ejemplo.txt");      // Se pone la direccion de nuestro archivo
            
            int c = entrada.read();     // Se crea una variable entera para que me devuelva el valor entero de cada caracter del archivo
            
            while(c != -1){     // Se crea un while para que haga un bucle y se muestren todos los caracteres del documento, se pone que sea diferente a -1 ya que esta es la ultima letra del documento
                c = entrada.read();
                char letra = (char)c;       // Se transforma de entero a caracter
                System.out.print(letra);    // Se muestra la letra
            }
        }
        catch (IOException e){      // Es un control de error, se pone el nombre de la excepcion y lo que se quiera que haga si ocurre
            System.out.println("El archivo no fue encontrado, por favor comuniquese al 3003367605 para solucionar el problema...");
        }
        
    }
}
