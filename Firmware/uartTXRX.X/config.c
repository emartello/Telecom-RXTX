#include "config.h"

// PIC18F4550 Configuration Bit Settings

// 'C' source line config statements

// CONFIG1L

void InitPorts()
{
    TRISA = 0xff;       /*set as input port*/
    
    ADCON1 = 0x0e;      /*ref vtg is VDD and Configure pin as analog pin*/    
    ADCON2 = 0x92;      /*Right Justified, 4Tad and Fosc/32. */
    ADRESH = 0x00;           /*Flush ADC output Register*/
    ADRESL = 0x00;   
}

void delay_ms(int tempo)
{
    while(tempo--)
        __delay_ms(1);
}
