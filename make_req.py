import requests
import logging
import os
from tempfile import NamedTemporaryFile

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
file_name = input("Enter file name: ")
def make_req(base_url="http://localhost:5000") -> None:
    """Download a file from the server and upload it back."""
    logger.info(f"Making requests to {base_url}")
    
    # Download file
    try:
        download_response = requests.get(f"{base_url}/example-file_download/{file_name}")
        if download_response.status_code == 200:
            logger.info("File downloaded successfully")
            file_content = download_response.content
            logger.debug(f"Downloaded file content: {file_content[:100]}...")
            
            # Save to a temporary file for upload
            with NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(file_content)
                temp_file.flush()
                temp_file_path = temp_file.name
                logger.info(f"Saved downloaded file to temporary path: {temp_file_path}")
        else:
            logger.error(f"Failed to download file. Status code: {download_response.status_code}")
            return
        
        # Upload file
        with open(temp_file_path, 'rb') as f:
            files = {'file': (os.path.basename(temp_file_path), f)}
            upload_response = requests.post(f"{base_url}/upload_file", files=files)
            if upload_response.status_code == 200:
                logger.info("File uploaded successfully")
                logger.info(f"Upload response: {upload_response.text}")
            else:
                logger.error(f"Failed to upload file. Status code: {upload_response.status_code}")
                logger.error(f"Response: {upload_response.text}")
    except Exception as e:
        logger.error(f"Error: {e}")


if __name__ == "__main__":
    make_req()


