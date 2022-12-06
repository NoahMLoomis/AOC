def getTotals():
    with open('./data/day1.txt', 'r') as f:
        totals = []
        sum=0
        for line in f.readlines():
            print(line)
            if line == '\n':
                totals.append(sum)
                sum = 0
            else:
                sum += int(line)
        return totals

def get_highest(totals):
    return max(totals)
    
def remove_highest(totals):
    totals.remove(max(totals))
    
totals = getTotals()
sum = 0
for i in range(3):
    sum += get_highest(totals)
    remove_highest(totals)    
print(sum)
