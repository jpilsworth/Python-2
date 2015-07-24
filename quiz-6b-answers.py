''' 
Question 7
'''

n  = 1000
numbers = range(2, n)
results = []
def question(x):
    
    while numbers:
        i = numbers[0]
        results.append(i)
        for number in numbers:
            if number % i == 0:
                numbers.remove(number)
                
print question(numbers)
print len(results)


'''
Question 8
'''

slow_wumpuses, fast_wumpuses = 1000, 1
years=0
while slow_wumpuses > fast_wumpuses:
    slow_wumpuses *=.6*2
    fast_wumpuses *=.7*2
    years+=1
print "First year when the fast wumpuses outnumber the slow wumpuses : ", years

