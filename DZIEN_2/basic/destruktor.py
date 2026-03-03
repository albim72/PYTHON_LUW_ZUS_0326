class TempFile:

    def __init__(self, name: str):
        self.name = name
        print(f"[init] Tworzę zasób: {self.name}")

    def write(self,text: str):
        print(f"[Write] ({self.name}) {text}    )")

    def close(self):
        print(f"[Close] Zamykam ({self.name})")

    def __del__(self):
        print(f"[del] Usuwam ({self.name})")


obj = TempFile("session.tmp")
obj.write("Hello")
obj.close()

del obj
print("co dalej?")

obj.write("Hello")
