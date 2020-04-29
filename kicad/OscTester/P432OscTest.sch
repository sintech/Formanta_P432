EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Formanta P432 Oscillator tester"
Date "2020-03-31"
Rev ""
Comp ""
Comment1 "By SinTech"
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector_Generic:Conn_01x08 J4
U 1 1 5E6BAF7F
P 1000 3750
F 0 "J4" H 1000 4150 50  0000 C CNN
F 1 "Volume-XP6" H 1000 3250 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x08_P2.54mm_Vertical" H 1000 3750 50  0001 C CNN
F 3 "~" H 1000 3750 50  0001 C CNN
	1    1000 3750
	-1   0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x08 J3
U 1 1 5E6BBC8E
P 1000 4800
F 0 "J3" H 1000 5200 50  0000 C CNN
F 1 "Filter-XP7" H 1000 4300 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x08_P2.54mm_Vertical" H 1000 4800 50  0001 C CNN
F 3 "~" H 1000 4800 50  0001 C CNN
	1    1000 4800
	-1   0    0    -1  
$EndComp
Text Label 1300 5700 2    50   ~ 0
Q1
Text Label 1300 5800 2    50   ~ 0
Q0
Text Label 1300 5900 2    50   ~ 0
F1
Text Label 1300 6000 2    50   ~ 0
F0
Text Label 1300 6100 2    50   ~ 0
S2
Text Label 1300 6200 2    50   ~ 0
S1
Text Label 1300 6300 2    50   ~ 0
S0
Wire Wire Line
	1200 6300 1600 6300
Wire Wire Line
	1600 6200 1200 6200
Wire Wire Line
	1200 6100 1600 6100
Wire Wire Line
	1600 6000 1200 6000
Wire Wire Line
	1200 5900 1600 5900
Wire Wire Line
	1600 5800 1200 5800
Wire Wire Line
	1200 5700 1600 5700
Wire Wire Line
	1600 5600 1200 5600
$Comp
L Connector_Generic:Conn_01x08 J5
U 1 1 5E687A3A
P 1000 5900
F 0 "J5" H 1000 6300 50  0000 C CNN
F 1 "Control-XP5" H 1000 5400 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x08_P2.54mm_Vertical" H 1000 5900 50  0001 C CNN
F 3 "~" H 1000 5900 50  0001 C CNN
	1    1000 5900
	-1   0    0    -1  
$EndComp
Text Label 1200 2700 0    50   ~ 0
FC4
Text Label 1200 2800 0    50   ~ 0
FC10
Text Label 1200 2900 0    50   ~ 0
FC9
Text Label 1200 3000 0    50   ~ 0
FC8
Text Label 1200 2600 0    50   ~ 0
FC5
Text Label 1200 2500 0    50   ~ 0
FC6
Text Label 1200 2400 0    50   ~ 0
FC7
Text Label 1200 2300 0    50   ~ 0
FC0
Text Label 1200 2200 0    50   ~ 0
FC1
Text Label 1200 2100 0    50   ~ 0
FC2
Text Label 1200 2000 0    50   ~ 0
FC3
$Comp
L Connector_Generic:Conn_01x11 J2
U 1 1 5E68560B
P 1000 2500
F 0 "J2" H 1000 3100 50  0000 C CNN
F 1 "Freq-XP1" H 1000 1900 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x11_P2.54mm_Vertical" H 1000 2500 50  0001 C CNN
F 3 "~" H 1000 2500 50  0001 C CNN
	1    1000 2500
	-1   0    0    -1  
$EndComp
Wire Wire Line
	1200 3000 1650 3000
Wire Wire Line
	1650 2900 1200 2900
Wire Wire Line
	1200 2800 1650 2800
Wire Wire Line
	1650 2700 1200 2700
Wire Wire Line
	1200 2600 1650 2600
Wire Wire Line
	1650 2500 1200 2500
Wire Wire Line
	1200 2400 1650 2400
Wire Wire Line
	1200 2200 1800 2200
Wire Wire Line
	1200 2100 1600 2100
Wire Wire Line
	1200 2000 1400 2000
Wire Wire Line
	1600 1900 1600 2100
Wire Wire Line
	1800 1900 1800 2200
Wire Wire Line
	2000 1900 2000 2300
Wire Wire Line
	2000 2300 1200 2300
