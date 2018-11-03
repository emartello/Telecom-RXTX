
/* 
 * File:   config.h
 * Author: Emiliano
 * Comments: Configuracoes basicas do PIC18F4550
 * Revision history: 
 */

// This is a guard condition so that contents of this file are not included
// more than once.  
#ifndef CONFIG_H
#define	CONFIG_H

#include <xc.h> // include processor files - each processor file is guarded.  

#define _XTAL_FREQ  48000000 /* frequencia do clock utilizado internamente */

void InitPorts();
void delay_ms(int tempo);

#endif