class Assignments:
    def __init__(self):
        self.sections = []
        self.containing_counter = 0
        with open('./data/day4.txt', 'r') as f:
            for line in f.readlines():
                s1, s2 = line.split(",")
                s1_start, s1_end = s1.split('-')
                s2_start, s2_end = s2.split('-')
                self.sections.append(
                    [
                        Section(int(s1_start), int(s1_end)),
                        Section(int(s2_start), int(s2_end[:-1]))
                    ]
                )
                
    def compare_sections(self):
        print(self.sections)
        for i in range(len(self.sections)):
            if self.sec_contains_another(self.sections[i][0], self.sections[i][1]):
                self.containing_counter += 1
                

    def sec_contains_another(self, s1, s2):
        return any(item in s1.section for item in s2.section) or any(item in s2.section for item in s1.section)
    
    
    def run(self):
        self.compare_sections()


class Section:
    def __init__(self, start, end):
        self.section = list(range(start, end+1))
        

a = Assignments()
a.run()
print(a.containing_counter)
