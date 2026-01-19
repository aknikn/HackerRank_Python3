#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).______(thickness-1)+c+(c*i).______(thickness-1))
    # rjust, ljust

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))
    # center, center

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).______(thickness*6))
    # center

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))
    # center, center

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).______(thickness)+c+(c*(thickness-i-1)).______(thickness)).______(thickness*6))
    # rjust, ljust, rjust