from flask import Flask, request, render_template
import pyqrcode
import png
import time
import os


app = Flask(__name__, static_folder='static')

def delete_qr_code():
    # Delete the PNG file if it exists
    if os.path.exists("static/UPIgen.png"):
        os.remove("static/UPIgen.png")
    return

@app.route('/', methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        if "rmv" in request.form:
            time.sleep(0.1)
            delete_qr_code()
        else:
            amt = str(request.form.get("amount"))
            myUPI = "9494887445@ibl"
            upi_link = f"upi://pay?pa={myUPI}&pn=Merchant_Name&mc=&tid=&tr=&tn=Payment_Request&am={amt}&cu=INR"
            QRcode = pyqrcode.create(upi_link)
            QRcode.png("static/UPIgen.png", scale=8)
            #TODO: Perform payment Logic here 
            time.sleep(0.1)

        return render_template("index.html")
    return render_template("index.html")

@app.route('/success')
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug = True)