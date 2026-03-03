from dt_ext1 import User
from dt_ext2 import User

def demo_1_user() -> None:
    print("\n[1] User")
    u = User("marcin", "marcin@example.com")
    print(u)
    print(u.contact_card())

def demo_1a_user() -> None:
    print("\n[2] User")
    u = User("robert", "robert@example.com")
    print(u)
    print(u.contact_card())


if __name__ == "__main__":
    demo_1_user()
    demo_1a_user()
    # demo_2_cart()
    # demo_3_money()
    # demo_4_runsession()
