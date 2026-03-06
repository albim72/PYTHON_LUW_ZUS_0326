import os
import paramiko
from scp import SCPClient
from concurrent.futures import ThreadPoolExecutor


HOST = "test.rebex.net"
USERNAME = "demo"
PASSWORD = "password"

LOCAL_DIR = "data"
REMOTE_DIR = "/pub/example"


def upload_file(filename):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(HOST, username=USERNAME, password=PASSWORD)

    scp = SCPClient(ssh.get_transport())

    local_path = os.path.join(LOCAL_DIR, filename)
    remote_path = REMOTE_DIR + "/" + filename

    print("wysyłam:", filename)

    scp.put(local_path, remote_path)

    scp.close()
    ssh.close()


def main():

    files = os.listdir(LOCAL_DIR)

    with ThreadPoolExecutor(max_workers=4) as executor:

        executor.map(upload_file, files)


if __name__ == "__main__":
    main()
