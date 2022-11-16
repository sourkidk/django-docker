import requests
from PIL import Image
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
    exifdata = img.getexif()
    metadata = {}
    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # decode bytes
        if isinstance(data, bytes):
            data = data.decode()
        metadata[tag] = data
        # print(metadata)
    mod_file_name = f'mod_{file_name}'
    img = img.convert('L')
    img.save(mod_file_name)

    return data, file_name, mod_file_name, metadata

# test
