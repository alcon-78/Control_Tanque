/*-----------------------------------------------------
Author:  --<fandres>
Date: 2014-04-03
Description: Adquiere informacion de un lm35 y lo envia a host
Programa Host [Python]: https://github.com/fandres/pyqwt-Temperatura-pinguino/tree/master/session5
-----------------------------------------------------*/

#include <stdlib.h>   // la necesitaremos para la función "itoa()"

char enviado[64];   // Cadena enviada a pyQt.
int entero = 0;     // Donde almacenamos temporalmente el valor leido.

char recibido[64];  // Cadena recibida desde pyQt 
u8 recibirbyte;
 
//-------------------------setup()---------------------//
void setup()
{
    pinMode(10, OUTPUT); // pin 10 led amarillo (nivel minimo)
    pinMode(11, OUTPUT); // pin 11 led verde (encendido OK / titilante falla)
    pinMode(12, OUTPUT); // pin 12 led rojo (rele termico del motor bomba de llenado activado)
    pinMode(13, INPUT);  // pin 13 boton ON/OFF bomba de llenado
    pinMode(14, INPUT);  // pin 14 potenciometro simulación de nivel.
    pinMode(17, INPUT);  // pin 17 contacto auxiliar rele termico (97-98) motor de llenado
}

//-------------------------loop()---------------------//
void loop()
{
    entero = analogRead(14);    // Leyendo del Pin13
    itoa(entero,enviado,10);    // Conversión de int a string
    BULK.write(enviado, 5);     // Enviado los datos al host
    delay(100);                 // Esperamos 100 milisegundos. 
    
    recibirbyte=0;
    
    if(BULK.available())
        recibirbyte = BULK.read(recibido);
                
    if(recibirbyte > 0){
    
    switch (recibirbyte){
        case 1:
            digitalWrite(10,HIGH); //LED AMARILLO ON
            break;
        case 2:
            digitalWrite(10,LOW); //LED AMARILLO OFF
            break;
        case 3:
            digitalWrite(11,HIGH); //LED VERDE ON
            break;
        case 4:
            digitalWrite(11,LOW); //LED VERDE OFF
            break;
        case 5:
            digitalWrite(12,HIGH); //LER ROJO ON
            break;
        case 6:
            digitalWrite(12,LOW); //LED ROJO OFF
            break;
        }
        delay(10);
     }
     recibido[recibirbyte] = 0;
}
    