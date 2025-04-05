from flask import Flask, request, send_file, render_template
import os, requests
import tempfile

app = Flask(__name__)

UPLOAD_FOLDER = "C:/Users/SurfacePro/Code/Marihacks2025'  # Directory to temporarily store received files"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/receive_file', methods=['POST'])
def receive_file():
    f = request.files['file']
    try:
        # Save the received file temporarily
        with tempfile.NamedTemporaryFile(delete=False, dir=UPLOAD_FOLDER) as temp_file:
            f.save(temp_file.name)
            file_to_return_path = temp_file.name
            return_filename = f.filename

        if os.path.exists(file_to_return_path):
            return send_file(
                file_to_return_path,
                as_attachment=True,
                download_name=return_filename
            )
        else:
            return 'Error: File to return not found on the server', 500

    except Exception as e:
        return f'Error processing the uploaded file: {str(e)}', 500

    finally:
        if 'file_to_return_path' in locals() and os.path.exists(file_to_return_path):
            try:
                os.remove(file_to_return_path)
            except PermissionError:
                print(f"Could not delete file: {file_to_return_path}")


send_path = "C:/Users/SurfacePro/Code/Marihacks2025/test.txt.zip"
@app.route('/send_zip_file', methods=['POST'])
def send_zip_file(zip_file_path=send_path, url="http://127.0.0.1:5001/receive_file"):
    """
    Sends a POST request with a zip file attached.

    :param zip_file_path: Path to the zip file to be sent.
    :param url: The URL to send the POST request to.
    :return: Response from the server.
    """
    try:
        with open(zip_file_path, 'rb') as f:
            files = {'file': (os.path.basename(zip_file_path), f, 'application/zip')}
            response = requests.post(url, files=files)
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.text
    except FileNotFoundError:
        return f"Error: Zip file not found at {zip_file_path}"
    except requests.exceptions.RequestException as e:
        return f"Error during file upload: {e}"

if __name__ == '__main__':
    # Example usage:

    app.run(debug=True, port=5001, host="0.0.0.0", use_reloader=False) # Choose a port

    response = send_zip_file(send_path, 'http://127.0.0.1:5001/send')
    print(response)
    print("hello")