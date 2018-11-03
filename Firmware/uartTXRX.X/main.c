#include "config.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <plib/usart.h>
#include "config_intosc.h"

/* modulo uart*/
void InitSerial();
void TransmiteByte(unsigned char byte);
unsigned char RecebeByte();

/*------------------------------------------------------------------------------*/

void main(void) {
    
    InitPorts();
    InitSerial();
    unsigned char dado;
    unsigned char d1 = '$';
    unsigned char d2 = '!';
    unsigned char d3 = '@';
    unsigned char LIGA = 'w';
    unsigned char DESLIGA = 'p';
    
    while(1)
    {
        dado = RecebeByte();
        if(dado == 'L'){
            TransmiteByte(d1);
            TransmiteByte(d2);
            TransmiteByte(d3);
            TransmiteByte(LIGA);
            dado = '0';
        }
        if(dado == 'L'){
            TransmiteByte(d1);
            TransmiteByte(d2);
            TransmiteByte(d3);
            TransmiteByte(DESLIGA);
            dado = '0';
        }
        delay_ms(100);
    }            
    return;
}
/*------------------------------------------------------------------------------*/

void InitSerial()
{
    OpenUSART(USART_TX_INT_OFF
              & USART_RX_INT_OFF
              & USART_ASYNCH_MODE
              & USART_EIGHT_BIT
              & USART_CONT_RX
              & USART_BRGH_HIGH,155);  
              //64 = 19200 com CLK = 20MHZ
              //155 = 19200 com CLK = 48 Mhz
}
/*------------------------------------------------------------------------------*/

void TransmiteByte(unsigned char byte)
{
  while(!TXSTA1bits.TRMT); /* aguarda liberar modulo para envio de dado */
  
    putcUSART(byte); 
}
/*------------------------------------------------------------------------------*/

unsigned char RecebeByte()
{
    unsigned char b = 0x00;
    
    b = getcUSART();
    
    return b;
}

/*------------------------------------------------------------------------------*/
