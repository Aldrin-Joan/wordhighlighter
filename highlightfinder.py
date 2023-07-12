from docx import Document
def extract_keywords_to_file(docx_file):
    doc = Document(docx_file)
    highlighted_text = []

    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if run.font.highlight_color is not None:
                highlighted_text.append(run.text)

    output_file = docx_file.replace(".docx", ".txt")

    with open(output_file, "w", encoding="utf-8") as file:
        for line in highlighted_text:
            file.write(line + "\n")

    print(f"Highlighted text extracted and saved to {output_file} successfully.")
docx_file = input(r"Enter the file location: ")
extract_keywords_to_file(docx_file)
