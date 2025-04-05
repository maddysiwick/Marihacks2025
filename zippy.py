import zipfile, os


def compress_to_zip(file_path, output_zip_path):
    """
    Compresses a file into a .zip archive.

    :param file_path: Path to the file to be compressed.
    :param output_zip_path: Path where the .zip file will be created.
    """
    try:
        with zipfile.ZipFile(output_zip_path, 'w') as zipf:
            zipf.write(file_path, os.path.basename(file_path))
        print(f"File compressed successfully: {output_zip_path}")
    except Exception as e:
        print(f"Error compressing file: {str(e)}")


def extract_from_zip(zip_file_path, extract_to_folder):
    """
    Extracts a .zip archive to a specified folder.

    :param zip_file_path: Path to the .zip file to be extracted.
    :param extract_to_folder: Folder where the contents will be extracted.
    """
    try:
        # Ensure the extraction folder exists
        if not os.path.exists(extract_to_folder):
            os.makedirs(extract_to_folder)

        with zipfile.ZipFile(zip_file_path, 'r') as zipf:
            # Extract all files to the specified folder
            zipf.extractall(extract_to_folder)

        print(f"File extracted successfully to: {extract_to_folder}")

        # Debugging: List extracted files
        extracted_files = os.listdir(extract_to_folder)
        print(f"Extracted files: {extracted_files}")

    except zipfile.BadZipFile:
        print(f"Error: The file {zip_file_path} is not a valid zip file.")
    except Exception as e:
        print(f"Error extracting file: {str(e)}")

