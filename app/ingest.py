import fitz
import re

def extract_sections(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""

    for page in doc:
        full_text += page.get_text()

    pattern = r"(Section\s+\d+\..*?)(?=Section\s+\d+\.|$)"
    matches = re.findall(pattern, full_text, re.S)

    sections = {}

    for i, section in enumerate(matches, 1):
        sections[i] = section.strip()

    return sections


if __name__ == "__main__":
    s = extract_sections("data/SLATEFALL_DOSSIER.pdf")
    print(f"Found {len(s)} sections")
    print(s[1][:500])