Wire Wire Line
	1650 2400 1650 2500
Connection ~ 1650 2500
Wire Wire Line
	1650 2500 1650 2600
Connection ~ 1650 2600
Wire Wire Line
	1650 2600 1650 2700
Connection ~ 1650 2700
Wire Wire Line
	1650 2700 1650 2800
Connection ~ 1650 2800
Wire Wire Line
	1650 2800 1650 2900
Connection ~ 1650 2900
Wire Wire Line
	1650 2900 1650 3000
$Comp
L power:GND #PWR04
U 1 1 5E8936EA
P 1650 3050
F 0 "#PWR04" H 1650 2800 50  0001 C CNN
F 1 "GND" H 1650 2900 50  0000 C CNN
F 2 "" H 1650 3050 50  0001 C CNN
F 3 "" H 1650 3050 50  0001 C CNN
	1    1650 3050
	1    0    0    -1  
$EndComp
Wire Wire Line
	1650 3050 1650 3000
Connection ~ 1650 3000
Wire Wire Line
	1600 6350 1600 6300
Connection ~ 1600 5800
Wire Wire Line
	1600 5800 1600 5700
Connection ~ 1600 5900
Wire Wire Line
	1600 5900 1600 5800
Connection ~ 1600 6000
Wire Wire Line
	1600 6000 1600 5900
Connection ~ 1600 6100
Wire Wire Line
	1600 6100 1600 6000
Connection ~ 1600 6200
Wire Wire Line
	1600 6200 1600 6100
Connection ~ 1600 6300
Wire Wire Line
	1600 6300 1600 6200
$Comp
L power:GND #PWR010
U 1 1 5E8FA2FD
P 1600 6350
F 0 "#PWR010" H 1600 6100 50  0001 C CNN
F 1 "GND" H 1600 6200 50  0000 C CNN
F 2 "" H 1600 6350 50  0001 C CNN
F 3 "" H 1600 6350 50  0001 C CNN
	1    1600 6350
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 5E8FA940
P 1400 1750
F 0 "R1" V 1480 1750 50  0000 C CNN
F 1 "220" V 1400 1750 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric" V 1330 1750 50  0001 C CNN
F 3 "~" H 1400 1750 50  0001 C CNN
	1    1400 1750
	-1   0    0    1   
$EndComp
$Comp
L Device:R R2
U 1 1 5E8FB99E
P 1600 1750
F 0 "R2" V 1680 1750 50  0000 C CNN
F 1 "220" V 1600 1750 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric" V 1530 1750 50  0001 C CNN
F 3 "~" H 1600 1750 50  0001 C CNN
	1    1600 1750
	-1   0    0    1   
$EndComp
$Comp
L Device:R R3
U 1 1 5E8FBB02
P 1800 1750
F 0 "R3" V 1880 1750 50  0000 C CNN
F 1 "220" V 1800 1750 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric" V 1730 1750 50  0001 C CNN
F 3 "~" H 1800 1750 50  0001 C CNN
	1    1800 1750
	-1   0    0    1   
$EndComp
$Comp
L Device:R R4
U 1 1 5E8FBD18
P 2000 1750
F 0 "R4" V 2080 1750 50  0000 C CNN
F 1 "220" V 2000 1750 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric" V 1930 1750 50  0001 C CNN
F 3 "~" H 2000 1750 50  0001 C CNN
	1    2000 1750
	-1   0    0    1   
$EndComp
Wire Wire Line
	1400 1600 1400 1550
Wire Wire Line
	2000 1600 2000 1550
Wire Wire Line
	1800 1600 1800 1550
Wire Wire Line
	1600 1600 1600 1550
Wire Wire Line
	1200 4500 1650 4500
Wire Wire Line
	1650 4500 1650 4600
Wire Wire Line
	1650 5200 1200 5200
Wire Wire Line
	1200 5100 1650 5100
Connection ~ 1650 5100
Wire Wire Line
	1650 5100 1650 5200
Wire Wire Line
	1200 5000 1650 5000
Connection ~ 1650 5000
Wire Wire Line
	1650 5000 1650 5100
Wire Wire Line
	1200 4900 1650 4900
Connection ~ 1650 4900
Wire Wire Line
	1650 4900 1650 5000
Wire Wire Line
	1200 4800 1650 4800
