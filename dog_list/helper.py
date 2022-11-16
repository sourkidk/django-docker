import requests
from PIL import Image, ImageEnhance
from PIL.ExifTags import TAGS

# Function to call dog.ceo api, download dog image, modify and save a copy, and serialize metadata
def download_images():
    dog_api_call = requests.get('https://dog.ceo/api/breeds/image/random')
    image_url = dog_api_call.json().get("message")
    image_request = requests.get(image_url)
    # partioning original filename and reformatting for our filename
    keyword = 'breeds'
    before, keyword, after = image_url.partition(keyword)
    extension = after.replace('/', '')

    json_message = dog_api_call.json()
    file_name = f'dog_image_{extension}'

    with open(file_name, 'wb') as f:
        f.write(image_request.content)

    img = Image.open(file_name)

    metadata = {
        "Filename": img.filename,
        "Image Size": img.size,
        "Image Height": img.height,
        "Image Width": img.width,
        "Image Format": img.format,
        "Image Mode": img.mode
    }

    mod_file_name = f'mod_{file_name}'
    # Converts image to greyscale
    img = img.convert('L')
    img.save(mod_file_name)
    return json_message, file_name, mod_file_name, metadata
