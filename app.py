import connexion
from connexion import NoContent
import datetime
import json
from update_event_data import update_event_data
import requests

# CONSTS
DATA_STORAGE = 'http://127.0.0.1:8090/home/media/'
# EndPoints

def media_upload(body, deviceId):
    # update_event_data("media_upload",body)
    file_path = './test.jpg'
    files = {'file': open(file_path, 'rb')}
    media_upload_url = DATA_STORAGE + 'upload?deviceId=' + deviceId
    
    response = requests.post(media_upload_url, files=files, data=body)
    return response.json(), response.status_code


def media_playback(body, deviceId):
    # print(f'{body[mediaType]} \n{body[fileSize]} \n{body[uploadTime]} \n')
    media_playback_url = DATA_STORAGE + 'playback?deviceId=' + deviceId
    response = requests.post(media_playback_url, json=body, headers={"Content-Type": "application/json"})
    return NoContent, response.status_code


app = connexion.FlaskApp(__name__, specification_dir='')
#specification_dir is where to look for OpenAPI specifications. Empty string means
#look in the current directory
app.add_api("openapi.yaml",
            strict_validation=True,
            validate_responses=True)


#openapi.yaml is the name of the file
# strict_validation - whether to validate requests parameters or messages
# validate_responses - whether to validate the parameters in a request message against your OpenAPI specification


if __name__ == "__main__":
    app.run(port=8080)