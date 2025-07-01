class Player:
    def __init__(self):
        self.name = "Mick Jagger"
        self.score = 0

    def getName(self):
        return self.name

    def receive_score(self, score):
        self.score += score
