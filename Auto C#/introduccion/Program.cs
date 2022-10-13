// Esto es un comentario
// Crear archivo                    dotnet new console
Console.WriteLine("Hello, World!"); // Mostrar por pantalla
string dato = Console.ReadLine();   // Guarda lo que se pone en el WriteLine
const int valor_constante = 34;     // variable - constante
string variable = "Sebastian";      // Variable normal

// Tipos numéricos
int numero_entero = 23;
float flotante = 3_45;
Console.WriteLine(flotante);

//  Tipos textuales
string varios_caracteres = "Hola mundo, cadena larga";
char un_solo_caracter = 'a';
string nombre = "Sebas";
string texto = $"Mi nombre es {nombre}";    // Se coloca el $ para enlazar variables

// Valor booleano
bool verdadero = true;
bool falso = false;

//Operadores
int num1 = 2;
bool si_es_igual = num1 == 2;     // Si es totalmente igual
bool si_es_desigual = num1 != 2;    // SI es desigual

int edad = 20; 
bool inferiorA20 = edad < 20; 
bool inferiorOIgualA20 = edad <= 20; 
bool superiorA20 = edad > 20; 
bool superiorOIgualA20 = edad >= 20; 

int suma = 1 + 2; 
int diferencia = 4 - 2; 
int multiplicacion = 6 * 3; 
int division = 18 / 3; 
int modulo = 19 % 3; 

// Concadenar cadenas
string nombre1 = "Juan";
string apellido = "Gonzalo";
string nombrecompleto = nombre1 + apellido;



// Otros tipos de datos
// DATETIME IMPONER FECHA (AÑO, MES, DIA, HORA QUE ES OPCIONAL)
var fecha = new DateTime(2022, 9, 3, 19, 00, 00);

// DATETIME HORA ACTUAL
var ahora = DateTime.Now; 
var ahoraUtc = DateTime.UtcNow; // Formato UTC

// DATETIME CON MAS PRECISION
var fecha2 = new DateTime(2022, 9, 3, 19, 05, 23); 
var fechaOffset = new DateTimeOffset(fecha2); 
var fechaOffset2 = fecha; 


// DateOnly, guarda solo la fecha mas no la hora 
DateOnly d1 = new DateOnly(2022, 9, 3); 
Console.WriteLine(d1.Year); // 2022 
Console.WriteLine(d1.Month); // 9
Console.WriteLine(d1.Day); // 3
Console.WriteLine(d1.DayOfWeek); // Sabado

// TimeOnly, guarda solo la hora pero no la fecha 
TimeOnly t1 = new TimeOnly(16, 30); 
Console.WriteLine(t1.Hour); // 16 
Console.WriteLine(t1.Minute); // 30 
Console.WriteLine(t1.Second); // 0 