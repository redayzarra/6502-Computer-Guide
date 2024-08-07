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

<div align="center">
<img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/7a01b0e3-954c-416e-8790-4596a82aa116" alt="Datasheet diagram of 6502 Microprocessor" height="350"><br>
<details>
<summary>

#### Pin Connections
</summary>

| Pin | Name | Description |
|-----|------|-------------|
| **#1** | **VPB** | Vector Pull output indicates when interrupt vectors are being addressed |
| **#2** | **RDY** | Ready (low input logic) will halt the microprocessor in its current state |
| **#3** | **PHI1O** | Phase 1 Out is the inverted PHI2 signal |
| **#4** | **IRQB** | Interrupt Request input signal to initiate an interrupt sequence |
| **#5** | **MLB** | Memory Lock output to ensure the integrity of Read-Modify-Write instructions in multiprocessor systems |
| **#6** | **NMIB** | Non-Maskable Interrupt input initiates an interrupt sequence on a negative transition |
| **#7** | **SYNC** | Synchronize output indicates OpCode fetch cycle |
| **#8** | **VDD** | Positive power supply voltage |
| **#9-20** | **A0-A11** | Address Bus lines 0 to 11 used to address memory and I/O registers |
| **#21** | **VSS** | System logic ground |
| **#22-25** | **A12-A15** | Address Bus lines 12 to 15 used to address memory and I/O registers |
| **#26-33** | **D7-D0** | Data Bus lines 0 to 7 used for data exchange with memory and I/O registers |
| **#34** | **RWB** | Read/Write output signal controls data transfer direction (high for read, low for write) |
| **#35** | **NC** | No Connect pins not connected internally and should not be connected externally |
| **#36** | **BE** | Bus Enable input signal provides external control of the Address, Data, and RWB buffers |
| **#37** | **PHI2** | Phase 2 In is the system clock input to the microprocessor internal clock |
| **#38** | **SOB** | Set Overflow input sets the overflow bit in the status code register on a negative transition |
| **#39** | **PHI2O** | Phase 2 Out signal generated from PHI2 |
| **#40** | **RESB** | Reset input used to initialize the microprocessor and start program execution |
</details>
</div>

The 6502 microprocessor was a popular chip in the 1970s, used in many famous computers like the Apple I and Commodore 64. It features:
- 8-bit data bus
- 16-bit address bus
- Data sheet (30 pages)

### Key Features

- Address Bus (A0-A15): 16-bit address bus allowing access to 65,536 unique memory locations.
- Data Bus (D0-D7): 8-bit bidirectional data bus for reading from and writing to memory and I/O devices.
- Clock Inputs (PHI2): System clock input that controls the timing of the processor.
- Interrupt Handling (IRQB, NMIB): Support for maskable and non-maskable interrupts.
- Read/Write Control (RWB): Indicates whether the current operation is a read or write.
- Power Management (RDY): Ability to halt the processor to save power or synchronize with slow memory/peripherals.
- Reset (RESB): Input to initialize the processor and start program execution.

### Connecting 6502 to Memory and I/O

1. Address lines (A0-A15) connect to memory devices (like ROM and RAM) and I/O peripherals.
2. Data lines (D0-D7) connect bidirectionally to memory and I/O devices.
3. RWB signal connects to memory and I/O devices to indicate read or write operations.
4. Clock signal (PHI2) is provided externally to drive the processor's timing.

### Considerations

- The 6502 reads from addresses FFFC and FFFD on startup to determine the program start address (reset vector).
- Proper setup of interrupt vectors is crucial for handling IRQ and NMI.
- The RDY pin can be used to introduce wait states for slow memory or I/O devices.
- The BE (Bus Enable) pin allows external control of the processor's buses, useful in multi-processor systems.
- Careful timing considerations are needed, especially when interfacing with memory and I/O devices of varying speeds.


## Understanding the AT28C256 EEPROM
<div align="center">
 <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/ef555cfb-39d4-4f68-9f09-73f2b6c7d4ec" alt="Datasheet diagram of 28C256 EEPROM" height="350"><br>
 <details>
 <summary>

#### Pin Connections
</summary>

