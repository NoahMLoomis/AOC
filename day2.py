class RockPaperScissors:
    def __init__(self):
        with open("./data/day2.txt", "r") as file:
            self.games = [line[:-1] for line in file.readlines()]

    def play_games(self):
        grand_total = 0
        for game in self.games:
            grand_total += self.get_score(game)
        return grand_total

    def get_score(self, game):
        total = 0
        elf = game[0]
        mine = game[2]
        if mine == 'X':
            mine = self.get_loss(elf)
        elif mine == 'Y':
            mine = self.get_tie(elf)
        else:
            mine = self.get_win(elf)

        if mine == "Y":
            total += 2
        elif mine == "X":
            total += 1
        else:
            total += 3
        total += self.get_result(elf, mine)
        return total

    def get_tie(self, elf):
        if elf == 'A':
            return 'X'
        elif elf == 'B':
            return 'Y'
        return "Z"

    def get_loss(self, elf):
        if elf == 'A':
            return 'Z'
        elif elf == 'B':
            return 'X'
        return 'Y'
    
    def get_win(self, elf):
        if elf == 'A':
            return 'Y'
        elif elf == 'B':
            return 'Z'
        return 'X'


    def get_result(self, elf, mine):
        if elf == 'A':
            if mine == 'Y':
                return 6
            elif mine == 'X':
                return 3
            else:
                return 0
        if elf == 'B':
            if mine == 'Y':
                return 3
            elif mine == 'X':
                return 0
            else:
                return 6
        if elf == 'C':
            if mine == 'Y':
                return 0
            elif mine == 'X':
                return 6
            else:
                return 3


game = RockPaperScissors()
print(game.play_games())
