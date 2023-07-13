from docx import Document #importing the necessary libraries: The docx library is imported to work with Word documents
def extract_keywords_to_file(docx_file): #function to extract highlighted text 
    doc = Document(docx_file)
    highlighted_text = [] #empty list to store highlighted text 

    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if run.font.highlight_color is not None:
                highlighted_text.append(run.text)

    output_file = docx_file.replace(".docx", ".txt") #generating output file by replacing docx extension

    with open(output_file, "w", encoding="utf-8") as file:
        for line in highlighted_text:
            file.write(line + "\n") #writing the highlighted text to a txt file 

    print(f"Highlighted text extracted and saved to {output_file} successfully.") #success message 
docx_file = input(r"Enter the file location: ")
extract_keywords_to_file(docx_file) #calling the function extract_keywords_to_file(docx_file)
