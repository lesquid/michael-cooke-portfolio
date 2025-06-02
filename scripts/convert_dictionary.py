import re

input_path = "michael-cooke-portfolio/resources/dictionary.html"
output_path = "../resources/dictionary_cleaned.html"

# Regex to match <div class="word-list-entry"><strong>WORD</strong> MEANING</div>
entry_re = re.compile(
    r'<div class="word-list-entry">\s*<strong>([^<]+)</strong>\s*([^<]*)</div>',
    re.IGNORECASE
)

def convert_entry(match):
    word = match.group(1).strip()
    meaning = match.group(2).strip()
    return (
        '<div class="word-list-item">\n'
        f'  <strong class="ngaanyatjarra-word">{word}</strong> '
        f'<span class="english-meaning">{meaning}</span>\n'
        '</div>'
    )

with open(input_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace all word-list-entry blocks
html = entry_re.sub(convert_entry, html)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Conversion complete. Output written to {output_path}")