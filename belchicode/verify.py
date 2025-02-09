import requests

def verify(host: str, key: str, requestID: str, code: str):
    url = f"{host}/verify"
    
    code = str(code)
    
    payload = {
        "key": key,
        "id": requestID,
        "code": code
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
        print(json_data)

        if json_data.get("error"):
            print(json_data.get("error"))
            return False
        
        callback = json_data.get("result")
        
        if json_data.get("result") == "success":
            print("return: " + callback)
            return True
        else:
            print("return: " + callback)
            return False
    
    except requests.exceptions.SSLError as ssl_err:
        print(ssl_err)
        return False
    except requests.exceptions.RequestException as req_err:
        print(req_err)
        return False