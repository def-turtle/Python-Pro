import flask
app = flask.Flask(__name__)
@app.route("/")
def home():
    return "<h1>Hello HTTP world</h1>"

@app.route("/download_file/<filename>")
def download_file(filename):
    random_content = "bla bla bla " * 1000
    temp_file_path = f"C:/Users/User/PycharmProjects/Python-Pro/temp/{filename}"
    with open(temp_file_path, 'wb') as f:
        f.write(random_content.encode('utf-8'))
        f.close()
    return flask.send_file(temp_file_path, as_attachment=True, mimetype='text/plain')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