| Pin | Name | Description |
|-----|------|-------------|
| **#1** | **A14** | Address line 14 (Most Significant Bit) |
| **#2** | **A12** | Address line 12 |
| **#3** | **A7** | Address line 7 |
| **#4** | **A6** | Address line 6 |
| **#5** | **A5** | Address line 5 |
| **#6** | **A4** | Address line 4 |
| **#7** | **A3** | Address line 3 |
| **#8** | **A2** | Address line 2 |
| **#9** | **A1** | Address line 1 |
| **#10** | **A0** | Address line 0 (Least Significant Bit) |
| **#11** | **I/O0** | Data Input/Output 0 |
| **#12** | **I/O1** | Data Input/Output 1 |
| **#13** | **I/O2** | Data Input/Output 2 |
| **#14** | **GND** | Ground |
| **#15** | **I/O3** | Data Input/Output 3 |
| **#16** | **I/O4** | Data Input/Output 4 |
| **#17** | **I/O5** | Data Input/Output 5 |
| **#18** | **I/O6** | Data Input/Output 6 |
| **#19** | **I/O7** | Data Input/Output 7 |
| **#20** | **CE** | Chip Enable (active low) |
| **#21** | **A10** | Address line 10 |
| **#22** | **OE** | Output Enable (active low) |
| **#23** | **A11** | Address line 11 |
| **#24** | **A9** | Address line 9 |
| **#25** | **A8** | Address line 8 |
| **#26** | **A13** | Address line 13 |
| **#27** | **WE** | Write Enable (active low) |
| **#28** | **VCC** | Power supply voltage |
</details>
</div>
The AT28C256 is a 32K x 8 Electrically Erasable Programmable Read-Only Memory (EEPROM) used to store our program. It features:

- Storage capacity: 256K bits (32 kilobytes)
- Organization: 32,768 words x 8 bits
- 15 address lines (A0-A14) for accessing 32,768 unique locations
- 8 data lines (I/O0-I/O7) for input/output


### Key Features

- Address Lines (A0-A14): Used to specify the memory location for read or write operations.
- Data Lines (I/O0-I/O7): Bidirectional pins for data input during write operations and data output during read operations.
- CE (Chip Enable): When low, it enables the chip. When high, it puts the device in low-power standby mode.
- OE (Output Enable): Controls the output buffers. When low, it enables data output during read operations.
- WE (Write Enable): Controls write operations. A low-to-high transition initiates a write cycle.
- VCC and GND: Power supply connections.

### Connecting EEPROM to 6502

1. The 6502 has 16 address lines (A0-A15), allowing access to 65,536 unique addresses.
2. Two options for connecting:
   - Connect A0-A14 directly, repeating ROM contents twice in address space.
   - Use A15 to control EEPROM's chip enable (CE), allowing the upper half of address space for other uses (RAM, I/O).

### Considerations

- The 6502 reads from addresses FFFC and FFFD on startup to determine where to begin fetching instructions.
- These addresses should be accessible in the ROM for proper initialization.
- Proper connection of CE, OE, and WE pins is crucial for correct operation and power management.


## Understanding the NAND Gate
<div align="center">
 <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/68c86327-ae5b-4067-a8dd-a9766b4d31a7" alt="Datasheet diagram of SN74LS00N Nand Gates chip" height="350"><br>
 <details>
<summary>

#### Pin Connections
</summary>

| Pin | Name | Description |
|-----|------|-------------|
| **#1, #4, #9, #12** | **Input A** | Input A for each of the four NAND gates |
| **#2, #5, #10, #13** | **Input B** | Input B for each of the four NAND gates |
| **#3, #6, #8, #11** | **Output** | Output for each of the four NAND gates |
| **#7** | **GND** | Ground |
| **#14** | **VCC** | Positive supply voltage |

</details>
</div>
The SN74LS00N is a quadruple 2-input positive-NAND gates chip used as an inverter in our 6502 computer project. It features:
- Four independent 2-input NAND gates
- Low power Schottky TTL logic
- Operation from a single 5V supply

### Key Features

- Clock Signal Inversion: Shapes the clock signal to meet 6502 requirements.
- Address Decoding: Inverts the A15 signal to select between ROM and RAM or I/O devices.
- Logic Level Conversion: Adapts signals between different logic families.
- Signal Buffering: Maintains signal integrity.
- Noise Reduction: Reduces clock signal noise when used as an inverter.

