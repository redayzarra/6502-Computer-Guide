def create_eeprom(size=32768, fill_value=0xEA, filename="rom.bin"):
    """
    Create an EEPROM binary file filled with a specific value.
    
    :param size: Size of the EEPROM in bytes (default: 32768)
    :param fill_value: Value to fill the EEPROM with (default: 0xEA)
    :param filename: Name of the output file (default: "rom.bin")
    """
    # Fill up the rom with EA bytes
    rom = bytearray([fill_value] * size)
    
    # Overwrite `7ffc` to "0" and `7ffd` to "80"
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