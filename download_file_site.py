import io
from tempfile import NamedTemporaryFile
from pathlib import Path
import flask
# import magic

FILESDIR = Path(__file__).parent / "files"
FILESDIR.mkdir(exist_ok=True)

app = flask.Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/")
def home():
    return "<h1>Hello HTTP world</h1>"
@app.route("/example-file_download")
def download_file():
    file_name = "example.txt"
    random_content = "This is an example file for download."
    # Create a temporary file and return it
    temp_file_path = FILESDIR / "temp_download.txt"
    with open(temp_file_path, 'w') as f:
        f.write(random_content)
    return flask.send_file(
        temp_file_path,
        as_attachment=True,
        download_name=file_name,
        mimetype='text/plain'
    )

@app.route("/upload_file", methods=["POST"])
def upload_file():
    if 'file' not in flask.request.files:
        return "No file part in the request", 400
    file = flask.request.files['file']
    if file.filename == '':
        return "No selected file", 400
    save_path = FILESDIR / file.filename
    file.save(save_path)
    return f"File '{file.filename}' uploaded successfully to {save_path}!", 200
# @app.route("/example_file_download_2")
# def download_file_2():
#     path_to_image = FILESDIR / "example.png"
#     mimetype = magic.from_file(path_to_image, mime=True)
#     if path_to_image.realative_to

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)