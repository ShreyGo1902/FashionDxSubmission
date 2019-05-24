import os
from flask import Flask, render_template, request
from CNNmodel import process_test_data
from PIL import Image

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=["post", "get"])
def upload():
    target = os.path.join(APP_ROOT, "static/")
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "".join([target, filename])
        print(destination)
        os.remove("/home/shreyas/PycharmProjects/FashionDxSubmission/static/previous_uploaded.jpg")
        file.save(destination)
        img1 = Image.open(destination)
        img1.save('/home/shreyas/PycharmProjects/FashionDxSubmission/static/previous_uploaded.jpg')
        a = process_test_data('/home/shreyas/PycharmProjects/FashionDxSubmission/static/previous_uploaded.jpg')

    return render_template("complete.html", image_name1='previous_uploaded.jpg', value=a)


if __name__ == "__main__":
    app.run(port=3200, debug=True)






