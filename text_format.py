# Usage: python file.py <input_file> <output_file>

import sys
import re
from html import unescape

def add_br(text):
    # Add <br /> between </div> and <ul>
    text = re.sub(r'</div>\s*<div>\s*<ul>', '</div><br /><ul>', text)
    return text

def remove_div_border(text):
    # Remove <div style:"border...></div>
    pattern = re.compile(r'<div style="border: 1px solid; padding: 5px">(.*?)</div>', re.DOTALL)
    match = pattern.search(text)
    if match:
        return match.group(1).strip()
    return text

def remove_font_tags(text):
    # Remove <font></font>
    text = re.sub(r'<font[^>]*>', '', text)
    text = re.sub(r'</font>', '', text)
    return text

def replace_to_space(text):
    # Replace with space
    return text.replace('\xa0', ' ').replace('&nbsp;', ' ')
    return text

def convert_html_list(text):
    # Convert "<ul><li>item1</li><li>item2</li></ul>" to "- item1<br />- item2"
    def repl(match):
        ul_content = match.group(1)
        items = re.findall(r'<li>(.*?)</li>', ul_content, re.DOTALL)
        cleaned_items = ['- ' + re.sub(r'\s+', ' ', unescape(item.strip())) for item in items]
        return '<br />' + '<br />'.join(cleaned_items)
    text = re.sub(r'<ul>(.*?)</ul>', repl, text, flags=re.DOTALL)
    return text

def replace_br_tags(text):
    # Convert all variations of <br> tags to <br />
    text = re.sub(r'<br\s*/?>', '<br />', text)
    return text

def remove_all_other_tags_except_br(text):
    # Remove all other tags (e.g. div, big, span etc) except <br>
    placeholder = "___BR_TAG___"
    text = text.replace('<br />', placeholder)
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace(placeholder, '<br />')
    return text

def format_line(line):
    if '\t' not in line:
        return line.strip()
    parts = line.split('\t', 1)
    dict_part = parts[0]
    html_part = parts[1].strip()

    html_part = add_br(html_part)
    html_part = remove_div_border(html_part)
    html_part = remove_font_tags(html_part)
    html_part = replace_to_space(html_part)
    html_part = convert_html_list(html_part)
    html_part = replace_br_tags(html_part)
    html_part = remove_all_other_tags_except_br(html_part)
    html_part = unescape(html_part)
    html_part = html_part.strip()

    formatted_line = f"{dict_part}\t{html_part}"
    return formatted_line

def main():
    if len(sys.argv) == 3:
        input_path, output_path = sys.argv[1], sys.argv[2]

    with open(input_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    formatted_lines = []
    for line in lines:
        line = line.rstrip('\n\r')
        if line.strip() == '':
            continue
        formatted_line = format_line(line)
        if formatted_line.strip() != '':
            formatted_lines.append(formatted_line)

    with open(output_path, 'w', encoding='utf-8') as file_out:
        file_out.write('\n'.join(formatted_lines))

    print(f"Processed {len(formatted_lines)} lines")

if __name__ == '__main__':
    main()