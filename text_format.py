# Write by GPT-4o mini🧙‍♂️, scillidan🤡
# Usage: python text_format.py <input_file> <output_file>

import sys
import re
from html import unescape

def remove_border_div(text):
    # Remove border div wrapper, keep inner content
    pattern = re.compile(r'<div style="border: 1px solid; padding: 5px">(.*?)</div>\s*$', re.DOTALL)
    m = pattern.search(text)
    if m:
        return m.group(1)
    return text

def remove_font_tags(text):
    # Remove all <font> and closing </font>, keep text
    text = re.sub(r'<font[^>]*>', '', text)
    text = re.sub(r'</font>', '', text)
    return text

def convert_html_list(text):
    # <ul><li>item1</li><li>item2</li></ul> -> - item1<br />- item2
    def repl(match):
        ul_content = match.group(1)
        items = re.findall(r'<li>(.*?)</li>', ul_content, re.DOTALL)
        cleaned_items = ['- ' + re.sub(r'\s+', ' ', unescape(item.strip())) for item in items]
        # Add a <br /> before the list to separate it from previous text
        return '<br />' + '<br />'.join(cleaned_items)
    text = re.sub(r'<ul>(.*?)</ul>', repl, text, flags=re.DOTALL)
    return text

def fix_ansi_codes(text):
    # Replace non-breaking spaces by space
    text = text.replace('\xa0', ' ')
    text = text.replace('&nbsp;', ' ')
    return text

def convert_br_tags(text):
    # Convert <br>, <br/>, <br /> to the exact string "<br />"
    text = re.sub(r'<br\s*/?>', '<br />', text)
    return text

def remove_all_other_tags(text):
    # Remove all remaining html tags (e.g. div, big, span etc)
    text = re.sub(r'<[^>]+>', '', text)
    return text

def remove_blank_lines(text):
    lines = text.splitlines()
    filtered = [line for line in lines if line.strip() != '']
    return '\n'.join(filtered)

def remove_all_other_tags_except_br(text):
    placeholder = "___BR_TAG___"
    text = text.replace('<br />', placeholder)
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace(placeholder, '<br />')
    return text

def ensure_br_before_ul(text):
    # Fix missing <br /> between div and ul
    text = re.sub(r'</div>\s*<div>\s*<ul>', '</div><br /><ul>', text)
    return text

def process_line(line):
    if '\t' not in line:
        return line.strip()
    parts = line.split('\t', 1)
    dict_part = parts[0]
    html_part = parts[1].strip()

    html_part = remove_border_div(html_part)
    html_part = remove_font_tags(html_part)
    html_part = convert_html_list(html_part)
    html_part = ensure_br_before_ul(html_part)  # Fix line break before list
    html_part = fix_ansi_codes(html_part)
    html_part = convert_br_tags(html_part)
    html_part = remove_all_other_tags_except_br(html_part)
    html_part = unescape(html_part)
    html_part = html_part.strip()

    formatted_line = f"{dict_part}\t{html_part}"
    return formatted_line

def main():
    if len(sys.argv) != 3:
        print("Usage: python cli.py <input> <output>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    processed_lines = []
    for line in lines:
        line = line.rstrip('\n\r')
        if line.strip() == '':
            continue
        processed_line = process_line(line)
        if processed_line.strip() != '':
            processed_lines.append(processed_line)

    output_text = '\n'.join(processed_lines)

    with open(output_path, 'w', encoding='utf-8') as f_out:
        f_out.write(output_text)

if __name__ == '__main__':
    main()
