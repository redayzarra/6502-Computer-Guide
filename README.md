# 6502 Computer Guide

## Introduction
Welcome to the guide for building [Ben Eater](https://eater.net/)'s 6502 computer using his [custom kit](https://eater.net/6502). In this guide, you'll learn step-by-step how to assemble the hardware, understand the workings of the 6502 microprocessor, and run simple programs on your own 6502-based computer. 
This is simply to help others for their projects if they are facing issues.

## Prerequisites
Before you begin, make sure you have the following:
- Basic understanding of electronics and circuit design
- Tools: Wire strippers, power supply (5 volts), multimeter
- Ben Eater’s 6502 computer kit

## Unboxing and Inventory
When you receive your kit, ensure you have all the necessary components:
- 6502 microprocessor
- RAM and ROM chips
- Clock module components
- Breadboards and connecting wires
- Power supply components
- Additional ICs for address decoding and I/O
- LEDs, resistors, and capacitors

<div align="center">
 
  <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/82bf0d62-8094-46b3-9c5d-a1ea7e716009" alt="Labeled Parts">

</div>

## Understanding the 6502 Microprocessor
The 6502 microprocessor was a popular chip in the 1970s, used in many famous computers like the Apple I and Commodore 64. It features:
- 8-bit data bus
- 16-bit address bus
- Data sheet (30 pages)

## Step-by-Step Assembly Instructions

This section meticulously breaks down each phase of the assembly process into clear, manageable steps. Starting with organizing your components, you'll move on to setting up your breadboards, wiring the CPU and support chips, and then proceed to connecting memory and I/O devices.

### 1. Connect the 6502 Microprocessor to Power

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/7a01b0e3-954c-416e-8790-4596a82aa116" alt="Datasheet diagram of 6502 Microprocessor" height="350"><br>
        <figcaption>Figure 3-1 W65C02S 40 Pin PDIP Pinout</figcaption>
      </td>
      <td align="center" >
        <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/614dc660-b828-47a7-9604-6b40eb56a532" alt="6502 Microprocessor on breadboard" height="350"><br>
        <figcaption>Connect VDD to positive power, and VSS to ground</figcaption>
      </td>
    </tr>
  </table>
</div>

### 2. Connecting Input Pins

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/7a01b0e3-954c-416e-8790-4596a82aa116" alt="Datasheet diagram of 6502 Microprocessor" height="350"><br>
        <figcaption>Figure 3-1 W65C02S 40 Pin PDIP Pinout</figcaption>
      </td>
      <td align="center" >
        <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/e5007ef8-211d-4549-bb34-91eba05b8ea5" alt="6502 Microprocessor connected to input pins" height="350"><br>
        <figcaption>Connecting input pins, see below</figcaption>
      </td>
    </tr>
  </table>
</div>

#### Pins Explained (✔= Connect)

**#1: VPB** - Vector Pull output indicates when interrupt vectors are being addressed

**#2: RDY ✔** - Ready (low input logic) will halt the microprocessor in its current state

**#3: PHI1O** - Phase 1 Out is the inverted PHI2 signal

**#4: IRQB ✔** - Interrupt Request input signal to initiate an interrupt sequence

**#5: MLB** - Memory Lock output to ensure the integrity of Read-Modify-Write instructions in multiprocessor systems

**#6: NMIB ✔** - Non-Maskable Interrupt input initiates an interrupt sequence on a negative transition

**#7: SYNC** - Synchronize output indicates OpCode fetch cycle

**#8: VDD ✔** - Positive power supply voltage

**#9: A0** - Address Bus line 0 used to address memory and I/O registers

**#10: A1** - Address Bus line 1 used to address memory and I/O registers

**#11: A2** - Address Bus line 2 used to address memory and I/O registers

**#12: A3** - Address Bus line 3 used to address memory and I/O registers

**#13: A4** - Address Bus line 4 used to address memory and I/O registers

**#14: A5** - Address Bus line 5 used to address memory and I/O registers

**#15: A6** - Address Bus line 6 used to address memory and I/O registers

**#16: A7** - Address Bus line 7 used to address memory and I/O registers

**#17: A8** - Address Bus line 8 used to address memory and I/O registers

**#18: A9** - Address Bus line 9 used to address memory and I/O registers

**#19: A10** - Address Bus line 10 used to address memory and I/O registers

**#20: A11** - Address Bus line 11 used to address memory and I/O registers

**#21: VSS ✔** - System logic ground

**#22: A12** - Address Bus line 12 used to address memory and I/O registers

**#23: A13** - Address Bus line 13 used to address memory and I/O registers

**#24: A14** - Address Bus line 14 used to address memory and I/O registers

**#25: A15** - Address Bus line 15 used to address memory and I/O registers

**#26: D7** - Data Bus line 7 used for data exchange with memory and I/O registers

**#27: D6** - Data Bus line 6 used for data exchange with memory and I/O registers

**#28: D5** - Data Bus line 5 used for data exchange with memory and I/O registers

**#29: D4** - Data Bus line 4 used for data exchange with memory and I/O registers

**#30: D3** - Data Bus line 3 used for data exchange with memory and I/O registers

**#31: D2** - Data Bus line 2 used for data exchange with memory and I/O registers

**#32: D1** - Data Bus line 1 used for data exchange with memory and I/O registers

**#33: D0** - Data Bus line 0 used for data exchange with memory and I/O registers

**#34: RWB** - Read/Write output signal controls data transfer direction (high for read, low for write)

**#35: NC** - No Connect pins not connected internally and should not be connected externally

**#36: BE ✔** - Bus Enable input signal provides external control of the Address, Data, and RWB buffers

**#37: PHI2 ✔** - Phase 2 In is the system clock input to the microprocessor internal clock

**#38: SOB ✔** - Set Overflow input sets the overflow bit in the status code register on a negative transition

**#39: PHI2O** - Phase 2 Out signal generated from PHI2

**#40: RESB ✔** - Reset input used to initialize the microprocessor and start program execution


<div><br></br></div>
  

### Testing and Troubleshooting
After assembling each section, it’s essential to test and troubleshoot:
1. Power on the circuit and check the voltages.
2. Use the multimeter and oscilloscope to verify signals.
3. Troubleshoot any issues by checking connections and components.

## Conclusion
Congratulations on building your own 6502 computer! For more information, tutorials, and community support, visit Ben Eater’s website and forums.

## References
- [Ben Eater’s YouTube Channel](https://www.youtube.com/BenEater)
- [Ben Eater’s Website](https://eater.net)
- [6502 Microprocessor Datasheet](https://eater.net/datasheets/w65c02s.pdf)

