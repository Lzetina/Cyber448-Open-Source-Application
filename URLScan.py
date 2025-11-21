
def get_url_scan(scan_url):
    import requests
    import os
    import json
    # Path to URLScan scan API endpoint, then the API key and URL are set with user input
    url = 'https://urlscan.io/api/v1/scan/'
    headers = {'API-Key': '019a792f-70f0-70bf-9352-221e6b92eff2', 'Content-Type': 'application/json'}
    
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
            scan_result = {'error': response.status_code}
    except Exception as e:
        scan_result = {'error': str(e)}
        
    finally:
        output_file = 'data.json'
        if os.path.exists(output_file):
            try:
                with open(output_file, 'r', encoding='utf-8') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                    data = []
                    # Attempts to load the file; if there is an error, it initializes an empty list
        else:
            data = []
            # Creates an array if the file does not exist
        
        data.append(scan_result)
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        
        # At the end of the main function, the scan results are stored in a JSON file
    return scan_result
