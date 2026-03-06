import os
import paramiko


HOST = "test.rebex.net"
PORT = 22
USERNAME = "demo"
PASSWORD = "password"

REMOTE_DIR = "/pub/example"
LOCAL_DIR = "backup"


def download_directory(sftp, remote_path, local_path):

    os.makedirs(local_path, exist_ok=True)

    for item in sftp.listdir_attr(remote_path):

        remote_item = remote_path + "/" + item.filename
        local_item = os.path.join(local_path, item.filename)

        if paramiko.S_ISDIR(item.st_mode):

            download_directory(sftp, remote_item, local_item)

        else:
            print("Pobieram:", remote_item)
            sftp.get(remote_item, local_item)


def main():

    transport = paramiko.Transport((HOST, PORT))
    transport.connect(username=USERNAME, password=PASSWORD)

    sftp = paramiko.SFTPClient.from_transport(transport)

    download_directory(sftp, REMOTE_DIR, LOCAL_DIR)

    sftp.close()
    transport.close()


if __name__ == "__main__":
    main()
