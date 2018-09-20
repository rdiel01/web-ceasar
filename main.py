from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config["DEBUG"] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form{{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea{{
                margin: 10ps 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="post">
            Rotate by: <input type="text" name="rot" value="0"><br>
            <textarea placeholder="Enter your text here..." rows="15" cols="30" name="text">{0}</textarea>
            <input type="submit" value="Submit">
        </form>
    </body>
"""

@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=["post"])
def encrypt():
    user_rotation = int(request.form.get("rot"))
    user_text = request.form.get("text")

    encrypt_text = rotate_string(user_text,user_rotation)
    return form.format(encrypt_text)

app.run()