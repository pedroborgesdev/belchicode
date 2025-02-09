import subprocess as sb
from pathlib import Path
import threading
import socket
import time

def check_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('localhost', port))
        except socket.error:
            return True
        else:
            return False

def run(port: str, token: str):
    print("Staring application...")
    print(f"Checking port: {port}...")

    check = check_port(int(port))

    if check:
        print(f"Error: port: {port} already in use, change another.")
        return False

    print(f"Server: http://localhost:{port}")
    print(f"Token: {token}")
    libPath = Path(__file__).resolve()
    packagesDir = str(libPath.parent / "packages")

    def start_process():
        try:
            process = sb.Popen([str(Path(packagesDir) / "api.exe"), "-port", port, "-telegramToken", token], cwd=packagesDir, stderr=sb.PIPE, stdout=sb.PIPE)
            process.communicate()
        except Exception as e:
            print(f"Error serving application on {port}, change another")
            return False

    threading.Thread(target=start_process).start()

    time.sleep(2)

    return f"http://localhost:{port}"

