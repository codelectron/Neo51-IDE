;--------------------------------------------------------
; File Created by SDCC : free open source ANSI-C Compiler
; Version 3.1.1 #7132 (Dec 26 2011) (Linux)
; This file was generated Mon Feb  6 14:16:08 2012
;--------------------------------------------------------
	.module main
	.optsdcc -mmcs51 --model-small
	
;--------------------------------------------------------
; Public variables in this module
;--------------------------------------------------------
	.globl _pinmode_PARM_2
	.globl _digitalwrite_PARM_2
	.globl _main
	.globl _Delayus
	.globl _Delayms
	.globl _pinmode
	.globl _digitalread
	.globl _digitalwrite
	.globl _SWDT
	.globl _WDT
	.globl _WDTS
	.globl _WDRE
	.globl _WDOUT
	.globl _PBO
	.globl _PPC
	.globl _EBO
	.globl _EC
	.globl _CCF0
	.globl _CCF1
	.globl _CCF2
	.globl _CCF3
	.globl _CCF4
	.globl _CR
	.globl _CF
	.globl _TF2
	.globl _EXF2
	.globl _RCLK
	.globl _TCLK
	.globl _EXEN2
	.globl _TR2
	.globl _C_T2
	.globl _CP_RL2
	.globl _T2CON_7
	.globl _T2CON_6
	.globl _T2CON_5
	.globl _T2CON_4
	.globl _T2CON_3
	.globl _T2CON_2
	.globl _T2CON_1
	.globl _T2CON_0
	.globl _PT2
	.globl _ET2
	.globl _CY
	.globl _AC
	.globl _F0
	.globl _RS1
	.globl _RS0
	.globl _OV
	.globl _F1
	.globl _P
	.globl _PS
	.globl _PT1
	.globl _PX1
	.globl _PT0
	.globl _PX0
	.globl _RD
	.globl _WR
	.globl _T1
	.globl _T0
	.globl _INT1
	.globl _INT0
	.globl _TXD
	.globl _RXD
	.globl _P3_7
	.globl _P3_6
	.globl _P3_5
	.globl _P3_4
	.globl _P3_3
	.globl _P3_2
	.globl _P3_1
	.globl _P3_0
	.globl _EA
	.globl _ES
	.globl _ET1
	.globl _EX1
	.globl _ET0
	.globl _EX0
	.globl _P2_7
	.globl _P2_6
	.globl _P2_5
	.globl _P2_4
	.globl _P2_3
	.globl _P2_2
	.globl _P2_1
	.globl _P2_0
	.globl _SM0
	.globl _SM1
	.globl _SM2
	.globl _REN
	.globl _TB8
	.globl _RB8
	.globl _TI
	.globl _RI
	.globl _P1_7
	.globl _P1_6
	.globl _P1_5
	.globl _P1_4
	.globl _P1_3
	.globl _P1_2
	.globl _P1_1
	.globl _P1_0
	.globl _TF1
	.globl _TR1
	.globl _TF0
	.globl _TR0
	.globl _IE1
	.globl _IT1
	.globl _IE0
	.globl _IT0
	.globl _P0_7
	.globl _P0_6
	.globl _P0_5
	.globl _P0_4
	.globl _P0_3
	.globl _P0_2
	.globl _P0_1
	.globl _P0_0
	.globl _T2MOD
	.globl _WDTD
	.globl _WDTC
	.globl _SPDAT
	.globl _SPDR
	.globl _SPCFG
	.globl _SPSR
	.globl _SPCTL
	.globl _SPCR
	.globl _SADEN
	.globl _SADDR
	.globl _IP1H
	.globl _IP1
	.globl _IP0H
	.globl _IP0
	.globl _IEN1
	.globl _IEN0
	.globl _FCF
	.globl _FST
	.globl _CMOD
	.globl _CL
	.globl _CH
	.globl _CCON
	.globl _CCAPM4
	.globl _CCAPM3
	.globl _CCAPM2
	.globl _CCAPM1
	.globl _CCAPM0
	.globl _CCAP4L
	.globl _CCAP3L
	.globl _CCAP2L
	.globl _CCAP1L
	.globl _CCAP0L
	.globl _CCAP4H
	.globl _CCAP3H
	.globl _CCAP2H
	.globl _CCAP1H
	.globl _CCAP0H
	.globl _AUXR1
	.globl _AUXR
	.globl _TH2
	.globl _TL2
	.globl _RCAP2H
	.globl _RCAP2L
	.globl _T2CON
	.globl _B
	.globl _ACC
	.globl _PSW
	.globl _IP
	.globl _P3
	.globl _IE
	.globl _P2
	.globl _SBUF
	.globl _SCON
	.globl _P1
	.globl _TH1
	.globl _TH0
	.globl _TL1
	.globl _TL0
	.globl _TMOD
	.globl _TCON
	.globl _PCON
	.globl _DPH
	.globl _DPL
	.globl _SP
	.globl _P0
	.globl _setup
	.globl _loop
