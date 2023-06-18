from flask import Flask, render_template, request
import convert_pdf_to_string as cpts
import function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    pdf_file = request.files['pdf_file']
    pdf_path = "path_to_save_uploaded_pdf.pdf"  # Provide a path to save the uploaded PDF file
    pdf_file.save(pdf_path)  # Save the uploaded file to the specified path
    pdf_text = cpts.extract_text(pdf_path)
    print(pdf_text)
    question = request.form['question']  # Get the value from the question input
    answer = function.compare(pdf_text, question)
    # Use the pdf_text for further processing or display it in the web app
    return render_template('result.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)