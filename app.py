import connexion
from connexion import NoContent
import datetime
import json


def update_event_data(event_type, event_data):
    EVENTFILE = "events.json"
    MAX_EVENTS = 5
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    formatted_data = ", ".join([f"{key}: {event_data[key]}" for key in event_data])
    event = {
        "received_timestamp": current_time,
        "msg_data": formatted_data
    }
    try:
        with open( EVENTFILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    if event_type not in data:
        data[event_type] = {"count":0, "events":[]}
    data[event_type]["count"] += 1
    data[event_type]["events"].insert(0, event)
    data[event_type]["events"] = data[event_type]["events"][:MAX_EVENTS]
    with open(EVENTFILE, "w") as file:
        json.dump(data, file, indent=4)


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