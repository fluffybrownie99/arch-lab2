import connexion
from connexion import NoContent
import datetime
import json
from update_event_data import update_event_data



def media_upload(body, deviceId):
    media_id = "123e4567-e89b-12d3-a456-426614174000"
    update_event_data("media_upload",body)
    print(body)
    return body, 201


def media_playback(body, deviceId):
    # print(f'{body[mediaType]} \n{body[fileSize]} \n{body[uploadTime]} \n')
    update_event_data("media_playback", body)
    return body, 201


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