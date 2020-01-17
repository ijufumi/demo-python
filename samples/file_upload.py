import requests

url = ''
file_name = ''
file_path = ''
def upload():
    res = requests.post(url, files={'file': (file_name, open(file_path, 'rb'))})
    print(res)

if __name__ == '__main__':
    upload()
