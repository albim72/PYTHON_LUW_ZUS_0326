import paramiko
from scp import SCPClient

host = "test.rebex.net"
username = "demo"
password = "password"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(host, username=username, password=password)

scp = SCPClient(ssh.get_transport())

# pobranie pliku z serwera
scp.get("readme.txt", "readme_local.txt")

print("Plik pobrany")

scp.close()
ssh.close()