Connection ~ 1650 4800
Wire Wire Line
	1650 4800 1650 4850
Wire Wire Line
	1200 4700 1650 4700
Connection ~ 1650 4700
Wire Wire Line
	1650 4700 1650 4800
Wire Wire Line
	1200 4600 1650 4600
Connection ~ 1650 4600
Wire Wire Line
	1650 4600 1650 4700
Wire Wire Line
	1650 4850 1800 4850
Connection ~ 1650 4850
Wire Wire Line
	1650 4850 1650 4900
$Comp
L power:GND #PWR06
U 1 1 5E9907C0
P 1950 5150
F 0 "#PWR06" H 1950 4900 50  0001 C CNN
F 1 "GND" H 1950 5000 50  0000 C CNN
F 2 "" H 1950 5150 50  0001 C CNN
F 3 "" H 1950 5150 50  0001 C CNN
	1    1950 5150
	1    0    0    -1  
$EndComp
Wire Wire Line
	1950 5100 1950 5150
$Comp
L power:+5V #PWR05
U 1 1 5E998FB7
P 1950 4550
F 0 "#PWR05" H 1950 4400 50  0001 C CNN
F 1 "+5V" H 1950 4690 50  0000 C CNN
F 2 "" H 1950 4550 50  0001 C CNN
F 3 "" H 1950 4550 50  0001 C CNN
	1    1950 4550
	1    0    0    -1  
$EndComp
Wire Wire Line
	1950 4600 1950 4550
Wire Wire Line
	1200 3450 1650 3450
Wire Wire Line
	1650 3450 1650 3550
Wire Wire Line
	1650 4150 1200 4150
Wire Wire Line
	1200 4050 1650 4050
Connection ~ 1650 4050
Wire Wire Line
	1650 4050 1650 4150
Wire Wire Line
	1200 3950 1650 3950
Connection ~ 1650 3950
Wire Wire Line
	1650 3950 1650 4050
Wire Wire Line
	1200 3850 1650 3850
Connection ~ 1650 3850
Wire Wire Line
	1650 3850 1650 3950
Wire Wire Line
	1200 3750 1650 3750
Connection ~ 1650 3750
Wire Wire Line
	1650 3750 1650 3800
Wire Wire Line
	1200 3650 1650 3650
Connection ~ 1650 3650
Wire Wire Line
	1650 3650 1650 3750
Wire Wire Line
	1200 3550 1650 3550
Connection ~ 1650 3550
Wire Wire Line
	1650 3550 1650 3650
Wire Wire Line
	1650 3800 1800 3800
Connection ~ 1650 3800
Wire Wire Line
	1650 3800 1650 3850
Wire Notes Line
	3500 1700 4100 1700
Text Notes 4200 1750 0    50   ~ 10
Frequency
Text Notes 3550 1800 0    50   ~ 10
1
Text Notes 3700 1800 0    50   ~ 10
2
Text Notes 3850 1800 0    50   ~ 10
3
Text Notes 4000 1800 0    50   ~ 10
4
Wire Notes Line
	3500 1850 4750 1850
Wire Wire Line
	1400 1550 1600 1550
Connection ~ 1600 1550
Wire Wire Line
	1600 1550 1800 1550
Connection ~ 1800 1550
Wire Wire Line
	1800 1550 2000 1550
Wire Wire Line
	1200 1100 1400 1100
Connection ~ 1400 1200
Wire Wire Line
	1400 1100 1400 1200
Wire Wire Line
	1400 1200 1400 1250
Wire Wire Line
	1200 1200 1400 1200
$Comp
L power:GND #PWR02
U 1 1 5E82D822
P 1400 1250
F 0 "#PWR02" H 1400 1000 50  0001 C CNN
F 1 "GND" H 1400 1100 50  0000 C CNN
F 2 "" H 1400 1250 50  0001 C CNN
F 3 "" H 1400 1250 50  0001 C CNN
	1    1400 1250
	1    0    0    -1  
$EndComp
Wire Wire Line
	1400 900  1400 850 
Connection ~ 1400 900 
Wire Wire Line
	1200 900  1400 900 
Wire Wire Line
	1400 1000 1400 900 
Wire Wire Line
	1200 1000 1400 1000
