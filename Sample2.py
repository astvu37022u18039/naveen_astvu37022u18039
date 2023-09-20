class Player:
    def play(self):
        print("The player is playing cricket.")
        

class Batsman(Player):
    def play(self):
        Player.play(self)
        print("The batsman is batting\n")
        

class Bowler(Player):
    def play(self):
        Player.play(self)
        print("The bowler is bowling")

        
b = Batsman()
b1 = Bowler()
b.play()
b1.play()