;--------------------------------------------------------
; special function registers
;--------------------------------------------------------
	.area RSEG    (ABS,DATA)
	.org 0x0000
_P0	=	0x0080
_SP	=	0x0081
_DPL	=	0x0082
_DPH	=	0x0083
_PCON	=	0x0087
_TCON	=	0x0088
_TMOD	=	0x0089
_TL0	=	0x008a
_TL1	=	0x008b
_TH0	=	0x008c
_TH1	=	0x008d
_P1	=	0x0090
_SCON	=	0x0098
_SBUF	=	0x0099
_P2	=	0x00a0
_IE	=	0x00a8
_P3	=	0x00b0
_IP	=	0x00b8
_PSW	=	0x00d0
_ACC	=	0x00e0
_B	=	0x00f0
_T2CON	=	0x00c8
_RCAP2L	=	0x00ca
_RCAP2H	=	0x00cb
_TL2	=	0x00cc
_TH2	=	0x00cd
_AUXR	=	0x008e
_AUXR1	=	0x00a2
_CCAP0H	=	0x00fa
_CCAP1H	=	0x00fb
_CCAP2H	=	0x00fc
_CCAP3H	=	0x00fd
_CCAP4H	=	0x00fe
_CCAP0L	=	0x00ea
_CCAP1L	=	0x00eb
_CCAP2L	=	0x00ec
_CCAP3L	=	0x00ed
_CCAP4L	=	0x00ee
_CCAPM0	=	0x00da
_CCAPM1	=	0x00db
_CCAPM2	=	0x00dc
_CCAPM3	=	0x00dd
_CCAPM4	=	0x00de
_CCON	=	0x00d8
_CH	=	0x00f9
_CL	=	0x00e9
_CMOD	=	0x00d9
_FST	=	0x00b6
_FCF	=	0x00b1
_IEN0	=	0x00a8
_IEN1	=	0x00e8
_IP0	=	0x00b8
_IP0H	=	0x00b7
_IP1	=	0x00f8
_IP1H	=	0x00f7
_SADDR	=	0x00a9
_SADEN	=	0x00b9
_SPCR	=	0x00d5
_SPCTL	=	0x00d5
_SPSR	=	0x00aa
_SPCFG	=	0x00aa
_SPDR	=	0x0086
_SPDAT	=	0x0086
_WDTC	=	0x00c0
_WDTD	=	0x0085
_T2MOD	=	0x00c9
;--------------------------------------------------------
; special function bits
;--------------------------------------------------------
	.area RSEG    (ABS,DATA)
	.org 0x0000
