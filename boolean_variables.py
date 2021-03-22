 # A student makes honour roll if their average is >=85
 # and their lowest grade is not below 70
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))
# lowest_grade = float(lowest_grade)

# if gpa >= .85:
#     if lowest_grade >= .70:
#         print('You made the honour roll')

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False

# Somewhere later in your code if you need to check if students are 
# on honoour roll, all I need to do is check the boolean variable I 
#  set earlier in my code

if honour_roll:
    print('You made the honour roll')
else:
    print('Study harder, fool!')