import firebase_admin
from firebase_admin import credentials, storage
import base64

def download_and_encode_image(bucket_name, source_blob_name):
    """Download and base64-encode an image from Firebase Storage."""
    bucket = storage.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    # Download the image data as bytes
    image_data = blob.download_as_bytes()

    # Encode the image data to base64
    base64_encoded_image = base64.b64encode(image_data).decode()

    return base64_encoded_image

# Test function
def write_to_txt(base64_encoded_image, output_file_path):
    """Write base64-encoded image data to a text file."""
    with open(output_file_path, 'w') as file:
        file.write(base64_encoded_image)
    print(f"Base64-encoded image data written to {output_file_path}")
    
    
def storagemain(image_name):
    output_file_path = 'output.txt'

    # Replace with your Firebase Storage bucket name
    bucket_name = 'canvas-chronicles.appspot.com'
    
    # Replace with the path to the folder containing the image
    folder_path = 'images/'
    
    # Replace with the name of the image you want to download and encode
    source_blob_name = "Canvas2"
    
    # Initialize Firebase app
    cred = credentials.Certificate("./serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {'storageBucket': bucket_name},'IMAGE')
    
    # Download and base64-encode the image
    base64_encoded_image = download_and_encode_image(bucket_name, folder_path + source_blob_name)
    

    # Print the base64-encoded image data
    write_to_txt(base64_encoded_image, output_file_path)
    # print(f"Base64 Encoded Image:\n{base64_encoded_image}")

if __name__ == "__main__":
    storagemain()