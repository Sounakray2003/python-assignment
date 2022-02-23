a=int(input("Enter marks of first course out of 100 marks: "))
b=int(input("Enter marks of second course out of 100 marks : "))
c=int(input("Enter maarks of third course out of 100 marks : "))
g=int(input("Enter marks of fourth course out of 100 marks: "))
h=int(input("Enter marks of fifth course out of 100 marks: "))
percentage=(a+b+c+g+h)*100/500
#marks=([a,b,c,g,h])
#print(marks)
#if any(marks<40):
if a<40 or b<40 or c<40 or g<40 or h<40:
        print(" student has failed")
elif percentage >=75:
   print("Student has got Distinction")
elif percentage<75 and percentage>=60:
   print("Student has got First division")
elif percentage<60 and percentage>=50:
   print("Student has got Second division")
elif percentage<50 and percentage>=40:
   print("Student has got Third division")
else:
    print("Student has passed")
