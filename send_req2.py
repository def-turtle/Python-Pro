import requests
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def make_req(base_url="http://localhost:5000") -> None:
    logger.info(f"Making requests to {base_url}")
    try:
        response = requests.get(f"{base_url}/example-file_download")
        if response.status_code == 200:
            logger.info("file downloaded successfully") 
            file_content = response.content
            logger.debug(f"Downloaded file content: {file_content[:100]}...")  # Log the first 100 bytes of the file content for debugging
            # Save the downloaded content to a temporary file for upload
            with open("temp_download.txt", 'wb') as temp_file:
                temp_file.write(file_content)
                logger.info("Saved downloaded file to temp_download.txt")
            # Now upload the file back to the server
            with open("temp_download.txt", 'rb') as f:
                files = {'file': ('temp_download.txt', f)}
                upload_response = requests.post(f"{base_url}/upload_file", files=files)
                if upload_response.status_code == 200:
                    logger.info("file uploaded successfully")
                    logger.info(f"Upload response: {upload_response.text}")
                else:
                    logger.error(f"Failed to upload file. Status code: {upload_response.status_code}")
                    logger.error(f"Response: {upload_response.text}")
        else:
            logger.error(f"Failed to download file. Status code: {response.status_code}")
    except Exception as e:
        logger.error(f"Error: {e}")
if __name__ == "__main__":
    make_req()