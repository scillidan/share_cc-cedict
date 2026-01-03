# Usage: python file.py <input_file> <output_file>

import sys

def html_to_ansi(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                # Replace <br>  with the string \n
                modified_line = line.replace('<br>', r'\n')
                outfile.write(modified_line)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    sys.exit(0)

def main():
    if len(sys.argv) == 3:
        input_file, output_file  = sys.argv[1], sys.argv[2]
        html_to_ansi(input_file, output_file)
        print(f"Conversion completed: {input_file} to {output_file}")

if __name__ == '__main__':
    main()