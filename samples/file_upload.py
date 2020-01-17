import request

url = ''
file_name = ''
file_path = ''
def upload():
    res = request.post(url, files={'file': (file_name, open(file_path, 'rb')})

if __name__ == '__main__':
    upload()