$Comp
L power:+5V #PWR01
U 1 1 5E827480
P 1400 850
F 0 "#PWR01" H 1400 700 50  0001 C CNN
F 1 "+5V" H 1400 990 50  0000 C CNN
F 2 "" H 1400 850 50  0001 C CNN
F 3 "" H 1400 850 50  0001 C CNN
	1    1400 850 
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x04 J1
U 1 1 5E812DC8
P 1000 1000
F 0 "J1" H 1000 1200 50  0000 C CNN
F 1 "Power-XP6" H 1000 700 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x04_P2.54mm_Vertical" H 1000 1000 50  0001 C CNN
F 3 "~" H 1000 1000 50  0001 C CNN
	1    1000 1000
	-1   0    0    -1  
$EndComp
Wire Wire Line
	1400 1900 1400 2000
$Comp
L Jumper:Jumper_3_Bridged12 JP2
U 1 1 5E8BE8F9
P 1950 4850
F 0 "JP2" V 2050 4750 50  0000 C CNN
F 1 "Filter off/on" H 1950 4960 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 1950 4850 50  0001 C CNN
F 3 "~" H 1950 4850 50  0001 C CNN
	1    1950 4850
	0    1    -1   0   
$EndComp
$Comp
L power:GND #PWR08
U 1 1 5E8D20A0
P 1950 4100
F 0 "#PWR08" H 1950 3850 50  0001 C CNN
F 1 "GND" H 1950 3950 50  0000 C CNN
F 2 "" H 1950 4100 50  0001 C CNN
F 3 "" H 1950 4100 50  0001 C CNN
	1    1950 4100
	1    0    0    -1  
$EndComp
Wire Wire Line
	1950 4050 1950 4100
$Comp
L power:+5V #PWR07
U 1 1 5E8D20A7
P 1950 3500
F 0 "#PWR07" H 1950 3350 50  0001 C CNN
F 1 "+5V" H 1950 3640 50  0000 C CNN
F 2 "" H 1950 3500 50  0001 C CNN
F 3 "" H 1950 3500 50  0001 C CNN
	1    1950 3500
	1    0    0    -1  
$EndComp
Wire Wire Line
	1950 3550 1950 3500
$Comp
L Jumper:Jumper_3_Bridged12 JP1
U 1 1 5E8D20AE
P 1950 3800
F 0 "JP1" V 2050 3700 50  0000 C CNN
F 1 "Volume off/on" H 1950 3910 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 1950 3800 50  0001 C CNN
F 3 "~" H 1950 3800 50  0001 C CNN
	1    1950 3800
	0    1    -1   0   
$EndComp
Text Notes 3550 2000 0    50   ~ 0
0
Text Notes 3700 2000 0    50   ~ 0
0
Text Notes 4000 2000 0    50   ~ 0
0
Text Notes 4200 2000 0    50   ~ 0
33 Hz
Text Notes 3550 2150 0    50   ~ 0
0
Text Notes 3700 2150 0    50   ~ 0
1
Text Notes 4200 2150 0    50   ~ 0
65 Hz
Wire Notes Line
	3500 2200 4750 2200
Wire Notes Line
	3500 2050 4750 2050
Wire Notes Line
	3500 2350 4750 2350
Text Notes 4200 2300 0    50   ~ 0
127 Hz
Text Notes 3550 2300 0    50   ~ 0
0
Text Notes 4000 2300 0    50   ~ 0
1
Text Notes 3850 2150 0    50   ~ 0
1
Text Notes 4000 2150 0    50   ~ 0
0
Wire Notes Line
	3500 2500 4750 2500
Wire Notes Line
	3500 2650 4750 2650
Text Notes 4200 2450 0    50   ~ 0
250 Hz
Text Notes 3700 2450 0    50   ~ 0
1
Text Notes 3550 2450 0    50   ~ 0
0
Text Notes 3850 2450 0    50   ~ 0
0
Text Notes 4000 2450 0    50   ~ 0
1
Wire Notes Line
	3500 2800 4750 2800
