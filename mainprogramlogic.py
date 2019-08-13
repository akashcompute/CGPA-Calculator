
grades1 = []
grade1point=[]
credit1 = []
grades2 = []
grade2point=[]
credit2 = []

#Collects the data of Class names and Grades in Letter Form
def collect():
    print("Enter 8 credits of first semester")
    y,x,a,z=0,0,0,0
    while (y <8):
        credit= int(input(""))
        credit1.append(credit)
        y = y +1
    print(credit1)
    print("Enter 8 grades of first semester")
    while(z<8):
        grades=input("")
        grades=grades.upper()
        if(grades=="O"):
            number=10
            grade1point.append(number)
        elif(grades=="A+"):
            number=9
            grade1point.append(number)
        elif(grades=="A"):
            number=8
            grade1point.append(number)
        elif(grades=="B+"):
            number=7
            grade1point.append(number)
        elif(grades=="B"):
            number=6
            grade1point.append(number)
        elif(grades=="C+"):
            number=5
            grade1point.append(number)
        elif(grades=="C"):
            number=4
            grade1point.append(number)
        elif(grades=="D+"):
            number=3
            grade1point.append(number)
        elif(grades=="D"):
            number=2
            grade1point.append(number)
        elif(grades=="E"):
            number=0
            grade1point.append(number)

        grades1.append(grades)
        z = z + 1
    print(grade1point)
    print(grades1)
    print("Enter 9 credits of second semester")
    while (x <9):
        credit= int(input(""))
        credit2.append(credit)
        x = x +1
    print(credit2)
    print("Enter 9 grades of second semester")
    while(a<9):
        grades=input("")
        grades=grades.upper()
        if(grades=="O"):
            number=10
            grade2point.append(number)
        elif(grades=="A+"):
            number=9
            grade2point.append(number)
        elif(grades=="A"):
            number=8
            grade2point.append(number)
        elif(grades=="B+"):
            number=7
            grade2point.append(number)
        elif(grades=="B"):
            number=6
            grade2point.append(number)
        elif(grades=="C+"):
            number=5
            grade2point.append(number)
        elif(grades=="C"):
            number=4
            grade2point.append(number)
        elif(grades=="D+"):
            number=3
            grade2point.append(number)
        elif(grades=="D"):
            number=2
            grade2point.append(number)
        elif(grades=="E"):
            number=0
            grade2point.append(number)
        grades2.append(grades)
        a= a + 1
    print(grade2point)
    print(grades2)
    calculate()

def calculate():
    i,j=0,0
    tgpa1,tgpa2,first_part1,second_part1,first_part2,second_part2=0,0,0,0,0,0
    while(i<8):
        first_part1+=credit1[i]*grade1point[i]
        second_part1+=credit1[i]
        i=i+1
    while(j<9):
        first_part2+=credit2[j]*grade2point[j]
        second_part2+=credit2[j]
        j=j+1
    tgpa1=first_part1/second_part1
    tgpa2=first_part2/second_part2
    tgpa1=float("{:.2f}".format(tgpa1))
    tgpa2=float("{:.2f}".format(tgpa2))
    print("Tgpa1=",tgpa1)
    print("Tgpa2=",tgpa2)
    cgpa=(tgpa1+tgpa2)/2
    print(cgpa)
    print("Cgpa=",cgpa)
    pass
collect()
