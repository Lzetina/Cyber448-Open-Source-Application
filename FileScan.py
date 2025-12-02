
def get_file_scan(file_path):
    import requests
    import os
    import json
    # Path to VirusTotal file scan API endpoint, then the API key and file path are set with user input
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': '9cf48fa4d97ddba0b7843b56261da3493bdb515f7d94b03d04a1fd04d00b2c8f'}
    #file_path = input('Enter the path to the file to be scanned: ')
    scan_result = None 
    
    # Sends the file to VirusTotal for scanning
    # If successful, the scan results are printed; if there is an error, it is printed
    # Finally, the scan results are stored in a JSON file called data.json
    try:
        with open(file_path, 'rb') as file_to_scan:
            files = {'file': (os.path.basename(file_path), file_to_scan)}
            response = requests.post(url, files=files, params=params)
        
        if response.status_code == 200:
            scan_result = response.json()
        else:
            scan_result = {"error": f"HTTP {response.status_code}"}
    except Exception as e:
        scan_result = {"exception": str(e)}
        
    output_file = 'data.json'
    if os.path.exists(output_file):
        try:
            with open(output_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = []  # file exists but is corrupted or empty
    else:
        data = []  # file doesn't exist

                # Creates an array if the file does not exist
        
    data.append(scan_result)

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    
    return scan_result
        # At the end of the main function, the scan results are stored in a JSON file
    