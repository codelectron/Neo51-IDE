//
// Register Declarations for Microchip 16C715 Processor
//
//
// This header file was automatically generated by:
//
//	inc2h.pl V4850
//
//	Copyright (c) 2002, Kevin L. Pauba, All Rights Reserved
//
//	SDCC is licensed under the GNU Public license (GPL) v2.  Note that
//	this license covers the code to the compiler and other executables,
//	but explicitly does not cover any code or objects generated by sdcc.
//	We have not yet decided on a license for the run time libraries, but
//	it will not put any requirements on code linked against it. See:
// 
//	http://www.gnu.org/copyleft/gpl/html
//
//	See http://sdcc.sourceforge.net/ for the latest information on sdcc.
//
// 
#ifndef P16C715_H
#define P16C715_H

//
// Register addresses.
//
#define INDF_ADDR	0x0000
#define TMR0_ADDR	0x0001
#define PCL_ADDR	0x0002
#define STATUS_ADDR	0x0003
#define FSR_ADDR	0x0004
#define PORTA_ADDR	0x0005
#define PORTB_ADDR	0x0006
#define PCLATH_ADDR	0x000A
#define INTCON_ADDR	0x000B
#define PIR1_ADDR	0x000C
#define ADRES_ADDR	0x001E
#define ADCON0_ADDR	0x001F
#define OPTION_REG_ADDR	0x0081
#define TRISA_ADDR	0x0085
#define TRISB_ADDR	0x0086
#define PIE1_ADDR	0x008C
#define PCON_ADDR	0x008E
#define ADCON1_ADDR	0x009F

//
// Memory organization.
//



//         LIST
// P16C715.INC  Standard Header File, Version 1.01    Microchip Technology, Inc.
//         NOLIST

// This header file defines configurations, registers, and other useful bits of
// information for the PIC16C715 microcontroller.  These names are taken to match 
// the data sheets as closely as possible.  

// Note that the processor must be selected before this file is 
// included.  The processor may be selected the following ways:

//       1. Command line switch:
//               C:\ MPASM MYFILE.ASM /PIC16C715
//       2. LIST directive in the source file
//               LIST   P=PIC16C715
//       3. Processor Type entry in the MPASM full-screen interface

//==========================================================================
//
//       Revision History
//
//==========================================================================

//Rev:   Date:    Reason:

//1.01   05/12/97 Added values for Parity Enable configuration bits
//1.00   04/11/96 Initial Release

//==========================================================================
//
//       Verify Processor
//
//==========================================================================

//        IFNDEF __16C715
//            MESSG "Processor-header file mismatch.  Verify selected processor."
//         ENDIF

//==========================================================================
//
//       Register Definitions
//
//==========================================================================

#define W                    0x0000
#define F                    0x0001

//----- Register Files------------------------------------------------------

extern __sfr  __at (INDF_ADDR)                    INDF;
extern __sfr  __at (TMR0_ADDR)                    TMR0;
extern __sfr  __at (PCL_ADDR)                     PCL;
extern __sfr  __at (STATUS_ADDR)                  STATUS;
extern __sfr  __at (FSR_ADDR)                     FSR;
extern __sfr  __at (PORTA_ADDR)                   PORTA;
extern __sfr  __at (PORTB_ADDR)                   PORTB;
extern __sfr  __at (PCLATH_ADDR)                  PCLATH;
extern __sfr  __at (INTCON_ADDR)                  INTCON;
extern __sfr  __at (PIR1_ADDR)                    PIR1;
extern __sfr  __at (ADRES_ADDR)                   ADRES;
extern __sfr  __at (ADCON0_ADDR)                  ADCON0;

extern __sfr  __at (OPTION_REG_ADDR)              OPTION_REG;
extern __sfr  __at (TRISA_ADDR)                   TRISA;
extern __sfr  __at (TRISB_ADDR)                   TRISB;
extern __sfr  __at (PIE1_ADDR)                    PIE1;
extern __sfr  __at (PCON_ADDR)                    PCON;
extern __sfr  __at (ADCON1_ADDR)                  ADCON1;

//----- STATUS Bits --------------------------------------------------------


