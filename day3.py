import string


class Packing:
    def __init__(self):
        self.total = 0
        self.rucksacks = []
        self.groups = []
        with open('./data/day3.txt', 'r') as f:
            for line in f.readlines():
                ruck = Rucksack(line[:-1])
                self.rucksacks.append(ruck)
            ruck_set = []
            count = 0
            for ruck in self.rucksacks:
                ruck_set.append(ruck)
                if count >= 2:
                    self.groups.append(ruck_set)
                    ruck_set = []
                    count = 0
                else:
                    count += 1

        for ruck in self.rucksacks:
            self.total += ruck.score
        self.group_totals = 0
        for group in self.groups:
            matching = self.get_matching_letters(group)
            self.group_totals += self.get_score(matching)

        print(self.groups)
        print(self.group_totals)

    def get_matching_letters(self, group):
        matching = set()
        rack1 = group[0].rucksack
        rack2 = group[1].rucksack
        rack3 = group[2].rucksack

        # Efficieny be dammed
        for letter in rack1:
            if letter in rack2 and letter in rack3:
                matching.add(letter)
        for letter in rack2:
            if letter in rack1 and letter in rack3:
                matching.add(letter)
        for letter in rack3:
            if letter in rack2 and letter in rack1:
                matching.add(letter)
        return matching

    def get_score(self, matching):
        total = 0
        for item in matching:
            total += string.ascii_letters.index(item) + 1
        return total


class Rucksack:
    def __init__(self, rucksack):
        self.rucksack = rucksack
        self.container1, self.container2 = self.split_rucksack()
        self.matching = self.get_matching_items()
        self.score = self.get_score()

    def __str__(self):
        return self.rucksack

    def __repr__(self):
        return self.rucksack

    def split_rucksack(self):
        c1 = slice(0, len(self.rucksack)//2)
        c2 = slice(len(self.rucksack)//2, len(self.rucksack))
        return self.rucksack[c1], self.rucksack[c2]

    def get_matching_items(self):
        matching = set()
        if len(self.container2) >= len(self.container1):
            for letter in self.container2:
                if letter in self.container1:
                    matching.add(letter)
        else:
            for letter in self.container1:
                if letter in self.container2:
                    matching.add(letter)

        return matching

    def get_score(self):
        total = 0
        for item in self.matching:
            total += string.ascii_letters.index(item) + 1
        return total


print(Packing().total)
