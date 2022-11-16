import requests
from PIL import Image, ImageEnhance
from PIL.ExifTags import TAGS


def download_images():
    dog_api_call = requests.get('https://dog.ceo/api/breeds/image/random')
    image_url = dog_api_call.json().get("message")
    r = requests.get(image_url)
    keyword = 'breeds'
    before, keyword, after = image_url.partition(keyword)
    ext = after.replace('/', '')

    data = dog_api_call.json()
    file_name = f'dog_image_{ext}'

    with open(file_name, 'wb') as f:
        f.write(r.content)

    img = Image.open(file_name)

    info_dict = {
        "Filename": img.filename,
        "Image Size": img.size,
        "Image Height": img.height,
        "Image Width": img.width,
        "Image Format": img.format,
        "Image Mode": img.mode
    }

    mod_file_name = f'mod_{file_name}'
    img = img.convert('L')
    img.save(mod_file_name)



    return data, file_name, mod_file_name, info_dict