Text Notes 4200 2600 0    50   ~ 0
500 Hz
Text Notes 3550 2600 0    50   ~ 0
0
Text Notes 4000 2600 0    50   ~ 0
1
Text Notes 4200 2750 0    50   ~ 0
1000 Hz
Text Notes 3700 2750 0    50   ~ 0
1
Text Notes 3550 2750 0    50   ~ 0
0
Text Notes 4000 2750 0    50   ~ 0
1
Text Notes 4200 2900 0    50   ~ 0
1122 Hz
Text Notes 3850 2900 0    50   ~ 0
1
Text Notes 4000 2900 0    50   ~ 0
1
Text Notes 3700 2300 0    50   ~ 0
0
Text Notes 3850 2300 0    50   ~ 0
0
Wire Notes Line
	3500 1900 4750 1900
Text Notes 3700 2600 0    50   ~ 0
0
Text Notes 3500 3050 0    50   ~ 0
First set 0111, tune to 1000 Hz.
Text Notes 3600 1700 0    50   ~ 10
DIP-Code
Wire Notes Line
	3500 1600 4750 1600
Wire Wire Line
	1600 5600 1600 5700
Connection ~ 1600 5700
Connection ~ 1400 2000
Connection ~ 1600 2100
Connection ~ 1800 2200
Connection ~ 2000 2300
Connection ~ 2000 1550
Connection ~ 1650 2400
Text Notes 2300 1800 1    50   ~ 10
Code
Wire Notes Line
	2200 1550 2200 2350
Wire Notes Line
	2200 1850 2350 1850
Wire Notes Line
	2350 1550 2200 1550
Wire Notes Line
	2350 2350 2350 1550
Wire Notes Line
	2200 2350 2350 2350
Text Label 2250 2000 0    59   ~ 0
4
Text Label 2250 2100 0    59   ~ 0
3
Text Label 2250 2200 0    59   ~ 0
2
Text Label 2250 2300 0    59   ~ 0
1
Wire Wire Line
	2300 2000 1400 2000
Wire Wire Line
	2300 2100 1600 2100
Wire Wire Line
	2300 2200 1800 2200
Wire Wire Line
	2000 2300 2300 2300
Wire Wire Line
	2000 1550 2150 1550
Wire Wire Line
	2150 2400 1650 2400
Wire Wire Line
	2150 1550 2150 2400
Connection ~ 3050 2200
Wire Wire Line
	3050 2300 3050 2200
Wire Wire Line
	2900 2300 3050 2300
Wire Wire Line
	2900 2200 3050 2200
Connection ~ 3050 2100
Wire Wire Line
	3050 2200 3050 2100
Connection ~ 3050 2000
Wire Wire Line
	3050 2100 3050 2000
Wire Wire Line
	2900 2100 3050 2100
Wire Wire Line
	3050 2000 3050 1900
Wire Wire Line
	2900 2000 3050 2000
$Comp
L power:+5V #PWR03
U 1 1 5E9BDAFE
P 3050 1900
F 0 "#PWR03" H 3050 1750 50  0001 C CNN
F 1 "+5V" H 3050 2040 50  0000 C CNN
F 2 "" H 3050 1900 50  0001 C CNN
F 3 "" H 3050 1900 50  0001 C CNN
	1    3050 1900
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_DIP_x04 SW1
U 1 1 5E857AA0
P 2600 2100
F 0 "SW1" H 2600 1850 50  0000 C CNN
F 1 "SW_DIP_x04" H 2600 2450 50  0000 C CNN
F 2 "Button_Switch_THT:SW_DIP_SPSTx04_Slide_9.78x12.34mm_W7.62mm_P2.54mm" H 2600 2100 50  0001 C CNN
F 3 "~" H 2600 2100 50  0001 C CNN
	1    2600 2100
	-1   0    0    1   
$EndComp
Text Label 1450 5600 2    50   ~ 0
Unison
Text Notes 3850 2000 0    50   ~ 0
1
Text Notes 3850 2600 0    50   ~ 0
1
Text Notes 3850 2750 0    50   ~ 0
1
Text Notes 3700 2900 0    50   ~ 0
1
Text Notes 3550 2900 0    50   ~ 0
1
Wire Notes Line
	3500 2950 3500 1600
Wire Notes Line
	4750 1600 4750 2950
Wire Notes Line
	3500 2950 4750 2950
Wire Notes Line
	3650 1700 3650 2950
Wire Notes Line
	3950 1700 3950 2950
Wire Notes Line
	3800 1700 3800 2950
Wire Notes Line
	4100 2950 4100 1600
$EndSCHEMATC
