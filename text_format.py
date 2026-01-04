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
    # Replace repeated ' ' with ' '
    text = re.sub(r'\s+', ' ', text)
    # Replace / with ", "
    text = re.sub(r'\s*/\s*', ', ', text)
    return text

def format(line):
    if '\t' not in line:
        return line.strip()
    parts = line.split('\t', 1)
    word = parts[0]
    meaning = parts[1].strip()

    meaning = match_add(meaning)
    meaning = match_replace(meaning)
    meaning = match_convert(meaning)
    meaning = match_remove(meaning)
    meaning = match_remove_except_br(meaning)
    meaning = match_other(meaning)
    meaning = unescape(meaning)
    meaning = meaning.strip()

    result = f"{word}\t{meaning}"
    return result

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <input_file> <output_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(results))

    print(f"Processed {len(results)} lines")

if __name__ == '__main__':
    main()