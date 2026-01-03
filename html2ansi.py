# Usage: python file.py <input> <output>

import sys

def convert(input, output):
    try:
        with open(input, 'r', encoding='utf-8') as infile, \
             open(output, 'w', encoding='utf-8') as outfile:
            for line in infile:
                # Replace <br>  with the string \n
                modified_line = line.replace('<br>', r'\n')
                outfile.write(modified_line)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    sys.exit(0)

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <input> <output>")
        sys.exit(1)

    input = sys.argv[1]
    output = sys.argv[2]

    convert(input, output)
    print(f"Conversion completed: {input} to {output}")

if __name__ == '__main__':
    main()