### Using NAND as an Inverter

To convert a NAND gate to an inverter:
1. Connect both inputs of the NAND gate together.
2. Use this connected pair as the single input.
3. The output will be the inverted signal of the input.

This configuration uses the NAND gate's truth table:
- When both inputs are high (1), the output is low (0)
- For all other input combinations, the output is high (1)

### Considerations

- Ensure proper 5V power supply and grounding.
- Account for propagation delays in time-sensitive operations.
- Use decoupling capacitors near the VCC pin.
- Tie unused inputs to a defined logic level to prevent floating inputs.


## Understanding the W65C22 Versatile Interface Adapter (VIA)
<div align="center">
 <img src="https://github.com/user-attachments/assets/af94dcd0-7da2-44ea-94ec-d5b9e341c618" alt="Datasheet diagram of W65C22 Versatile Interface Adapter" height="350"><br>
 <details>

<summary>
 
#### Pin Connections
</summary>
 
| Pin | Name | Description |
|-----|------|-------------|
| **CA1, CA2** | **Peripheral A Control Lines** | Interrupt inputs or handshake outputs for PA. CA1 also controls input data latching on PA. |
| **CB1, CB2** | **Peripheral B Control Lines** | Interrupt inputs or handshake outputs for PB. Also serve as serial data port for Shift Register. |
| **CS1, CS2B** | **Chip Select** | Enable chip when CS1 is logic 1 and CS2B is logic 0. |
| **D0-D7** | **Data Bus** | Bidirectional lines for data transfer with the microprocessor. |
| **IRQB** | **Interrupt Request** | Outputs logic 0 when interrupt conditions are met. |
| **PA0-PA7** | **Peripheral I/O Port A** | 8-line bidirectional bus for data, control, and status transfer. |
| **PB0-PB7** | **Peripheral I/O Port B** | 8-line bidirectional bus with additional timer control for PB6 and PB7. |
| **PHI2** | **Phase 2 Internal Clock** | Controls data transfers between VIA and microprocessor. |
| **RESB** | **Reset** | Clears internal registers (except T1, T2 counters/latches, and SR). |
| **RS0-RS3** | **Register Select** | Selects one of 16 internal registers. |
| **R/WB** | **Read/Write** | Controls data transfer direction. |
| **VDD** | **Positive Power Supply** | Positive supply voltage. |
| **VSS** | **Internal Logic Ground** | System logic ground. |
</details>
</div>

The W65C22 is a flexible I/O device designed for use with the 65xx series microprocessor family. It features:
- Two 8-bit bidirectional I/O ports
- Two 16-bit programmable timer/counters
- 8-bit shift register for serial communications
- Data sheet (52 pages)

### Key Features
- Peripheral Ports (PA0-PA7, PB0-PB7): Two 8-bit bidirectional I/O ports for interfacing with peripheral devices.
- Timer/Counters: Two 16-bit programmable interval timers/event counters.
- Shift Register: 8-bit shift register for serial-to-parallel and parallel-to-serial conversion.
- Interrupt Handling: Supports multiple interrupt sources with individual enable/disable control.
- Handshake Control: Programmable handshake modes for data transfer synchronization.
- Programmable I/O: Each pin can be individually programmed as input or output.

### Connecting W65C22 to Microprocessor and Peripherals
1. Data lines (D0-D7) connect bidirectionally to the microprocessor's data bus.
2. Register Select lines (RS0-RS3) connect to the microprocessor's address lines.
3. Chip Select lines (CS1, CS2B) connect to address decoding logic.
4. Peripheral ports (PA0-PA7, PB0-PB7) connect to various I/O devices.
5. Control lines (CA1, CA2, CB1, CB2) connect to peripheral handshake or interrupt signals.

### Considerations
- The W65C22 has 16 internal registers, accessible via the RS0-RS3 lines.
- Proper configuration of Data Direction Registers is crucial for correct I/O operation.
- Timer interrupts can be used for generating precise timing intervals or counting external events.
- The Shift Register can be used for serial communication protocols.
- Interrupt flags and enables must be properly managed for efficient interrupt-driven operations.
- The device is versatile but requires careful programming to fully utilize its features.


