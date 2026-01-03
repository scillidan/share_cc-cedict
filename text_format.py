# Usage: python file.py <input_file> <output_file>

import sys
import re
from html import unescape

def match_add(text):
    # Add <br> between </div> and <ul>
    text = re.sub(r'</div>\s*<div>\s*<ul>', '</div><br><ul>', text)
    # Add space between </font> and <font ...>
    text = re.sub(r'</font>\s*<font([^>]*)>', r'</font> <font\1>', text)
    return text

def match_replace(text):
    # Replace all variations of <br> tags with <br>
    text = re.sub(r'<br\s*/?>', '<br>', text)
    # Replace with space
    text = text.replace('\xa0', ' ').replace('&nbsp;', ' ')
    return text

def match_convert(text):
    # Convert "<ul><li>item1</li><li>item2</li></ul>" to "- item1<br>- item2"
    def repl(match):
        ul_content = match.group(1)
        items = re.findall(r'<li>(.*?)</li>', ul_content, re.DOTALL)
        cleaned_items = ['- ' + re.sub(r'\s+', ' ', unescape(item.strip())) for item in items]
        return '<br><br>' + '<br>'.join(cleaned_items)
    text = re.sub(r'<ul>(.*?)</ul>', repl, text, flags=re.DOTALL)
    return text

def match_remove(text):
    # Remove <font></font>
    text = re.sub(r'<font[^>]*>', '', text)
    text = re.sub(r'</font>', '', text)
    # Remove <div style:"border...></div>
    pattern = re.compile(r'<div style="border: 1px solid; padding: 5px">(.*)</div>', re.DOTALL)
    match = pattern.search(text)
    if match:
        return match.group(1).strip()
    return text

def match_remove_except_br(text):
    # Remove all other tags (e.g. div, big, span etc) except <br>
    placeholder = "___BR_TAG___"
    text = text.replace('<br>', placeholder)
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace(placeholder, '<br>')
    return text

def match_other(text):
    # Replace repeated <br> with <br>
    text = re.sub(r'(<br>\s*)+', '<br>', text)
    # Replace / with ", "
    text = re.sub(r'\s*/\s*', ', ', text)
    return text

def format_line(line):
    if '\t' not in line:
        return line.strip()
    parts = line.split('\t', 1)
    word_part = parts[0]
    meaning_part = parts[1].strip()

    meaning_part = match_add(meaning_part)
    meaning_part = match_replace(meaning_part)
    meaning_part = match_convert(meaning_part)
    meaning_part = match_remove(meaning_part)
    meaning_part = match_remove_except_br(meaning_part)
    meaning_part = match_other(meaning_part)
    meaning_part = unescape(meaning_part)
    meaning_part = meaning_part.strip()

    formatted_line = f"{word_part}\t{meaning_part}"
    return formatted_line

def main():
    if len(sys.argv) != 3:
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    formatted_lines = []
    for line in lines:
        line = line.rstrip('\n\r')
        if line.strip() == '':
            continue
        formatted_line = format_line(line)
        if formatted_line.strip() != '':
            formatted_lines.append(formatted_line)

    with open(output_file, 'w', encoding='utf-8') as file_out:
        file_out.write('\n'.join(formatted_lines))

    print(f"Processed {len(formatted_lines)} lines")

if __name__ == '__main__':
    main()