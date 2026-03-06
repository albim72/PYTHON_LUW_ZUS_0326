from ftplib import FTP

host = "ftp.dlptest.com"
user = "dlpuser"
password = "rNrKYTX9g7z3RgJRmxWuGHbeu"

ftp = FTP(host)
ftp.login(user, password)

print("Połączono z FTP")

print("Lista plików:")
ftp.retrlines("LIST")

ftp.quit()
