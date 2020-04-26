#/usr/bin/python
#There are  students in this class whose names and grades are assembled to build the following list:
#python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    marklist = []
    for _ in range(int(input())):
        marklist.append([(input()), float(input())])
        print (marklist)