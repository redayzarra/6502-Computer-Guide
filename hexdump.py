import sys

# ANSI escape codes for colors
CYAN = "\033[96m"
RESET = "\033[0m"

def format_binary_file(file):
    # Check if 'file' is a string (file path) or a file-like object
    if isinstance(file, str):
        with open(file, 'rb') as f:
            data = f.read()
    else:
        # Assume it's a file-like object
        data = file.read()

    output = []
    last_line_content = None
    repeat_count = 0

    for i in range(0, len(data), 16):
        chunk = data[i:i+16]
        hex_values = ' '.join([f'{b:02x}' for b in chunk[:8]]) + '   ' + ' '.join([f'{b:02x}' for b in chunk[8:]])
        ascii_repr = ''.join([chr(b) if 32 <= b < 127 else '.' for b in chunk])
        
        line_content = f"{hex_values:<51}  |{ascii_repr}|"
        line = f'{i:08x}  {line_content}'
        
        if line_content == last_line_content:
            repeat_count += 1
        else:
            if repeat_count > 0:
                output.append(f'{CYAN}* lines repeated {repeat_count} times{RESET}')
                repeat_count = 0
            output.append(line)
            last_line_content = line_content

    if repeat_count > 0:
        output.append(f'{CYAN}* lines repeated {repeat_count} times {RESET}')

    output.append(f'{len(data):08x}')

    return '\n'.join(output)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        formatted_output = format_binary_file(file_path)
        print(formatted_output)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
