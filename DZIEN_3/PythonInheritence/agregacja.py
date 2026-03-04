class Player:
    def __init__(self, name: str):
        self.name = name

class Team:
    def __init__(self, name: str, players: list[Player] | None = None):
        self.name = name
        self.players = players if players is not None else []

    def add_player(self, player: Player) -> None:
        self.players.append(player)

    def roster(self) -> list[str]:
        return [p.name for p in self.players]

p1 = Player("Cristiano")
p2 = Player("Robert")
p3 = Player("Messi")

barca = Team("Barcelona",[p2])
real = Team("Real Madrid",[p1,p3])

print(barca.name, barca.roster())
print(real.name, real.roster())

barca.add_player(p1)
print(barca.name, barca.roster())
print(real.name, real.roster())
