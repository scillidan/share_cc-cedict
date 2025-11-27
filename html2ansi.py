# Write by GPT-4o mini🧙‍♂️, scillidan🤡
# Usage: python html2ansi.py <input_file> <output_file>

import sys

def convert_br_to_string(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Replace <br /> with the literal string \n
            modified_line = line.replace('<br />', r'\n')
            # Write the modified line to the output file
            outfile.write(modified_line)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python html2ansi.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_br_to_string(input_file, output_file)
    print(f"Conversion completed: {input_file} to {output_file}")