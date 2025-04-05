from flask import Flask, request, send_file, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'  # Directory to temporarily store received files
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/receive_file', methods=['POST'])
def receive_file():
    print(type(request.files))
    print("hello")

    if request.files:
        for f in request.files:
            print(f.file)
        
        print("world")
    
    

    # if f.filename == '':
    #     return 'No selected file', 400

    try:
        # Save the received file temporarily (optional, depending on your needs)
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # --- Logic to determine the file to return goes here ---
        # For this example, we'll just return the received file back
        file_to_return_path = filepath
        return_filename = file.filename

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
        # Clean up the temporarily saved file (optional)
        if 'filepath' in locals() and os.path.exists(filepath):
            os.remove(filepath)

if __name__ == '__main__':
    app.run(debug=True, port=5001, host="0.0.0.0", use_reloader=False) # Choose a port