//----- INTCON Bits --------------------------------------------------------


//----- PIR1 Bits ----------------------------------------------------------


//----- ADCON0 Bits --------------------------------------------------------


//----- OPTION Bits --------------------------------------------------------


//----- PIE1 Bits ----------------------------------------------------------


//----- PCON Bits ----------------------------------------------------------


//----- ADCON1 Bits --------------------------------------------------------


//==========================================================================
//
//       RAM Definition
//
//==========================================================================

//         __MAXRAM H'FF'
//         __BADRAM H'07'-H'09', H'0D'-H'1D'
//         __BADRAM H'87'-H'89', H'8D', H'8F'-H'9E', H'C0'-H'EF'

//==========================================================================
//
//       Configuration Bits
//
//==========================================================================

#define _MPEEN_ON            0x3FFF 
#define _MPEEN_OFF           0x3F7F
#define _BODEN_ON            0x3FFF
#define _BODEN_OFF           0x3FBF
#define _CP_ALL              0x00CF
#define _CP_50               0x15DF
#define _CP_OFF              0x3FFF
#define _PWRTE_OFF           0x3FFF
#define _PWRTE_ON            0x3FF7
#define _WDT_ON              0x3FFF
#define _WDT_OFF             0x3FFB
#define _LP_OSC              0x3FFC
#define _XT_OSC              0x3FFD
#define _HS_OSC              0x3FFE
#define _RC_OSC              0x3FFF

//         LIST

// ----- ADCON0 bits --------------------
typedef union {
  struct {
    unsigned char ADON:1;
    unsigned char :1;
    unsigned char GO:1;
    unsigned char CHS0:1;
    unsigned char CHS1:1;
    unsigned char CHS2:1;
    unsigned char ADCS0:1;
    unsigned char ADCS1:1;
  };
  struct {
    unsigned char :1;
    unsigned char :1;
    unsigned char NOT_DONE:1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
  };
  struct {
    unsigned char :1;
    unsigned char :1;
    unsigned char GO_DONE:1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
  };
} __ADCON0bits_t;
extern volatile __ADCON0bits_t __at(ADCON0_ADDR) ADCON0bits;

// ----- ADCON1 bits --------------------
typedef union {
  struct {
    unsigned char PCFG0:1;
    unsigned char PCFG1:1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
  };
} __ADCON1bits_t;
extern volatile __ADCON1bits_t __at(ADCON1_ADDR) ADCON1bits;

// ----- INTCON bits --------------------
typedef union {
  struct {
    unsigned char RBIF:1;
    unsigned char INTF:1;
    unsigned char T0IF:1;
    unsigned char RBIE:1;
    unsigned char INTE:1;
    unsigned char T0IE:1;
    unsigned char PEIE:1;
    unsigned char GIE:1;
  };
} __INTCONbits_t;
extern volatile __INTCONbits_t __at(INTCON_ADDR) INTCONbits;

// ----- OPTION_REG bits --------------------
typedef union {
  struct {
    unsigned char PS0:1;
    unsigned char PS1:1;
    unsigned char PS2:1;
    unsigned char PSA:1;
    unsigned char T0SE:1;
    unsigned char T0CS:1;
    unsigned char INTEDG:1;
    unsigned char NOT_RBPU:1;
  };
} __OPTION_REGbits_t;
extern volatile __OPTION_REGbits_t __at(OPTION_REG_ADDR) OPTION_REGbits;

// ----- PCON bits --------------------
typedef union {
  struct {
    unsigned char NOT_BO:1;
    unsigned char NOT_POR:1;
    unsigned char NOT_MPE:1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
  };
  struct {
    unsigned char NOT_BOR:1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
  };
} __PCONbits_t;
extern volatile __PCONbits_t __at(PCON_ADDR) PCONbits;

// ----- PIE1 bits --------------------
typedef union {
  struct {
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char ADIE:1;
    unsigned char :1;
  };
} __PIE1bits_t;
extern volatile __PIE1bits_t __at(PIE1_ADDR) PIE1bits;

// ----- PIR1 bits --------------------
typedef union {
  struct {
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char :1;
    unsigned char ADIF:1;
    unsigned char :1;
  };
} __PIR1bits_t;
extern volatile __PIR1bits_t __at(PIR1_ADDR) PIR1bits;

