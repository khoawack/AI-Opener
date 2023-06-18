# import io 
# from pdfminer.converter import TextConverter 
# from pdfminer.pdfinterp import PDFPageInterpreter 
# from pdfminer.pdfinterp import PDFResourceManager 
# from pdfminer.pdfpage import PDFPage 

# def extract_text_by_page(pdf_path):
#     text = ""  # Create an empty string to store the concatenated text
    
#     with open(pdf_path, 'rb') as fh:
#         resource_manager = PDFResourceManager()
        
#         for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
#             fake_file_handle = io.StringIO()
#             converter = TextConverter(resource_manager, fake_file_handle)
#             page_interpreter = PDFPageInterpreter(resource_manager, converter)
            
#             page_interpreter.process_page(page)
#             page_text = fake_file_handle.getvalue()
            
#             text += page_text  # Concatenate the text from each page
            
#             # Close open handles
#             converter.close()
#             fake_file_handle.close()
    
#     return text  # Return the concatenated text as a single string

# def extract_text(pdf_path):
#     text = extract_text_by_page(pdf_path)
#     return text

import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


def extract_text_by_page(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as fh:
        resource_manager = PDFResourceManager()
        
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            
            page_interpreter.process_page(page)
            page_text = fake_file_handle.getvalue()
            
            text += page_text  # Concatenate the text from each page
            
            # Close open handles
            converter.close()
            fake_file_handle.close()
    
    return text  # Return the concatenated text as a single string


def extract_text(pdf_path, chunk_size=4096):
    text = ""
    with open(pdf_path, 'rb') as fh:
        resource_manager = PDFResourceManager()
        fake_file_handle = io.StringIO()
        converter = TextConverter(resource_manager, fake_file_handle)
        page_interpreter = PDFPageInterpreter(resource_manager, converter)
        
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            page_interpreter.process_page(page)
            page_text = fake_file_handle.getvalue()
            
            if len(text) + len(page_text) <= chunk_size:
                text += page_text
            else:
                break
        
        converter.close()
        fake_file_handle.close()
    
    return text


# # Usage example
# pdf_file_path = 'path_to_your_large_pdf.pdf'
# pdf_text = extract_text(pdf_file_path)
# print(pdf_text)

