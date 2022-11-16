Docker-Django API Practical

Please see requirements.txt for full list of dependencies.

Instructions for installing Docker Application:
---





Instructions for use:
1. If development server is not running.  Run 'docker-compose up --build' to build the container and start the app.
2. The API can be consumed via a request client(ie. Postman) or via the browsable API interface included with the Django
    REST framework.  These instructions will use the browsable interface.
3. In a browser, navigate to 'http://127.0.0.1:8000/'.  You should see API Root page.  If you get an error page, please
    be sure the dev server is running.
4.  To test the key/value endpoints, click the link in red for "key": "http://127.0.0.1:8000/key/".
5.  To use GET functionality, we will first need to create a few key/value pairs. Scroll down to the HTML form.  You can use
    the form or click the Raw Data tab if you prefer to test with raw JSON.
6. Enter a 'key' without a value and click 'POST'.  You should see the response above including the raw JSON that was sent by
    the serializer.  Note: the default value of 1 for the value.  You can choose a different value by entering any integer if desired,
    however, 1 is the default if left blank.
7.  From this same page "http://127.0.0.1:8000/key/", the GET button at the top will return all the current key/value pairs in a JSON structure.
8.  To use the individual PATCH feature to increment a value, you must navigate to "http://127.0.0.1:8000/increment/<key>".  Any spaces
    in the 'key' name can be substituted with '%20' for the url.
9.  Once on the 'Increment Key' page, click the 'Raw Data' tab to access the PATCH request.  Click patch to increment the value up by 1.



10.  To use the dog API functionality, navigate to http://127.0.0.1:8000/key/dog/" or navigate back to the API root and then use
    the link to the 'dog' API.
11.  Currently the 'POST' method only gets a single dog from the original 'DOG-CEO' site.  Simply click 'POST' to download a random dog image from the site.
12.  Each dog object has four fields(original_json, image, modified_image, and metadata).  Both image and modified_image contain the local urls for the saved images.
13.  The 'GET' button will return all dog objects in their serialized format.  You can click the link on the 'image' or 'modified_image' fields for
    any dog to view the image.  The original JSON data is also included as a dedicated field as is the metadata field.
    Note: I previously had a functional method for parsing the exif metadata if it existed, but chose to go with the more consistent fields that are now
    included as metadata.


