def create_eeprom(size=32768, fill_value=0xEA, filename="rom.bin"):
    """
    Note: The EEPROM takes 7 clock cycles to initialize, then it will read the
    reset vector (which will jump to "8000").
    
    Create an EEPROM binary file filled with a specific value.
    
    :param size: Size of the EEPROM in bytes (default: 32768)
    :param fill_value: Value to fill the EEPROM with (default: 0xEA)
    :param filename: Name of the output file (default: "rom.bin")
    """
    # Fill up the rom with EA bytes
    rom = bytearray([fill_value] * size)
    
    # First: Load the value 42 into the `A` register
    rom[0] = 0xa9
    rom[1] = 0x42
    
    # Second: Store the contents of the `A` register at address "6000"
    rom[2] = 0x8d 
    rom[3] = 0x00
    rom[4] = 0x60
    
    # Overwrite `7ffc` to "00" and `7ffd` to "80", reset vector is now at "8000"
    rom[0x7ffc] = 0x00
    rom[0x7ffd] = 0x80
    
    try:
        with open(filename, "wb") as out_file:
            out_file.write(rom)
        print(f"EEPROM file '{filename}' created successfully!")
        print(f"Size: {size} bytes")
        print(f"Fill value: 0x{fill_value:02X}")
    except IOError as e:
        print(f"Error writing to file: {e}\n\n")

if __name__ == "__main__":
    create_eeprom()