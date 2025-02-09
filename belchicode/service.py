import requests

def service(host, serviceName):
    url = f"{host}/services"
    
    payload = {
        "name": serviceName
    }
    
    print(f"\nurl: {url}")
    print(f"payload: {payload}")

    try:
        response = requests.post(
            url,
            json=payload,  
            verify=True,   
            timeout=5      
        )
        
        json_data = response.json()

        if json_data.get("error"):
            print(json_data.get("error"))
            return False
        
        callback = json_data.get("key")

        if response.status_code == 201:
            print("return: " + callback)
            return callback
        else:
            return False
    
    except requests.exceptions.SSLError as ssl_err:
        print(ssl_err)
        return False
    except requests.exceptions.RequestException as req_err:
        print(req_err)
        return False