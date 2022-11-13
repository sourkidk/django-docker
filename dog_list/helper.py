import requests
def download_images():
    for i in range(1, 24):
        dog_api_call = requests.get('https://dog.ceo/api/breeds/image/random')
        image_url = dog_api_call.json().get("message")
        r = requests.get(image_url)

        # print(search('breeds/', image_url))

        file_name = f'test_image_file{i}.jpg'

        with open(file_name, 'wb') as f:
            f.write(r.content)
    return