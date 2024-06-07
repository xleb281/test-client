import requests

def mess():
    com = input("command:")
    data1 = input("data1:")
    data2 = input("data2:")
    message = {
        'sender': 'client',
        'text': com,
        'data1': data1,
        'data2': data2 
    }
    try:
        response = requests.post('http://127.0.0.1:5000/send_message', json=message)

        if response.status_code == 200:
            print('Message sent successfully!')
    except:
        print("err")
        mess()
mess()
