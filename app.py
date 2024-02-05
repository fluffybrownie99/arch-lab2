from connexion import NoContent
from update_event_data import update_event_data
import connexion, requests, yaml, logging, logging.config, datetime, json, uuid
#Log loader
with open('log_conf.yml', 'r') as f:
    log_config = yaml.safe_load(f.read())
    logging.config.dictConfig(log_config)
logger = logging.getLogger('basicLogger')

# URLs from YAML
with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())
    log_upload = app_config.get('eventstore1', {}).get('url')
    log_playback = app_config.get('eventstore2', {}).get('url')

# EndPoints


def media_upload(body):
    # update_event_data("media_upload",body)
    trace_id = str(uuid.uuid4())
    logger.info(f'Recieved event "media_upload" request with a trace id of {trace_id}')
    body['trace_id']=trace_id
    file_path = './test.jpg'
    files = {'file': open(file_path, 'rb')}
    media_upload_url = app_config["eventstore1"]["url"] 
    response = requests.post(media_upload_url, files=files, data=body)
    logger.info(f'Returned event "media_upload" response (Id: {trace_id}) with status {response.status_code}')
    return response.json(), 201  



def media_playback(body):
    # print(f'{body[mediaType]} \n{body[fileSize]} \n{body[uploadTime]} \n')
    trace_id = str(uuid.uuid4())
    logger.info(f'Recieved event "media_playback" request with a trace id of {trace_id}')
    body['trace_id']=trace_id
    media_playback_url = app_config["eventstore2"]["url"] 
    response = requests.post(media_playback_url, json=body, headers={"Content-Type": "application/json"})
    logger.info(f'Returned event "media_playback" response (Id: {trace_id}) with status {response.status_code}')
    return response.json(), 201  



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