from flask import *  
import PyPDF2
from gtts import gTTS
app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("index.html")  
 
language = 'en-us'

@app.route('/', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        pdf_file = open(f.filename,'rb')
        print(f.filename)
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        print(number_of_pages)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        myobj = gTTS(text=page_content, lang=language, slow=False)
        myobj.save("welcome.wav")

        return render_template("index.html", name = page_content)
          

if __name__ == '__main__':  
    app.run(debug=True)  