## Step-by-Step Assembly Instructions

This section meticulously breaks down each phase of the assembly process into clear, manageable steps. Starting with organizing your components, you'll move on to setting up your breadboards, wiring the CPU and support chips, and then proceed to connecting memory and I/O devices.

### 1. Connect the 6502 Microprocessor to Power

<div align="center">
<table>
  <tr>
    <td align="center" width="300">
      <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/7a01b0e3-954c-416e-8790-4596a82aa116" alt="Datasheet diagram of 6502 Microprocessor" height="350"><br>
      <p>Figure 1: W65C02S 40 Pinout</p>
    </td>
    <td align="center" width="450">
      <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/614dc660-b828-47a7-9604-6b40eb56a532" alt="6502 Microprocessor on breadboard" height="350"><br>
      <p>Connect VDD to positive power, and VSS to ground</p>
    </td>
  </tr>
</table>
<details>
<summary>
 
#### Pin Connections

</summary>

| Pin | Name | Description | Connect |
|-----|------|-------------|---------|
| **#8** | **VDD** | Positive power supply voltage | ✔ |
| **#21** | **VSS** | System logic ground | ✔ |
</details>
</div>


### 2. Connecting Input Pins

<div align="center">
<table>
  <tr>
    <td align="center" width="300">
      <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/7a01b0e3-954c-416e-8790-4596a82aa116" alt="Datasheet diagram of 6502 Microprocessor" height="350"><br>
      <p>Figure 1: W65C02S 40 Pinout</p>
    </td>
    <td align="center" width="450">
      <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/e5007ef8-211d-4549-bb34-91eba05b8ea5" alt="6502 Microprocessor connected to input pins" height="350"><br>
      <p>Connecting input pins, see below</p>
    </td>
  </tr>
</table>
<details>
<summary>

#### Pin Connections
</summary>

| Pin | Name | Description | Connect |
|-----|------|-------------|---------|
| **#2** | **RDY** | Ready (low input logic) will halt the microprocessor in its current state | ✔ |
| **#4** | **IRQB** | Interrupt Request input signal to initiate an interrupt sequence | ✔ |
| **#6** | **NMIB** | Non-Maskable Interrupt input initiates an interrupt sequence on a negative transition | ✔ |
| **#36** | **BE** | Bus Enable input signal provides external control of the Address, Data, and RWB buffers | ✔ |
| **#37** | **PHI2** | Phase 2 In is the system clock input to the microprocessor internal clock | ✔ |
| **#38** | **SOB** | Set Overflow input sets the overflow bit in the status code register on a negative transition | ✔ |
| **#40** | **RESB** | Reset input used to initialize the microprocessor and start program execution | ✔ |
</details>
</div>

### 3. ROM Integration

<div align="center">
<table>
  <tr>
    <td align="center" width="300">
      <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/ef555cfb-39d4-4f68-9f09-73f2b6c7d4ec" alt="Datasheet diagram of 28C256 EEPROM" height="350"><br>
      <p>Figure 2: 28C256 EEPROM Pinout</p>
    </td>
    <td align="center" width="450">
      <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/5ec7bc17-05db-463e-a864-282cfb75943c" alt="28C256 EEPROM on breadboard" height="350"><br>
      <p>Connect VDD to positive power, and VSS to ground</p>
    </td>
  </tr>
</table>
 
<details>
<summary>

#### Pin Connections
</summary>

| Pin | Name | Description | Connect |
|-----|------|-------------|---------|
| **#14** | **GND** | System logic ground | ✔ |
| **#28** | **VCC** | Positive power supply voltage | ✔ |
</details>
</div>

### 4. ROM Control Signals

<div align="center">
<table>
  <tr>
    <td align="center" width="300">
      <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/ef555cfb-39d4-4f68-9f09-73f2b6c7d4ec" alt="Datasheet diagram of 28C256 EEPROM" height="350"><br>
      <p>Figure 2: 28C256 EEPROM Pinout</p>
    </td>
    <td align="center" width="450">
      <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/e303de2c-8efe-4379-bc5b-b9485eaacf0d" alt="28C256 EEPROM on breadboard" height="350"><br>
      <p>Connecting control signal pins, see below</p>
    </td>
  </tr>
