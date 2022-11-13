import requests
def download_images():
    for i in range(1, 2):
        dog_api_call = requests.get('https://dog.ceo/api/breeds/image/random')
        image_url = dog_api_call.json().get("message")
        r = requests.get(image_url)
        keyword = 'breeds'
        before, keyword, after = image_url.partition(keyword)

        file_name = f'test_image_file{i}.jpg'

        with open(file_name, 'wb') as f:
            f.write(r.content)
    return