import poplib
import email


POP_SERVER = "pop.gmail.com"

USERNAME = "twoj_email@gmail.com"
PASSWORD = "app_password"


server = poplib.POP3_SSL(POP_SERVER)

server.user(USERNAME)
server.pass_(PASSWORD)

num_messages = len(server.list()[1])

print("Liczba wiadomości:", num_messages)


resp, lines, octets = server.retr(num_messages)

msg = email.message_from_bytes(b"\n".join(lines))

print("From:", msg["From"])
print("Subject:", msg["Subject"])


server.quit()
