import requests

def send(host: str, key: str, phone: str):
    url = f"{host}/send"
    
    phone = int(phone)
    
    payload = {
        "key": key,
        "phone": phone
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
            print("return: " + json_data.get("error"))
            return False
        
        callback = json_data.get("request_id") 
        callbackError = json_data.get("result") 
        
        if response.status_code == 200:
            print("return: " + callback)
            return callback
        else:
            print("return: " + callbackError)
            return False
    
    except requests.exceptions.SSLError as ssl_err:
        print(ssl_err)
        return False
    except requests.exceptions.RequestException as req_err:
        print(req_err)
        return False