_P0_0	=	0x0080
_P0_1	=	0x0081
_P0_2	=	0x0082
_P0_3	=	0x0083
_P0_4	=	0x0084
_P0_5	=	0x0085
_P0_6	=	0x0086
_P0_7	=	0x0087
_IT0	=	0x0088
_IE0	=	0x0089
_IT1	=	0x008a
_IE1	=	0x008b
_TR0	=	0x008c
_TF0	=	0x008d
_TR1	=	0x008e
_TF1	=	0x008f
_P1_0	=	0x0090
_P1_1	=	0x0091
_P1_2	=	0x0092
_P1_3	=	0x0093
_P1_4	=	0x0094
_P1_5	=	0x0095
_P1_6	=	0x0096
_P1_7	=	0x0097
_RI	=	0x0098
_TI	=	0x0099
_RB8	=	0x009a
_TB8	=	0x009b
_REN	=	0x009c
_SM2	=	0x009d
_SM1	=	0x009e
_SM0	=	0x009f
_P2_0	=	0x00a0
_P2_1	=	0x00a1
_P2_2	=	0x00a2
_P2_3	=	0x00a3
_P2_4	=	0x00a4
_P2_5	=	0x00a5
_P2_6	=	0x00a6
_P2_7	=	0x00a7
_EX0	=	0x00a8
_ET0	=	0x00a9
_EX1	=	0x00aa
_ET1	=	0x00ab
_ES	=	0x00ac
_EA	=	0x00af
_P3_0	=	0x00b0
_P3_1	=	0x00b1
_P3_2	=	0x00b2
_P3_3	=	0x00b3
_P3_4	=	0x00b4
_P3_5	=	0x00b5
_P3_6	=	0x00b6
_P3_7	=	0x00b7
_RXD	=	0x00b0
_TXD	=	0x00b1
_INT0	=	0x00b2
_INT1	=	0x00b3
_T0	=	0x00b4
_T1	=	0x00b5
_WR	=	0x00b6
_RD	=	0x00b7
_PX0	=	0x00b8
_PT0	=	0x00b9
_PX1	=	0x00ba
_PT1	=	0x00bb
_PS	=	0x00bc
_P	=	0x00d0
_F1	=	0x00d1
_OV	=	0x00d2
_RS0	=	0x00d3
_RS1	=	0x00d4
_F0	=	0x00d5
_AC	=	0x00d6
_CY	=	0x00d7
_ET2	=	0x00ad
_PT2	=	0x00bd
_T2CON_0	=	0x00c8
_T2CON_1	=	0x00c9
_T2CON_2	=	0x00ca
_T2CON_3	=	0x00cb
_T2CON_4	=	0x00cc
_T2CON_5	=	0x00cd
_T2CON_6	=	0x00ce
_T2CON_7	=	0x00cf
_CP_RL2	=	0x00c8
_C_T2	=	0x00c9
_TR2	=	0x00ca
_EXEN2	=	0x00cb
_TCLK	=	0x00cc
_RCLK	=	0x00cd
_EXF2	=	0x00ce
_TF2	=	0x00cf
_CF	=	0x00df
_CR	=	0x00de
_CCF4	=	0x00dc
_CCF3	=	0x00db
_CCF2	=	0x00da
_CCF1	=	0x00d9
_CCF0	=	0x00d8
_EC	=	0x00ae
_EBO	=	0x00eb
_PPC	=	0x00be
_PBO	=	0x00fb
_WDOUT	=	0x00c4
_WDRE	=	0x00c3
_WDTS	=	0x00c2
_WDT	=	0x00c1
_SWDT	=	0x00c0
;--------------------------------------------------------
; overlayable register banks
;--------------------------------------------------------
	.area REG_BANK_0	(REL,OVR,DATA)
	.ds 8
;--------------------------------------------------------
; internal ram data
;--------------------------------------------------------
	.area DSEG    (DATA)
;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
	.area	OSEG    (OVR,DATA)
_digitalwrite_PARM_2:
	.ds 2
	.area	OSEG    (OVR,DATA)
	.area	OSEG    (OVR,DATA)
_pinmode_PARM_2:
	.ds 2
	.area	OSEG    (OVR,DATA)
	.area	OSEG    (OVR,DATA)
;--------------------------------------------------------
; Stack segment in internal ram 
;--------------------------------------------------------
	.area	SSEG	(DATA)
__start__stack:
	.ds	1

;--------------------------------------------------------
; indirectly addressable internal ram data
;--------------------------------------------------------
	.area ISEG    (DATA)
;--------------------------------------------------------
; absolute internal ram data
;--------------------------------------------------------
	.area IABS    (ABS,DATA)
	.area IABS    (ABS,DATA)
;--------------------------------------------------------
; bit data
;--------------------------------------------------------
	.area BSEG    (BIT)
;--------------------------------------------------------
; paged external ram data
;--------------------------------------------------------
	.area PSEG    (PAG,XDATA)
;--------------------------------------------------------
; external ram data
;--------------------------------------------------------
	.area XSEG    (XDATA)
;--------------------------------------------------------
; absolute external ram data
;--------------------------------------------------------
	.area XABS    (ABS,XDATA)
