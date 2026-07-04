from pdf2docx import Converter

def pdf_to_word(input_path: str, output_path: str):
    cv = Converter(input_path)
    cv.convert(output_path)
    cv.close()
    return output_path