// ----- PORTA bits --------------------
typedef union {
  struct {
    unsigned char RA0:1;
    unsigned char RA1:1;
    unsigned char RA2:1;
    unsigned char RA3:1;
    unsigned char RA4:1;
    unsigned char RA5:1;
    unsigned char :1;
    unsigned char :1;
  };
} __PORTAbits_t;
extern volatile __PORTAbits_t __at(PORTA_ADDR) PORTAbits;

// ----- PORTB bits --------------------
typedef union {
  struct {
    unsigned char RB0:1;
    unsigned char RB1:1;
    unsigned char RB2:1;
    unsigned char RB3:1;
    unsigned char RB4:1;
    unsigned char RB5:1;
    unsigned char RB6:1;
    unsigned char RB7:1;
  };
} __PORTBbits_t;
extern volatile __PORTBbits_t __at(PORTB_ADDR) PORTBbits;

// ----- STATUS bits --------------------
typedef union {
  struct {
    unsigned char C:1;
    unsigned char DC:1;
    unsigned char Z:1;
    unsigned char NOT_PD:1;
    unsigned char NOT_TO:1;
    unsigned char RP0:1;
    unsigned char RP1:1;
    unsigned char IRP:1;
  };
} __STATUSbits_t;
extern volatile __STATUSbits_t __at(STATUS_ADDR) STATUSbits;

// ----- TRISA bits --------------------
typedef union {
  struct {
    unsigned char TRISA0:1;
    unsigned char TRISA1:1;
    unsigned char TRISA2:1;
    unsigned char TRISA3:1;
    unsigned char TRISA4:1;
    unsigned char TRISA5:1;
    unsigned char :1;
    unsigned char :1;
  };
} __TRISAbits_t;
extern volatile __TRISAbits_t __at(TRISA_ADDR) TRISAbits;

// ----- TRISB bits --------------------
typedef union {
  struct {
    unsigned char TRISB0:1;
    unsigned char TRISB1:1;
    unsigned char TRISB2:1;
    unsigned char TRISB3:1;
    unsigned char TRISB4:1;
    unsigned char TRISB5:1;
    unsigned char TRISB6:1;
    unsigned char TRISB7:1;
  };
} __TRISBbits_t;
extern volatile __TRISBbits_t __at(TRISB_ADDR) TRISBbits;


#ifndef NO_BIT_DEFINES

#define ADON                 ADCON0bits.ADON                /* bit 0 */
#define GO                   ADCON0bits.GO                  /* bit 2 */
#define GO_DONE              ADCON0bits.GO_DONE             /* bit 2 */
#define NOT_DONE             ADCON0bits.NOT_DONE            /* bit 2 */
#define CHS0                 ADCON0bits.CHS0                /* bit 3 */
#define CHS1                 ADCON0bits.CHS1                /* bit 4 */
#define CHS2                 ADCON0bits.CHS2                /* bit 5 */
#define ADCS0                ADCON0bits.ADCS0               /* bit 6 */
#define ADCS1                ADCON0bits.ADCS1               /* bit 7 */

#define PCFG0                ADCON1bits.PCFG0               /* bit 0 */
#define PCFG1                ADCON1bits.PCFG1               /* bit 1 */

#define RBIF                 INTCONbits.RBIF                /* bit 0 */
#define INTF                 INTCONbits.INTF                /* bit 1 */
#define T0IF                 INTCONbits.T0IF                /* bit 2 */
#define RBIE                 INTCONbits.RBIE                /* bit 3 */
#define INTE                 INTCONbits.INTE                /* bit 4 */
#define T0IE                 INTCONbits.T0IE                /* bit 5 */
#define PEIE                 INTCONbits.PEIE                /* bit 6 */
#define GIE                  INTCONbits.GIE                 /* bit 7 */