;--------------------------------------------------------
; external initialized ram data
;--------------------------------------------------------
	.area XISEG   (XDATA)
	.area HOME    (CODE)
	.area GSINIT0 (CODE)
	.area GSINIT1 (CODE)
	.area GSINIT2 (CODE)
	.area GSINIT3 (CODE)
	.area GSINIT4 (CODE)
	.area GSINIT5 (CODE)
	.area GSINIT  (CODE)
	.area GSFINAL (CODE)
	.area CSEG    (CODE)
;--------------------------------------------------------
; interrupt vector 
;--------------------------------------------------------
	.area HOME    (CODE)
__interrupt_vect:
	ljmp	__sdcc_gsinit_startup
;--------------------------------------------------------
; global & static initialisations
;--------------------------------------------------------
	.area HOME    (CODE)
	.area GSINIT  (CODE)
	.area GSFINAL (CODE)
	.area GSINIT  (CODE)
	.globl __sdcc_gsinit_startup
	.globl __sdcc_program_startup
	.globl __start__stack
	.globl __mcs51_genXINIT
	.globl __mcs51_genXRAMCLEAR
	.globl __mcs51_genRAMCLEAR
	.area GSFINAL (CODE)
	ljmp	__sdcc_program_startup
;--------------------------------------------------------
; Home
;--------------------------------------------------------
	.area HOME    (CODE)
	.area HOME    (CODE)
__sdcc_program_startup:
	lcall	_main
;	return from main will lock up
	sjmp .
;--------------------------------------------------------
; code
;--------------------------------------------------------
	.area CSEG    (CODE)
;------------------------------------------------------------
;Allocation info for local variables in function 'digitalwrite'
;------------------------------------------------------------
;state                     Allocated with name '_digitalwrite_PARM_2'
;output                    Allocated to registers 
;------------------------------------------------------------
;	/home/krish/work/Neo51-ide/tools/bin/../share/sdcc/include/mcs51/digitalw.c:22: void digitalwrite(int output,int state)
;	-----------------------------------------
;	 function digitalwrite
;	-----------------------------------------
_digitalwrite:
	ar7 = 0x07
	ar6 = 0x06
	ar5 = 0x05
	ar4 = 0x04
	ar3 = 0x03
	ar2 = 0x02
	ar1 = 0x01
	ar0 = 0x00
;	/home/krish/work/Neo51-ide/tools/bin/../share/sdcc/include/mcs51/digitalw.c:46: }
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'digitalread'
;------------------------------------------------------------
;input                     Allocated to registers 
;------------------------------------------------------------
;	/home/krish/work/Neo51-ide/tools/bin/../share/sdcc/include/mcs51/digitalw.c:48: int digitalread(int input)
;	-----------------------------------------
;	 function digitalread
;	-----------------------------------------
_digitalread:
;	/home/krish/work/Neo51-ide/tools/bin/../share/sdcc/include/mcs51/digitalw.c:73: }
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'pinmode'
;------------------------------------------------------------
;state                     Allocated with name '_pinmode_PARM_2'
;input                     Allocated to registers 
;------------------------------------------------------------
;	/home/krish/work/Neo51-ide/tools/bin/../share/sdcc/include/mcs51/digitalw.c:75: void pinmode(int input, int state)
;	-----------------------------------------
;	 function pinmode
;	-----------------------------------------
_pinmode:
;	/home/krish/work/Neo51-ide/tools/bin/../share/sdcc/include/mcs51/digitalw.c:99: }
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'Delayms'
;------------------------------------------------------------
;milliseconde              Allocated to registers r4 r5 r6 r7 
;i                         Allocated to registers r0 r1 r2 r3 
;------------------------------------------------------------
;	/home/krish/work/Neo51-ide/tools/bin/../share/sdcc/include/mcs51/arduinodelay.c:8: void Delayms(unsigned long milliseconde)
;	-----------------------------------------
;	 function Delayms
;	-----------------------------------------
_Delayms:
	mov	r4,dpl
	mov	r5,dph
	mov	r6,b
	mov	r7,a
;	/home/krish/work/Neo51-ide/tools/bin/../share/sdcc/include/mcs51/arduinodelay.c:12: for (i=0;i<milliseconde;i++);
	mov	r0,#0x00
	mov	r1,#0x00
	mov	r2,#0x00
	mov	r3,#0x00
