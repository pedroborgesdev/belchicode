# 🚀 BelchiCode  

![GitHub stars](https://img.shields.io/github/stars/pedroborgesdev/belchicode?style=socia) <!-- Shows the number of stars -->
![GitHub issues](https://img.shields.io/github/issues/pedroborgesdev/belchicode) <!-- Shows the number of open issues -->
![GitHub license](https://img.shields.io/github/license/pedroborgesdev/belchicode) <!-- Shows the project license -->

**BelchiCode** is a library that sends verification codes via Telegram, allowing you to verify whether the number entered by the user is valid. It was created to verify phone numbers at no cost, as other verification methods using SMTP or SMS have service or sending fees.

---

## 📌 Table of Contents  

- [🔔 Coming Soon](#-coming-soon)  
- [✨ Features](#-features)  
- [📦 Installation](#-installation)  
- [🛠️ How to Use](#-how-to-use)  
- [⚙️ How Was It Made?](#-how-was-it-made)  
- [📄 License](#-license)  
- [👋 Thank You!](#-thank-you)  

---   

## 🔔 Coming Soon  

- Library available on PyPI for terminal installation with `pip install`.  
- Improved AES encryption system ([TelegramCodeSender](https://github.com/pedroborgesdev/TelegramCodeSender)).  
- More endpoints for service control ([TelegramCodeSender](https://github.com/pedroborgesdev/TelegramCodeSender)).  

[Go to the top](#-belchicode)  

---  

## ✨ Features  

- **Free**: Sends messages at no cost.  
- **Easy integration**: Can be integrated in various ways, via APIs or other preferred methods.  
- **High concurrency support**: Works well under high load.  
- **Secure**: User data is encrypted.  

[Go to the top](#-belchicode)  

---  

## 📦 Installation  

Follow the steps below to install and configure the project locally.  

### Prerequisites  

- [Python](https://www.python.org/) (v3.8 or higher)  
- Python Libraries: [requests (2.32.3)](https://pypi.org/project/requests/)  

### Step by Step  

1. Clone the repository:  
   ```bash
   git clone https://github.com/pedroborgesdev/belchicode.git
   ```  
2. Enter the project folder:  
   ```bash
   cd belchicode
   ```  
3. Move the project to your Python library folder.  

[Go to the top](#-belchicode)  

---  

## 🛠️ How to Use  

### How does the user receive the code?  
1. The user must be registered with the bot by using the `/register` command in the chat.  
2. To view pending codes, the user can use the `/code` command in the chat.  

### Notes:  
- Once registered, the user does not need to use the `/code` command, as the message is automatically sent after the request.  
- If the user is not registered and the code has already been sent, the `/code` command can still retrieve it.  

Here are some examples of how to use the project:  

### 1. Basic Library Usage  

```python
# Import the library into the project
import belchicode as bc

# Information to make the application available
token = "YOUR-BOT-TOKEN"  # Your Telegram bot token
port = "2040"             # Port to host your application locally

# Information for sending messages
serviceName = "Your-company-name"  # Your service name
phoneNumber = 9999999999999        # Customer's phone number to receive the code

# Make the application available on the desired port with the Telegram token
host = bc.run(port, token)  # Returns the address for request usage

# Create a service based on the entered name
key = bc.service(host, serviceName)  # Returns the service key for sending codes

# Send the code to the client using the service key and provided phone number
requestID = bc.send(host, key, phoneNumber)  # Returns a request ID for validation

# Request the code
code = input("\nEnter the received code...: ")

# Verify the code validity using the key, request ID, and entered code
verify = bc.verify(host, key, requestID, code)  # Returns verification status: True | False

# Display the message based on code validation
if verify == True:
    print("\nThe entered code is CORRECT!")
else:
    print("\nThe entered code is INCORRECT!")
```  

### 2. Integrating the Library with an API  

```python
# Importing the libraries
from flask import Flask, jsonify
import belchicode as bc

app = Flask(__name__)

# Route to send codes to a specific number
@app.route("/send/<int:phone>", methods=["GET"])
def send(phone):
    # Get the request ID
    request_id = bc.send(host, key, phone)

    return jsonify({"request_id": request_id})

# Route to verify the entered code based on the request ID
@app.route("/verify/<requestID>/<code>", methods=["GET"])
def verify(requestID, code):
    # Get the verification result
    check = bc.verify(host, key, requestID, code)
    
    if check:
        return jsonify({"status": "USER_VALID_CODE"})
    else:
        return jsonify({"status": "USER_INVALID_CODE"})

if __name__ == "__main__":
   # Declaring server variables
   token = "YOUR-BOT-TOKEN"
   port = 2040

    # Starting the BelchiCode server
    host = bc.run(port, token)

    # Creating a sending service
    key = bc.service(host, "BradescoSMS")
    
    # Starting the Flask server
    app.run(debug=False, use_reloader=False)
```  

[Go to the top](#-belchicode)  

---  

## ⚙️ How Was It Made?  

This project is an integration to facilitate the use of the library. You can check out the project behind this library at [TelegramCodeSender](https://github.com/pedroborgesdev/TelegramCodeSender), which was developed in [Golang](https://go.dev/).  

### Why was it made in Golang?  
- Great for handling high concurrency.  
- Faster than Python.  

### Why was it integrated with Python?  
- To make it easier to use the Golang library.  
- Ability to integrate easily into other projects.  

[Go to the top](#-belchicode)  

---  

## 📄 License  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.  

[Go to the top](#-belchicode)  

---  

## 👋 Thank You!  

Thank you for checking out this project. This library was developed with the goal of helping the community, as service costs are becoming increasingly expensive. Making a paid system free is a great way to help.  

To see more projects like this, visit my GitHub profile: [pedroborgesdev](https://github.com/pedroborgesdev).  

🌟 Don't forget to star the project and follow me!  

[Go to the top](#-belchicode)
