/*------------------------------------------------------------------------------------------------
Author:  --<fandres>
Date: 2014-04-03
Description: Adquiere informacion de un lm35 y lo envia a host
Programa Host [Python]: https://github.com/fandres/pyqwt-Temperatura-pinguino/tree/master/session5

Programa modificado por Cristian O. Viola
Sistema SCADA (control nivel de un tanque de agua) usando pyQt y Pinguino 18F2550
Enero 2015 - cristian_viola@hotmail.com.ar
---------------------------------------------------------------------------------------------------*/

#include <stdlib.h>   // la necesitaremos para la función "itoa()"

char enviado[64];   // Cadena enviada a pyQt.
int entero = 0;     // Donde almacenamos temporalmente el valor leido.

char recibido[0];  // Cadena recibida desde pyQt 
u8 recibirbyte;
 
//----------------------------------------setup()-------------------------------------------------//
void setup()
{
    pinMode(10, OUTPUT); // pin 10 Sistema en línea
    pinMode(11, OUTPUT); // pin 11 Bomba de llenado
    pinMode(12, OUTPUT); // pin 12 Valvula de vaciado
    pinMode(13, INPUT);  // pin 13 boton ON/OFF bomba de llenado
    pinMode(14, INPUT);  // pin 14 potenciometro simulación de nivel.
    pinMode(17, INPUT);  // pin 17 contacto auxiliar rele termico (97-98) motor de llenado
}

//-----------------------------------------loop()-------------------------------------------------//
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
        switch (recibido[0]){
        case '1':
            digitalWrite(10,HIGH); // Indicador sistema en linea "ON"
            break;
        case '2':
            digitalWrite(10,LOW); // Indicador sistema en linea "OFF"
            break;
        case '3':
            digitalWrite(11,HIGH); //Activar bomba de llenado tanque agua
            break;
        case '4':
            digitalWrite(11,LOW); //Desactivar bomba de llenado tanque agua
            break;
        case '5':
            digitalWrite(12,HIGH); //Activar válvula de vaciado tanque agua
            break;
        case '6':
            digitalWrite(12,LOW); //Desactivar válvula de vaciado tanque agua
            break;
        }
     delay(10);
     }
recibido[recibirbyte] = 0;
}
    