</table>
 
<details>
<summary>

#### Pin Connections
</summary>

| Pin | Name | Description | Connect |
|-----|------|-------------|---------|
| **#27** | **WE** | Write Enable. Controls write operations. A low-to-high transition initiates a write cycle. | ✔ |
| **#22** | **OE** | Output Enable (active low) | ✔ |
</details>
</div>


### 5. Adding the NAND Gate

<div align="center">
<table>
  <tr>
    <td align="center" width="300">
      <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/68c86327-ae5b-4067-a8dd-a9766b4d31a7" alt="Datasheet diagram of SN74LS00N Nand Gates chip" height="350"><br>
      <p>Figure 3: SN74LS00N Nand Gates Pinout</p>
    </td>
    <td align="center" width="450">
      <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/6fd2091d-d366-4422-99df-44678278babd" alt="SN74LS00N Nand Gates chip on breadboard" height="350"><br>
      <p>Connecting the NAND gate to power</p>
    </td>
  </tr>
</table>
 
<details>
<summary>


#### Pin Connections
</summary>

| Pin | Name | Description | Connect |
|-----|------|-------------|---------|
| **#7** | **GND** | System logic ground | ✔ |
| **#14** | **VCC** | Positive power supply voltage | ✔ |
</details>
</div>


### 6. Converting NAND Gate to Inverter

<div align="center">
<table>
  <tr>
    <td align="center" width="300">
      <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/68c86327-ae5b-4067-a8dd-a9766b4d31a7" alt="Datasheet diagram of SN74LS00N Nand Gates chip" height="350"><br>
      <p>Figure 3: SN74LS00N Nand Gates Pinout</p>
    </td>
    <td align="center" width="450">
      <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/feb1af65-d02c-4285-ac35-d16baa2d82a1" alt="SN74LS00N Nand Gates chip converted to inverter" height="350"><br>
      <p>Converting the NAND gate into inverter for EEPROM</p>
    </td>

  </tr>
</table>
 
<details>
<summary>Pin Connections</summary>

| Pin | Name | Description | Connect |
|-----|------|-------------|---------|
| **#7** | **GND** | System logic ground | ✔ |
| **#14** | **VCC** | Positive power supply voltage | ✔ |
| **#12** | **Input A** | NAND gate input | Connect to #13 and A15 |
| **#13** | **Input B** | NAND gate input | Connect to #12 and A15 |
| **#11** | **Output Y** | NAND gate output | Connect to EEPROM Chip Enable |

</details>
</div>



### 7. Connecting Address Lines to ROM

<div align="center">
<table>
  <tr>
    <td align="center" width="300">
      <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/7a01b0e3-954c-416e-8790-4596a82aa116" alt="Datasheet diagram of 6502 Microprocessor" height="350"><br>
      <p>Figure 1: W65C02S 40 Pinout</p>
    </td>
    <td align="center" width="450">
      <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/03d88ea0-3122-4a85-8af6-8df3f4082757" alt="6502 Microprocessor connected to EEPROM through address lines" height="350"><br>
      <p>Connecting address lines 0 to 14</p>
    </td>
  </tr>
</table>

<details>
<summary>Pin Connections</summary>

| Pin | Name | Description | Connect |
|-----|------|-------------|---------|
| **#2** | **RDY** | Ready (low input logic) will halt the microprocessor in its current state | ✔ |
| **#4** | **IRQB** | Interrupt Request input signal to initiate an interrupt sequence | ✔ |
| **#6** | **NMIB** | Non-Maskable Interrupt input initiates an interrupt sequence on a negative transition | ✔ |
| **#36** | **BE** | Bus Enable input signal provides external control of the Address, Data, and RWB buffers | ✔ |
| **#37** | **PHI2** | Phase 2 In is the system clock input to the microprocessor internal clock | ✔ |
| **#38** | **SOB** | Set Overflow input sets the overflow bit in the status code register on a negative transition | ✔ |
| **#40** | **RESB** | Reset input used to initialize the microprocessor and start program execution | ✔ |
| **#9-23** | **A0-A14** | Address lines 0 through 14 | Connect to corresponding A0-A14 on EEPROM |

