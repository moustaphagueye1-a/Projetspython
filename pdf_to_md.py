import fitz

pdf_path = "catalogue.pdf"
md_path = "catalogue.md"

doc = fitz.open(pdf_path)

with open(md_path, "w", encoding="utf-8") as f:
    for i, page in enumerate(doc):
        text = page.get_text()

        f.write(f"\n# Page {i + 1}\n\n")
        f.write(text)
        f.write("\n\n---\n\n")

print(f"Conversion terminée : {md_path}")
