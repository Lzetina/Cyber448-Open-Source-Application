import requests


def get_phone_number():
    phone = input('Enter phone number: ')
    CC = input('Enter default country code (optional): ')
    url = 'https://api.veriphone.io/v2/verify?phone=' + phone + '&country_code=' + CC + '&key=DD0982B23C8641CC97CEF6682591574C'
    #url for veriphone API
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            posts = response.json()
            print(posts)
        else:
            print('Error:', response.status_code)
    except Exception as e:
        print('An error occurred:', str(e))
    
    