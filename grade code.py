def assign_grade(num):
    while True:
        num = int(input('type your GWA to know your grade: '))
        if num >= 90 and num <= 100:
            print('Grade: A')
        elif num >= 80 and num <= 89:
            print('Grade: B')
        elif num >= 70 and num <= 79:
            print('Grade: C')
        elif num >= 60 and num <= 69:
            print('Grade: D')
        elif num >= 0 and num <= 59:
            print('Grade: F')
        else:
            print('Invalid score! Please enter a value between 0 and 100')
assign_grade(100)