00101$:
	clr	c
	mov	a,r0
	subb	a,r4
	mov	a,r1
	subb	a,r5
	mov	a,r2
	subb	a,r6
	mov	a,r3
	subb	a,r7
	jnc	00105$
	inc	r0
	cjne	r0,#0x00,00113$
	inc	r1
	cjne	r1,#0x00,00113$
	inc	r2
	cjne	r2,#0x00,00101$
	inc	r3
00113$:
	sjmp	00101$
00105$:
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'Delayus'
;------------------------------------------------------------
;microsecondes             Allocated to registers r6 r7 
;i                         Allocated to registers r4 r5 
;------------------------------------------------------------
;	/home/krish/work/Neo51-ide/tools/bin/../share/sdcc/include/mcs51/arduinodelay.c:15: void Delayus(int microsecondes)
;	-----------------------------------------
;	 function Delayus
;	-----------------------------------------
_Delayus:
	mov	r6,dpl
	mov	r7,dph
;	/home/krish/work/Neo51-ide/tools/bin/../share/sdcc/include/mcs51/arduinodelay.c:19: for (i=0;i<microsecondes;i++);
	mov	r4,#0x00
	mov	r5,#0x00
00101$:
	mov	ar2,r6
	mov	ar3,r7
	clr	c
	mov	a,r4
	subb	a,r2
	mov	a,r5
	subb	a,r3
	jnc	00105$
	inc	r4
	cjne	r4,#0x00,00101$
	inc	r5
	sjmp	00101$
00105$:
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'setup'
;------------------------------------------------------------
;	/home/krish/work/Neo51-ide/source/user.c:4: void setup(void)
;	-----------------------------------------
;	 function setup
;	-----------------------------------------
_setup:
;	/home/krish/work/Neo51-ide/source/user.c:6: pinmode(0,OUTPUT);	// test caractères
	clr	a
	mov	_pinmode_PARM_2,a
	mov	(_pinmode_PARM_2 + 1),a
	mov	dpl,a
	mov	dph,a
	ljmp	_pinmode
;------------------------------------------------------------
;Allocation info for local variables in function 'loop'
;------------------------------------------------------------
;	/home/krish/work/Neo51-ide/source/user.c:9: void loop(void)
;	-----------------------------------------
;	 function loop
;	-----------------------------------------
_loop:
;	/home/krish/work/Neo51-ide/source/user.c:11: digitalwrite(0,HIGH); 
	mov	_digitalwrite_PARM_2,#0x01
	mov	(_digitalwrite_PARM_2 + 1),#0x00
	mov	dptr,#0x0000
	lcall	_digitalwrite
;	/home/krish/work/Neo51-ide/source/user.c:12: Delayms(500);
	mov	dptr,#0x01F4
	clr	a
	mov	b,a
	lcall	_Delayms
;	/home/krish/work/Neo51-ide/source/user.c:13: digitalwrite(0,LOW);
	clr	a
	mov	_digitalwrite_PARM_2,a
	mov	(_digitalwrite_PARM_2 + 1),a
	mov	dpl,a
	mov	dph,a
	lcall	_digitalwrite
;	/home/krish/work/Neo51-ide/source/user.c:14: Delayms(500);
	mov	dptr,#0x01F4
	clr	a
	mov	b,a
	lcall	_Delayms
;	/home/krish/work/Neo51-ide/source/user.c:15: Delayms(500);
	mov	dptr,#0x01F4
	clr	a
	mov	b,a
	ljmp	_Delayms
;------------------------------------------------------------
;Allocation info for local variables in function 'main'
;------------------------------------------------------------
;	/home/krish/work/Neo51-ide/source/main.c:5: void main()
;	-----------------------------------------
;	 function main
;	-----------------------------------------
_main:
;	/home/krish/work/Neo51-ide/source/main.c:8: setup();
	lcall	_setup
;	/home/krish/work/Neo51-ide/source/main.c:10: while(1)
00102$:
;	/home/krish/work/Neo51-ide/source/main.c:11: loop();
	lcall	_loop
	sjmp	00102$
	.area CSEG    (CODE)
	.area CONST   (CODE)
	.area XINIT   (CODE)
	.area CABS    (ABS,CODE)
