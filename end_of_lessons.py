lesson = int(input())
if lesson == 1:
    print((585 // 60) % 23, (585 % 60) % 59)
if lesson == 2:
    print((635 // 60) % 23, (635 % 60) % 59)
if lesson == 3:
    print((695 // 60) % 23, (695 % 60) % 59)
if lesson == 4:
    print((745 // 60) % 23, (745 % 60) % 59)
if lesson == 5:
    print((805 // 60) % 23, (805 % 60) % 59)
if lesson == 6:
    print((855 // 60) % 23, (855 % 60) % 59)
if lesson == 7:
    print((915 // 60) % 23, (915 % 60) % 59)
if lesson == 8:
    print((965 // 60) % 23, (965 % 60) % 59)
if lesson == 9:
    print((1025 // 60) % 23, (1025 % 60) % 59)
if lesson == 10:
    print((1135 // 60) % 23, (1135 % 60) % 59)
else:
    print('on day maximum 10 lessons :)')

lesson = int(input())
a = lesson * 45 + (lesson // 2) * 5 + ((lesson + 1) // 2 - 1) * 15
print(lesson // 60 + 9, lesson % 60)
