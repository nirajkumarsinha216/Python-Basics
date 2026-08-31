from docx import Document

def convert_docx_to_text(docx_path):
    """
    Convert a .docx file to plain text.

    Args:
        docx_path (str): The path to the .docx file.

    Returns:
        str: The extracted text from the .docx file.
    """
    try:
        doc = Document(docx_path)
        output_path = "/Users/niraj/Documents On Mac/Projects/Python Basics/llm/company_document.txt"
        full_text = ""
        with open(output_path,'w', encoding='utf-8') as f:
            for para in doc.paragraphs:
                f.write(para.text + '\n')
                #full_text += para.text + '\n'
            #return full_text
        print(f"Text extracted and saved to {output_path}")
    except Exception as e:
        print(f"Error occurred while converting .docx to text: {e}")
        return ""