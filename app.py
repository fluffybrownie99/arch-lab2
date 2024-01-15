import connexion
from connexion import NoContent

def media_upload(body, deviceId):
    media_id = "123e4567-e89b-12d3-a456-426614174000"
    return {'mediaId': media_id}, 201

    
def media_playback(body, deviceId):
    return NoContent, 201

app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("openapi.yaml",
            strict_validation=True,
            validate_responses=True)

if __name__ == "__main__":
    app.run(port=8080)