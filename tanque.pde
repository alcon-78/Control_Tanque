/*-----------------------------------------------------
Author:  --<fandres>
Date: 2014-04-03
Description: Adquiere informacion de un lm35 y lo envia a host.Pro
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
    digitalWrite(11, LOW); // apagar led verde
}

//-------------------------loop()---------------------//
void loop()
{
    //
    //
    //
    
    entero = analogRead(14);    // Leyendo del Pin13
    itoa(entero,enviado,10);    // Conversión de int a string
    BULK.write(enviado, 5);    // Enviado los datos al host
    delay(100);                // Esperamos 100 milisegundos. 
    
    //
    //
    //
    
    recibirbyte=0;
    if(BULK.available())
        do {
                recibirbyte = BULK.read(recibido);
                
            } while(recibirbyte == 0);
            recibido[recibirbyte] = 0;
       
            if(recibirbyte > 0){
                 // Establecer estados (ON/OFF) led de sealizacion del sistema             
                 if (recibirbyte == '1') digitalWrite(10,HIGH);
                 else if (recibirbyte == '2') digitalWrite(10,LOW);
                 else if (recibirbyte == '3') digitalWrite(11,HIGH);
                 else if (recibirbyte == '4') digitalWrite(11,LOW);
                 else if (recibirbyte == '5') digitalWrite(12,HIGH);
                 else if (recibirbyte == '6') digitalWrite(12,LOW);
                 else{
                 // Cualquier otro valor
                    digitalWrite(10,LOW);
                    digitalWrite(11,LOW);
                    digitalWrite(12,LOW);             
                  }
             }
}