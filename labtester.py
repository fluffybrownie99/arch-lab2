import requests
media_upload_url = 'http://127.0.0.1:8080/home/media/upload?deviceId=2'
file_path = './test.jpg'
files = {'file': open(file_path, 'rb')}  # Open the file in binary read mode
data = {
    'mediaType': 'photo',
    'fileSize': '1024',  # Size in bytes as a string
    'uploadTimestamp': '2023-01-12T10:00:00'
}

response = requests.post(media_upload_url, files=files, data=data)
files['file'].close()
print('Status Code:', response.status_code)
print('Response:', response.json())