#define PS0                  OPTION_REGbits.PS0             /* bit 0 */
#define PS1                  OPTION_REGbits.PS1             /* bit 1 */
#define PS2                  OPTION_REGbits.PS2             /* bit 2 */
#define PSA                  OPTION_REGbits.PSA             /* bit 3 */
#define T0SE                 OPTION_REGbits.T0SE            /* bit 4 */
#define T0CS                 OPTION_REGbits.T0CS            /* bit 5 */
#define INTEDG               OPTION_REGbits.INTEDG          /* bit 6 */
#define NOT_RBPU             OPTION_REGbits.NOT_RBPU        /* bit 7 */

#define NOT_BO               PCONbits.NOT_BO                /* bit 0 */
#define NOT_BOR              PCONbits.NOT_BOR               /* bit 0 */
#define NOT_POR              PCONbits.NOT_POR               /* bit 1 */
#define NOT_MPE              PCONbits.NOT_MPE               /* bit 2 */

#define ADIE                 PIE1bits.ADIE                  /* bit 6 */

#define ADIF                 PIR1bits.ADIF                  /* bit 6 */

#define RA0                  PORTAbits.RA0                  /* bit 0 */
#define RA1                  PORTAbits.RA1                  /* bit 1 */
#define RA2                  PORTAbits.RA2                  /* bit 2 */
#define RA3                  PORTAbits.RA3                  /* bit 3 */
#define RA4                  PORTAbits.RA4                  /* bit 4 */
#define RA5                  PORTAbits.RA5                  /* bit 5 */

#define RB0                  PORTBbits.RB0                  /* bit 0 */
#define RB1                  PORTBbits.RB1                  /* bit 1 */
#define RB2                  PORTBbits.RB2                  /* bit 2 */
#define RB3                  PORTBbits.RB3                  /* bit 3 */
#define RB4                  PORTBbits.RB4                  /* bit 4 */
#define RB5                  PORTBbits.RB5                  /* bit 5 */
#define RB6                  PORTBbits.RB6                  /* bit 6 */
#define RB7                  PORTBbits.RB7                  /* bit 7 */

#define C                    STATUSbits.C                   /* bit 0 */
#define DC                   STATUSbits.DC                  /* bit 1 */
#define Z                    STATUSbits.Z                   /* bit 2 */
#define NOT_PD               STATUSbits.NOT_PD              /* bit 3 */
#define NOT_TO               STATUSbits.NOT_TO              /* bit 4 */
#define RP0                  STATUSbits.RP0                 /* bit 5 */
#define RP1                  STATUSbits.RP1                 /* bit 6 */
#define IRP                  STATUSbits.IRP                 /* bit 7 */

#define TRISA0               TRISAbits.TRISA0               /* bit 0 */
#define TRISA1               TRISAbits.TRISA1               /* bit 1 */
#define TRISA2               TRISAbits.TRISA2               /* bit 2 */
#define TRISA3               TRISAbits.TRISA3               /* bit 3 */
#define TRISA4               TRISAbits.TRISA4               /* bit 4 */
#define TRISA5               TRISAbits.TRISA5               /* bit 5 */

#define TRISB0               TRISBbits.TRISB0               /* bit 0 */
#define TRISB1               TRISBbits.TRISB1               /* bit 1 */
#define TRISB2               TRISBbits.TRISB2               /* bit 2 */
#define TRISB3               TRISBbits.TRISB3               /* bit 3 */
#define TRISB4               TRISBbits.TRISB4               /* bit 4 */
#define TRISB5               TRISBbits.TRISB5               /* bit 5 */
#define TRISB6               TRISBbits.TRISB6               /* bit 6 */
#define TRISB7               TRISBbits.TRISB7               /* bit 7 */
#endif /* NO_BIT_DEFINES */

#ifndef NO_LEGACY_NAMES
#define ADCON0_bits          ADCON0bits
#define ADCON1_bits          ADCON1bits
#define INTCON_bits          INTCONbits
#define OPTION_REG_bits      OPTION_REGbits
#define PCON_bits            PCONbits
#define PIE1_bits            PIE1bits
#define PIR1_bits            PIR1bits
#define PORTA_bits           PORTAbits
#define PORTB_bits           PORTBbits
#define STATUS_bits          STATUSbits
#define TRISA_bits           TRISAbits
#define TRISB_bits           TRISBbits
#endif /* NO_LEGACY_NAMES */

#endif
