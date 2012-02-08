                              1 ;--------------------------------------------------------
                              2 ; File Created by SDCC : free open source ANSI-C Compiler
                              3 ; Version 3.1.1 #7132 (Dec 26 2011) (Linux)
                              4 ; This file was generated Mon Feb  6 14:16:08 2012
                              5 ;--------------------------------------------------------
                              6 	.module main
                              7 	.optsdcc -mmcs51 --model-small
                              8 	
                              9 ;--------------------------------------------------------
                             10 ; Public variables in this module
                             11 ;--------------------------------------------------------
                             12 	.globl _pinmode_PARM_2
                             13 	.globl _digitalwrite_PARM_2
                             14 	.globl _main
                             15 	.globl _Delayus
                             16 	.globl _Delayms
                             17 	.globl _pinmode
                             18 	.globl _digitalread
                             19 	.globl _digitalwrite
                             20 	.globl _SWDT
                             21 	.globl _WDT
                             22 	.globl _WDTS
                             23 	.globl _WDRE
                             24 	.globl _WDOUT
                             25 	.globl _PBO
                             26 	.globl _PPC
                             27 	.globl _EBO
                             28 	.globl _EC
                             29 	.globl _CCF0
                             30 	.globl _CCF1
                             31 	.globl _CCF2
                             32 	.globl _CCF3
                             33 	.globl _CCF4
                             34 	.globl _CR
                             35 	.globl _CF
                             36 	.globl _TF2
                             37 	.globl _EXF2
                             38 	.globl _RCLK
                             39 	.globl _TCLK
                             40 	.globl _EXEN2
                             41 	.globl _TR2
                             42 	.globl _C_T2
                             43 	.globl _CP_RL2
                             44 	.globl _T2CON_7
                             45 	.globl _T2CON_6
                             46 	.globl _T2CON_5
                             47 	.globl _T2CON_4
                             48 	.globl _T2CON_3
                             49 	.globl _T2CON_2
                             50 	.globl _T2CON_1
                             51 	.globl _T2CON_0
                             52 	.globl _PT2
                             53 	.globl _ET2
                             54 	.globl _CY
                             55 	.globl _AC
                             56 	.globl _F0
                             57 	.globl _RS1
                             58 	.globl _RS0
                             59 	.globl _OV
                             60 	.globl _F1
                             61 	.globl _P
                             62 	.globl _PS
                             63 	.globl _PT1
                             64 	.globl _PX1
                             65 	.globl _PT0
                             66 	.globl _PX0
                             67 	.globl _RD
                             68 	.globl _WR
                             69 	.globl _T1
                             70 	.globl _T0
                             71 	.globl _INT1
                             72 	.globl _INT0
                             73 	.globl _TXD
                             74 	.globl _RXD
                             75 	.globl _P3_7
                             76 	.globl _P3_6
                             77 	.globl _P3_5
                             78 	.globl _P3_4
                             79 	.globl _P3_3
                             80 	.globl _P3_2
                             81 	.globl _P3_1
                             82 	.globl _P3_0
                             83 	.globl _EA
                             84 	.globl _ES
                             85 	.globl _ET1
                             86 	.globl _EX1
                             87 	.globl _ET0
                             88 	.globl _EX0
                             89 	.globl _P2_7
                             90 	.globl _P2_6
                             91 	.globl _P2_5
                             92 	.globl _P2_4
                             93 	.globl _P2_3
                             94 	.globl _P2_2
                             95 	.globl _P2_1
                             96 	.globl _P2_0
                             97 	.globl _SM0
                             98 	.globl _SM1
                             99 	.globl _SM2
                            100 	.globl _REN
                            101 	.globl _TB8
                            102 	.globl _RB8
                            103 	.globl _TI
                            104 	.globl _RI
                            105 	.globl _P1_7
                            106 	.globl _P1_6
                            107 	.globl _P1_5
                            108 	.globl _P1_4
                            109 	.globl _P1_3
                            110 	.globl _P1_2
                            111 	.globl _P1_1
                            112 	.globl _P1_0
                            113 	.globl _TF1
                            114 	.globl _TR1
                            115 	.globl _TF0
                            116 	.globl _TR0
                            117 	.globl _IE1
                            118 	.globl _IT1
                            119 	.globl _IE0
                            120 	.globl _IT0
                            121 	.globl _P0_7
                            122 	.globl _P0_6
                            123 	.globl _P0_5
                            124 	.globl _P0_4
                            125 	.globl _P0_3
                            126 	.globl _P0_2
                            127 	.globl _P0_1
                            128 	.globl _P0_0
                            129 	.globl _T2MOD
                            130 	.globl _WDTD
                            131 	.globl _WDTC
                            132 	.globl _SPDAT
                            133 	.globl _SPDR
                            134 	.globl _SPCFG
                            135 	.globl _SPSR
                            136 	.globl _SPCTL
                            137 	.globl _SPCR
                            138 	.globl _SADEN
                            139 	.globl _SADDR
                            140 	.globl _IP1H
                            141 	.globl _IP1
                            142 	.globl _IP0H
                            143 	.globl _IP0
                            144 	.globl _IEN1
                            145 	.globl _IEN0
                            146 	.globl _FCF
                            147 	.globl _FST
                            148 	.globl _CMOD
                            149 	.globl _CL
                            150 	.globl _CH
                            151 	.globl _CCON
                            152 	.globl _CCAPM4
                            153 	.globl _CCAPM3
                            154 	.globl _CCAPM2
                            155 	.globl _CCAPM1
                            156 	.globl _CCAPM0
                            157 	.globl _CCAP4L
                            158 	.globl _CCAP3L
                            159 	.globl _CCAP2L
                            160 	.globl _CCAP1L
                            161 	.globl _CCAP0L
                            162 	.globl _CCAP4H
                            163 	.globl _CCAP3H
                            164 	.globl _CCAP2H
                            165 	.globl _CCAP1H
                            166 	.globl _CCAP0H
                            167 	.globl _AUXR1
                            168 	.globl _AUXR
                            169 	.globl _TH2
                            170 	.globl _TL2
                            171 	.globl _RCAP2H
                            172 	.globl _RCAP2L
                            173 	.globl _T2CON
                            174 	.globl _B
                            175 	.globl _ACC
                            176 	.globl _PSW
                            177 	.globl _IP
                            178 	.globl _P3
                            179 	.globl _IE
                            180 	.globl _P2
                            181 	.globl _SBUF
                            182 	.globl _SCON
                            183 	.globl _P1
                            184 	.globl _TH1
                            185 	.globl _TH0
                            186 	.globl _TL1
                            187 	.globl _TL0
                            188 	.globl _TMOD
                            189 	.globl _TCON
                            190 	.globl _PCON
                            191 	.globl _DPH
                            192 	.globl _DPL
                            193 	.globl _SP
                            194 	.globl _P0
                            195 	.globl _setup
                            196 	.globl _loop
                            197 ;--------------------------------------------------------
                            198 ; special function registers
                            199 ;--------------------------------------------------------
                            200 	.area RSEG    (ABS,DATA)
   0000                     201 	.org 0x0000
                    0080    202 _P0	=	0x0080
                    0081    203 _SP	=	0x0081
                    0082    204 _DPL	=	0x0082
                    0083    205 _DPH	=	0x0083
                    0087    206 _PCON	=	0x0087
                    0088    207 _TCON	=	0x0088
                    0089    208 _TMOD	=	0x0089
                    008A    209 _TL0	=	0x008a
                    008B    210 _TL1	=	0x008b
                    008C    211 _TH0	=	0x008c
                    008D    212 _TH1	=	0x008d
                    0090    213 _P1	=	0x0090
                    0098    214 _SCON	=	0x0098
                    0099    215 _SBUF	=	0x0099
                    00A0    216 _P2	=	0x00a0
                    00A8    217 _IE	=	0x00a8
                    00B0    218 _P3	=	0x00b0
                    00B8    219 _IP	=	0x00b8
                    00D0    220 _PSW	=	0x00d0
                    00E0    221 _ACC	=	0x00e0
                    00F0    222 _B	=	0x00f0
                    00C8    223 _T2CON	=	0x00c8
                    00CA    224 _RCAP2L	=	0x00ca
                    00CB    225 _RCAP2H	=	0x00cb
                    00CC    226 _TL2	=	0x00cc
                    00CD    227 _TH2	=	0x00cd
                    008E    228 _AUXR	=	0x008e
                    00A2    229 _AUXR1	=	0x00a2
                    00FA    230 _CCAP0H	=	0x00fa
                    00FB    231 _CCAP1H	=	0x00fb
                    00FC    232 _CCAP2H	=	0x00fc
                    00FD    233 _CCAP3H	=	0x00fd
                    00FE    234 _CCAP4H	=	0x00fe
                    00EA    235 _CCAP0L	=	0x00ea
                    00EB    236 _CCAP1L	=	0x00eb
                    00EC    237 _CCAP2L	=	0x00ec
                    00ED    238 _CCAP3L	=	0x00ed
                    00EE    239 _CCAP4L	=	0x00ee
                    00DA    240 _CCAPM0	=	0x00da
                    00DB    241 _CCAPM1	=	0x00db
                    00DC    242 _CCAPM2	=	0x00dc
                    00DD    243 _CCAPM3	=	0x00dd
                    00DE    244 _CCAPM4	=	0x00de
                    00D8    245 _CCON	=	0x00d8
                    00F9    246 _CH	=	0x00f9
                    00E9    247 _CL	=	0x00e9
                    00D9    248 _CMOD	=	0x00d9
                    00B6    249 _FST	=	0x00b6
                    00B1    250 _FCF	=	0x00b1
                    00A8    251 _IEN0	=	0x00a8
                    00E8    252 _IEN1	=	0x00e8
                    00B8    253 _IP0	=	0x00b8
                    00B7    254 _IP0H	=	0x00b7
                    00F8    255 _IP1	=	0x00f8
                    00F7    256 _IP1H	=	0x00f7
                    00A9    257 _SADDR	=	0x00a9
                    00B9    258 _SADEN	=	0x00b9
                    00D5    259 _SPCR	=	0x00d5
                    00D5    260 _SPCTL	=	0x00d5
                    00AA    261 _SPSR	=	0x00aa
                    00AA    262 _SPCFG	=	0x00aa
                    0086    263 _SPDR	=	0x0086
                    0086    264 _SPDAT	=	0x0086
                    00C0    265 _WDTC	=	0x00c0
                    0085    266 _WDTD	=	0x0085
                    00C9    267 _T2MOD	=	0x00c9
                            268 ;--------------------------------------------------------
                            269 ; special function bits
                            270 ;--------------------------------------------------------
                            271 	.area RSEG    (ABS,DATA)
   0000                     272 	.org 0x0000
                    0080    273 _P0_0	=	0x0080
                    0081    274 _P0_1	=	0x0081
                    0082    275 _P0_2	=	0x0082
                    0083    276 _P0_3	=	0x0083
                    0084    277 _P0_4	=	0x0084
                    0085    278 _P0_5	=	0x0085
                    0086    279 _P0_6	=	0x0086
                    0087    280 _P0_7	=	0x0087
                    0088    281 _IT0	=	0x0088
                    0089    282 _IE0	=	0x0089
                    008A    283 _IT1	=	0x008a
                    008B    284 _IE1	=	0x008b
                    008C    285 _TR0	=	0x008c
                    008D    286 _TF0	=	0x008d
                    008E    287 _TR1	=	0x008e
                    008F    288 _TF1	=	0x008f
                    0090    289 _P1_0	=	0x0090
                    0091    290 _P1_1	=	0x0091
                    0092    291 _P1_2	=	0x0092
                    0093    292 _P1_3	=	0x0093
                    0094    293 _P1_4	=	0x0094
                    0095    294 _P1_5	=	0x0095
                    0096    295 _P1_6	=	0x0096
                    0097    296 _P1_7	=	0x0097
                    0098    297 _RI	=	0x0098
                    0099    298 _TI	=	0x0099
                    009A    299 _RB8	=	0x009a
                    009B    300 _TB8	=	0x009b
                    009C    301 _REN	=	0x009c
                    009D    302 _SM2	=	0x009d
                    009E    303 _SM1	=	0x009e
                    009F    304 _SM0	=	0x009f
                    00A0    305 _P2_0	=	0x00a0
                    00A1    306 _P2_1	=	0x00a1
                    00A2    307 _P2_2	=	0x00a2
                    00A3    308 _P2_3	=	0x00a3
                    00A4    309 _P2_4	=	0x00a4
                    00A5    310 _P2_5	=	0x00a5
                    00A6    311 _P2_6	=	0x00a6
                    00A7    312 _P2_7	=	0x00a7
                    00A8    313 _EX0	=	0x00a8
                    00A9    314 _ET0	=	0x00a9
                    00AA    315 _EX1	=	0x00aa
                    00AB    316 _ET1	=	0x00ab
                    00AC    317 _ES	=	0x00ac
                    00AF    318 _EA	=	0x00af
                    00B0    319 _P3_0	=	0x00b0
                    00B1    320 _P3_1	=	0x00b1
                    00B2    321 _P3_2	=	0x00b2
                    00B3    322 _P3_3	=	0x00b3
                    00B4    323 _P3_4	=	0x00b4
                    00B5    324 _P3_5	=	0x00b5
                    00B6    325 _P3_6	=	0x00b6
                    00B7    326 _P3_7	=	0x00b7
                    00B0    327 _RXD	=	0x00b0
                    00B1    328 _TXD	=	0x00b1
                    00B2    329 _INT0	=	0x00b2
                    00B3    330 _INT1	=	0x00b3
                    00B4    331 _T0	=	0x00b4
                    00B5    332 _T1	=	0x00b5
                    00B6    333 _WR	=	0x00b6
                    00B7    334 _RD	=	0x00b7
                    00B8    335 _PX0	=	0x00b8
                    00B9    336 _PT0	=	0x00b9
                    00BA    337 _PX1	=	0x00ba
                    00BB    338 _PT1	=	0x00bb
                    00BC    339 _PS	=	0x00bc
                    00D0    340 _P	=	0x00d0
                    00D1    341 _F1	=	0x00d1
                    00D2    342 _OV	=	0x00d2
                    00D3    343 _RS0	=	0x00d3
                    00D4    344 _RS1	=	0x00d4
                    00D5    345 _F0	=	0x00d5
                    00D6    346 _AC	=	0x00d6
                    00D7    347 _CY	=	0x00d7
                    00AD    348 _ET2	=	0x00ad
                    00BD    349 _PT2	=	0x00bd
                    00C8    350 _T2CON_0	=	0x00c8
                    00C9    351 _T2CON_1	=	0x00c9
                    00CA    352 _T2CON_2	=	0x00ca
                    00CB    353 _T2CON_3	=	0x00cb
                    00CC    354 _T2CON_4	=	0x00cc
                    00CD    355 _T2CON_5	=	0x00cd
                    00CE    356 _T2CON_6	=	0x00ce
                    00CF    357 _T2CON_7	=	0x00cf
                    00C8    358 _CP_RL2	=	0x00c8
                    00C9    359 _C_T2	=	0x00c9
                    00CA    360 _TR2	=	0x00ca
                    00CB    361 _EXEN2	=	0x00cb
                    00CC    362 _TCLK	=	0x00cc
                    00CD    363 _RCLK	=	0x00cd
                    00CE    364 _EXF2	=	0x00ce
                    00CF    365 _TF2	=	0x00cf
                    00DF    366 _CF	=	0x00df
                    00DE    367 _CR	=	0x00de
                    00DC    368 _CCF4	=	0x00dc
                    00DB    369 _CCF3	=	0x00db
                    00DA    370 _CCF2	=	0x00da
                    00D9    371 _CCF1	=	0x00d9
                    00D8    372 _CCF0	=	0x00d8
                    00AE    373 _EC	=	0x00ae
                    00EB    374 _EBO	=	0x00eb
                    00BE    375 _PPC	=	0x00be
                    00FB    376 _PBO	=	0x00fb
                    00C4    377 _WDOUT	=	0x00c4
                    00C3    378 _WDRE	=	0x00c3
                    00C2    379 _WDTS	=	0x00c2
                    00C1    380 _WDT	=	0x00c1
                    00C0    381 _SWDT	=	0x00c0
                            382 ;--------------------------------------------------------
                            383 ; overlayable register banks
                            384 ;--------------------------------------------------------
                            385 	.area REG_BANK_0	(REL,OVR,DATA)
   0000                     386 	.ds 8
                            387 ;--------------------------------------------------------
                            388 ; internal ram data
                            389 ;--------------------------------------------------------
                            390 	.area DSEG    (DATA)
                            391 ;--------------------------------------------------------
                            392 ; overlayable items in internal ram 
                            393 ;--------------------------------------------------------
                            394 	.area	OSEG    (OVR,DATA)
   0008                     395 _digitalwrite_PARM_2:
   0008                     396 	.ds 2
                            397 	.area	OSEG    (OVR,DATA)
                            398 	.area	OSEG    (OVR,DATA)
   0008                     399 _pinmode_PARM_2:
   0008                     400 	.ds 2
                            401 	.area	OSEG    (OVR,DATA)
                            402 	.area	OSEG    (OVR,DATA)
                            403 ;--------------------------------------------------------
                            404 ; Stack segment in internal ram 
                            405 ;--------------------------------------------------------
                            406 	.area	SSEG	(DATA)
   000A                     407 __start__stack:
   000A                     408 	.ds	1
                            409 
                            410 ;--------------------------------------------------------
                            411 ; indirectly addressable internal ram data
                            412 ;--------------------------------------------------------
                            413 	.area ISEG    (DATA)
                            414 ;--------------------------------------------------------
                            415 ; absolute internal ram data
                            416 ;--------------------------------------------------------
                            417 	.area IABS    (ABS,DATA)
                            418 	.area IABS    (ABS,DATA)
                            419 ;--------------------------------------------------------
                            420 ; bit data
                            421 ;--------------------------------------------------------
                            422 	.area BSEG    (BIT)
                            423 ;--------------------------------------------------------
                            424 ; paged external ram data
                            425 ;--------------------------------------------------------
                            426 	.area PSEG    (PAG,XDATA)
                            427 ;--------------------------------------------------------
                            428 ; external ram data
                            429 ;--------------------------------------------------------
                            430 	.area XSEG    (XDATA)
                            431 ;--------------------------------------------------------
                            432 ; absolute external ram data
                            433 ;--------------------------------------------------------
                            434 	.area XABS    (ABS,XDATA)
                            435 ;--------------------------------------------------------
                            436 ; external initialized ram data
                            437 ;--------------------------------------------------------
                            438 	.area XISEG   (XDATA)
                            439 	.area HOME    (CODE)
                            440 	.area GSINIT0 (CODE)
                            441 	.area GSINIT1 (CODE)
                            442 	.area GSINIT2 (CODE)
                            443 	.area GSINIT3 (CODE)
                            444 	.area GSINIT4 (CODE)
                            445 	.area GSINIT5 (CODE)
                            446 	.area GSINIT  (CODE)
                            447 	.area GSFINAL (CODE)
                            448 	.area CSEG    (CODE)
                            449 ;--------------------------------------------------------
                            450 ; interrupt vector 
                            451 ;--------------------------------------------------------
                            452 	.area HOME    (CODE)
   0000                     453 __interrupt_vect:
   0000 02 00 08            454 	ljmp	__sdcc_gsinit_startup
                            455 ;--------------------------------------------------------
                            456 ; global & static initialisations
                            457 ;--------------------------------------------------------
                            458 	.area HOME    (CODE)
                            459 	.area GSINIT  (CODE)
                            460 	.area GSFINAL (CODE)
                            461 	.area GSINIT  (CODE)
                            462 	.globl __sdcc_gsinit_startup
                            463 	.globl __sdcc_program_startup
                            464 	.globl __start__stack
                            465 	.globl __mcs51_genXINIT
                            466 	.globl __mcs51_genXRAMCLEAR
                            467 	.globl __mcs51_genRAMCLEAR
                            468 	.area GSFINAL (CODE)
   0061 02 00 03            469 	ljmp	__sdcc_program_startup
                            470 ;--------------------------------------------------------
                            471 ; Home
                            472 ;--------------------------------------------------------
                            473 	.area HOME    (CODE)
                            474 	.area HOME    (CODE)
   0003                     475 __sdcc_program_startup:
   0003 12 00 EB            476 	lcall	_main
                            477 ;	return from main will lock up
   0006 80 FE               478 	sjmp .
                            479 ;--------------------------------------------------------
                            480 ; code
                            481 ;--------------------------------------------------------
                            482 	.area CSEG    (CODE)
                            483 ;------------------------------------------------------------
                            484 ;Allocation info for local variables in function 'digitalwrite'
                            485 ;------------------------------------------------------------
                            486 ;state                     Allocated with name '_digitalwrite_PARM_2'
                            487 ;output                    Allocated to registers 
                            488 ;------------------------------------------------------------
                            489 ;	/home/krish/work/Neo51-ide/tools/bin/../share/sdcc/include/mcs51/digitalw.c:22: void digitalwrite(int output,int state)
                            490 ;	-----------------------------------------
                            491 ;	 function digitalwrite
                            492 ;	-----------------------------------------
   0064                     493 _digitalwrite:
                    0007    494 	ar7 = 0x07
                    0006    495 	ar6 = 0x06
                    0005    496 	ar5 = 0x05
                    0004    497 	ar4 = 0x04
                    0003    498 	ar3 = 0x03
                    0002    499 	ar2 = 0x02
                    0001    500 	ar1 = 0x01
                    0000    501 	ar0 = 0x00
                            502 ;	/home/krish/work/Neo51-ide/tools/bin/../share/sdcc/include/mcs51/digitalw.c:46: }
   0064 22                  503 	ret
                            504 ;------------------------------------------------------------
                            505 ;Allocation info for local variables in function 'digitalread'
                            506 ;------------------------------------------------------------
                            507 ;input                     Allocated to registers 
                            508 ;------------------------------------------------------------
                            509 ;	/home/krish/work/Neo51-ide/tools/bin/../share/sdcc/include/mcs51/digitalw.c:48: int digitalread(int input)
                            510 ;	-----------------------------------------
                            511 ;	 function digitalread
                            512 ;	-----------------------------------------
   0065                     513 _digitalread:
                            514 ;	/home/krish/work/Neo51-ide/tools/bin/../share/sdcc/include/mcs51/digitalw.c:73: }
   0065 22                  515 	ret
                            516 ;------------------------------------------------------------
                            517 ;Allocation info for local variables in function 'pinmode'
                            518 ;------------------------------------------------------------
                            519 ;state                     Allocated with name '_pinmode_PARM_2'
                            520 ;input                     Allocated to registers 
                            521 ;------------------------------------------------------------
                            522 ;	/home/krish/work/Neo51-ide/tools/bin/../share/sdcc/include/mcs51/digitalw.c:75: void pinmode(int input, int state)
                            523 ;	-----------------------------------------
                            524 ;	 function pinmode
                            525 ;	-----------------------------------------
   0066                     526 _pinmode:
                            527 ;	/home/krish/work/Neo51-ide/tools/bin/../share/sdcc/include/mcs51/digitalw.c:99: }
   0066 22                  528 	ret
                            529 ;------------------------------------------------------------
                            530 ;Allocation info for local variables in function 'Delayms'
                            531 ;------------------------------------------------------------
                            532 ;milliseconde              Allocated to registers r4 r5 r6 r7 
                            533 ;i                         Allocated to registers r0 r1 r2 r3 
                            534 ;------------------------------------------------------------
                            535 ;	/home/krish/work/Neo51-ide/tools/bin/../share/sdcc/include/mcs51/arduinodelay.c:8: void Delayms(unsigned long milliseconde)
                            536 ;	-----------------------------------------
                            537 ;	 function Delayms
                            538 ;	-----------------------------------------
   0067                     539 _Delayms:
   0067 AC 82               540 	mov	r4,dpl
   0069 AD 83               541 	mov	r5,dph
   006B AE F0               542 	mov	r6,b
   006D FF                  543 	mov	r7,a
                            544 ;	/home/krish/work/Neo51-ide/tools/bin/../share/sdcc/include/mcs51/arduinodelay.c:12: for (i=0;i<milliseconde;i++);
   006E 78 00               545 	mov	r0,#0x00
   0070 79 00               546 	mov	r1,#0x00
   0072 7A 00               547 	mov	r2,#0x00
   0074 7B 00               548 	mov	r3,#0x00
   0076                     549 00101$:
   0076 C3                  550 	clr	c
   0077 E8                  551 	mov	a,r0
   0078 9C                  552 	subb	a,r4
   0079 E9                  553 	mov	a,r1
   007A 9D                  554 	subb	a,r5
   007B EA                  555 	mov	a,r2
   007C 9E                  556 	subb	a,r6
   007D EB                  557 	mov	a,r3
   007E 9F                  558 	subb	a,r7
   007F 50 0F               559 	jnc	00105$
   0081 08                  560 	inc	r0
   0082 B8 00 09            561 	cjne	r0,#0x00,00113$
   0085 09                  562 	inc	r1
   0086 B9 00 05            563 	cjne	r1,#0x00,00113$
   0089 0A                  564 	inc	r2
   008A BA 00 E9            565 	cjne	r2,#0x00,00101$
   008D 0B                  566 	inc	r3
   008E                     567 00113$:
   008E 80 E6               568 	sjmp	00101$
   0090                     569 00105$:
   0090 22                  570 	ret
                            571 ;------------------------------------------------------------
                            572 ;Allocation info for local variables in function 'Delayus'
                            573 ;------------------------------------------------------------
                            574 ;microsecondes             Allocated to registers r6 r7 
                            575 ;i                         Allocated to registers r4 r5 
                            576 ;------------------------------------------------------------
                            577 ;	/home/krish/work/Neo51-ide/tools/bin/../share/sdcc/include/mcs51/arduinodelay.c:15: void Delayus(int microsecondes)
                            578 ;	-----------------------------------------
                            579 ;	 function Delayus
                            580 ;	-----------------------------------------
   0091                     581 _Delayus:
   0091 AE 82               582 	mov	r6,dpl
   0093 AF 83               583 	mov	r7,dph
                            584 ;	/home/krish/work/Neo51-ide/tools/bin/../share/sdcc/include/mcs51/arduinodelay.c:19: for (i=0;i<microsecondes;i++);
   0095 7C 00               585 	mov	r4,#0x00
   0097 7D 00               586 	mov	r5,#0x00
   0099                     587 00101$:
   0099 8E 02               588 	mov	ar2,r6
   009B 8F 03               589 	mov	ar3,r7
   009D C3                  590 	clr	c
   009E EC                  591 	mov	a,r4
   009F 9A                  592 	subb	a,r2
   00A0 ED                  593 	mov	a,r5
   00A1 9B                  594 	subb	a,r3
   00A2 50 07               595 	jnc	00105$
   00A4 0C                  596 	inc	r4
   00A5 BC 00 F1            597 	cjne	r4,#0x00,00101$
   00A8 0D                  598 	inc	r5
   00A9 80 EE               599 	sjmp	00101$
   00AB                     600 00105$:
   00AB 22                  601 	ret
                            602 ;------------------------------------------------------------
                            603 ;Allocation info for local variables in function 'setup'
                            604 ;------------------------------------------------------------
                            605 ;	/home/krish/work/Neo51-ide/source/user.c:4: void setup(void)
                            606 ;	-----------------------------------------
                            607 ;	 function setup
                            608 ;	-----------------------------------------
   00AC                     609 _setup:
                            610 ;	/home/krish/work/Neo51-ide/source/user.c:6: pinmode(0,OUTPUT);	// test caractères
   00AC E4                  611 	clr	a
   00AD F5 08               612 	mov	_pinmode_PARM_2,a
   00AF F5 09               613 	mov	(_pinmode_PARM_2 + 1),a
   00B1 F5 82               614 	mov	dpl,a
   00B3 F5 83               615 	mov	dph,a
   00B5 02 00 66            616 	ljmp	_pinmode
                            617 ;------------------------------------------------------------
                            618 ;Allocation info for local variables in function 'loop'
                            619 ;------------------------------------------------------------
                            620 ;	/home/krish/work/Neo51-ide/source/user.c:9: void loop(void)
                            621 ;	-----------------------------------------
                            622 ;	 function loop
                            623 ;	-----------------------------------------
   00B8                     624 _loop:
                            625 ;	/home/krish/work/Neo51-ide/source/user.c:11: digitalwrite(0,HIGH); 
   00B8 75 08 01            626 	mov	_digitalwrite_PARM_2,#0x01
   00BB 75 09 00            627 	mov	(_digitalwrite_PARM_2 + 1),#0x00
   00BE 90 00 00            628 	mov	dptr,#0x0000
   00C1 12 00 64            629 	lcall	_digitalwrite
                            630 ;	/home/krish/work/Neo51-ide/source/user.c:12: Delayms(500);
   00C4 90 01 F4            631 	mov	dptr,#0x01F4
   00C7 E4                  632 	clr	a
   00C8 F5 F0               633 	mov	b,a
   00CA 12 00 67            634 	lcall	_Delayms
                            635 ;	/home/krish/work/Neo51-ide/source/user.c:13: digitalwrite(0,LOW);
   00CD E4                  636 	clr	a
   00CE F5 08               637 	mov	_digitalwrite_PARM_2,a
   00D0 F5 09               638 	mov	(_digitalwrite_PARM_2 + 1),a
   00D2 F5 82               639 	mov	dpl,a
   00D4 F5 83               640 	mov	dph,a
   00D6 12 00 64            641 	lcall	_digitalwrite
                            642 ;	/home/krish/work/Neo51-ide/source/user.c:14: Delayms(500);
   00D9 90 01 F4            643 	mov	dptr,#0x01F4
   00DC E4                  644 	clr	a
   00DD F5 F0               645 	mov	b,a
   00DF 12 00 67            646 	lcall	_Delayms
                            647 ;	/home/krish/work/Neo51-ide/source/user.c:15: Delayms(500);
   00E2 90 01 F4            648 	mov	dptr,#0x01F4
   00E5 E4                  649 	clr	a
   00E6 F5 F0               650 	mov	b,a
   00E8 02 00 67            651 	ljmp	_Delayms
                            652 ;------------------------------------------------------------
                            653 ;Allocation info for local variables in function 'main'
                            654 ;------------------------------------------------------------
                            655 ;	/home/krish/work/Neo51-ide/source/main.c:5: void main()
                            656 ;	-----------------------------------------
                            657 ;	 function main
                            658 ;	-----------------------------------------
   00EB                     659 _main:
                            660 ;	/home/krish/work/Neo51-ide/source/main.c:8: setup();
   00EB 12 00 AC            661 	lcall	_setup
                            662 ;	/home/krish/work/Neo51-ide/source/main.c:10: while(1)
   00EE                     663 00102$:
                            664 ;	/home/krish/work/Neo51-ide/source/main.c:11: loop();
   00EE 12 00 B8            665 	lcall	_loop
   00F1 80 FB               666 	sjmp	00102$
                            667 	.area CSEG    (CODE)
                            668 	.area CONST   (CODE)
                            669 	.area XINIT   (CODE)
                            670 	.area CABS    (ABS,CODE)
