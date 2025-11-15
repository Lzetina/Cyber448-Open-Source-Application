import requests
import os
import json

def get_url_scan():
    # Path to URLScan scan API endpoint, then the API key and URL are set with user input
    url = 'https://urlscan.io/api/v1/scan/'
    headers = {'API-Key': '019a792f-70f0-70bf-9352-221e6b92eff2', 'Content-Type': 'application/json'}
    scan_url = input('Enter the URL to be scanned: ')
    
    # Sends the URL to URLScan.io for scanning
    # If successful, the scan results are printed; if there is an error, it is printed
    # Finally, the scan results are stored in a JSON file called data.json
    try:
        payload = {"url": scan_url, "visibility": "public"}
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        if response.status_code == 200:
            scan_result = response.json()
            print(scan_result)
        else:
            print('Error:', response.status_code)
            scan_result = {'error': response.status_code}
    except Exception as e:
        print('An error occurred:', str(e))
        scan_result = {'error': str(e)}
        
    finally:
        output_file = 'data.json'
        if os.path.exists(output_file):
            with open(output_file, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
                    # Attempts to load the file; if there is an error, it initializes an empty list
        else:
            data = []
            # Creates an array if the file does not exist
        
        data.append(scan_result)
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f'Data added to {output_file} successfully.')
        # At the end of the main function, the scan results are stored in a JSON file
