
from flask import Flask, render_template, url_for
from flask import request, redirect
import csv


app = Flask(__name__)
print(__name__)


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode = 'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')



def write_to_csv(data):
    with open('database.csv', newline='', mode = 'a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',' ,  quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])





@app.route('/sumbit_form', methods=['POST', 'GET'])
def sumbit_form():
    if request.method == 'POST' :
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'       
        

 