</details>
</div>


### 8. Connecting Data Lines to ROM
<div align="center">
<table>
  <tr>
    <td align="center" width="300">
      <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/7a01b0e3-954c-416e-8790-4596a82aa116" alt="Datasheet diagram of 6502 Microprocessor" height="350"><br>
      <p>Figure 1: W65C02S 40 Pinout</p>
    </td>
    <td align="center" width="450">
      <img src="https://github.com/redayzarra/6502-Computer-Guide/assets/113388793/e0821144-ee7f-44cf-804c-2a53573aa1aa" alt="6502 Microprocessor connected to EEPROM through data lines" height="350"><br>
      <p>Connecting data lines 0 to 7</p>
    </td>
  </tr>
</table>
<details>
<summary>Pin Connections</summary>

| Pin | Name | Description | Connect |
|-----|------|-------------|---------|
| **#2** | **RDY** | Ready (low input logic) will halt the microprocessor in its current state | ✔ |
| **#4** | **IRQB** | Interrupt Request input signal to initiate an interrupt sequence | ✔ |
| **#6** | **NMIB** | Non-Maskable Interrupt input initiates an interrupt sequence on a negative transition | ✔ |
| **#36** | **BE** | Bus Enable input signal provides external control of the Address, Data, and RWB buffers | ✔ |
| **#37** | **PHI2** | Phase 2 In is the system clock input to the microprocessor internal clock | ✔ |
| **#38** | **SOB** | Set Overflow input sets the overflow bit in the status code register on a negative transition | ✔ |
| **#40** | **RESB** | Reset input used to initialize the microprocessor and start program execution | ✔ |
| **#9-23** | **A0-A14** | Address lines 0 through 14 | Connect to corresponding A0-A14 on EEPROM |
| **#25-32** | **D0-D7** | Data lines 0 through 7 | Connect to corresponding D0-D7 on EEPROM |

</details>
</div>

### 9. Adding the W65C22 VIA
<div align="center">
<table>
  <tr>
    <td align="center" width="300">
      <img src="https://github.com/user-attachments/assets/af94dcd0-7da2-44ea-94ec-d5b9e341c618" alt="Datasheet diagram of W65C22 VIA" height="350"><br>
      <p>Figure 4: W65C22 VIA Pinout</p>
    </td>
    <td align="center" width="450">
      <img src="https://github.com/user-attachments/assets/18674732-1000-4100-91b9-21a87327246d" alt="W65C22 VIA connected to 6502 Microprocessor" height="350"><br>
      <p>Connecting the W65C22 VIA to the 6502</p>
    </td>
  </tr>
</table>
<details>
<summary>Pin Connections</summary>

| Pin | Name | Description | Connect |
|-----|------|-------------|---------|
| **#20** | **VDD** | Positive power supply voltage | ✔ |
| **#1** | **VSS** | System logic ground | ✔ |

</details>
</div>

### 10. Address Decoding and Additional Connections for W65C22 VIA

<div align="center">
<table>
  <tr>
    <td align="center" width="300">
      <img src="https://github.com/user-attachments/assets/af94dcd0-7da2-44ea-94ec-d5b9e341c618" alt="Diagram of NAND gates for address decoding" height="350"><br>
      <p>Figure 5: NAND Gate Logic for Address Decoding</p>
    </td>
    <td align="center" width="450">
      <img src="https://github.com/user-attachments/assets/413e003c-0d11-4fa0-ab3c-114be5424084"" alt="W65C22 VIA connected with address decoding" height="350"><br>
      <p>Connecting address decoding logic to W65C22 VIA</p>
    </td>
  </tr>
</table>
<details>
<summary>Address Decoding Connections</summary>

| Connection | Description |
|------------|-------------|
| **NAND Gate 1** | Input: Inverted A15, A14. Output: To CS2B of W65C22 |
| **NAND Gate 2** | Input 1: Output from NAND Gate 1. Input 2: A14 |
| **A13** | Directly connected to CS1 of W65C22 |
| **A14** | Connected to one input of NAND Gate 2 |
| **A15** | Inverted and connected to one input of NAND Gate 1 |

</details>
</div>

<div><br></br></div>
  

## Testing and Troubleshooting
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

