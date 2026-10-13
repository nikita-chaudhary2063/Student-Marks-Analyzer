count_pass=0
count_fail=0
marks=[]
for i in range(1,6):
    mark=int(input("Enter marks for student:"))
    marks.append(mark)

    if mark>=40:
        count_pass=count_pass+1
    else:
        count_fail=count_fail+1

total_marks=sum(marks)
average_marks=total_marks/len(marks)
highest_marks=max(marks)

print("Student marks:",marks)
print("Total passed:",count_pass)
print("Total failed:",count_fail)
print("Total marks:",total_marks)
print("Average marks:",average_marks)
print("Highest marks:",highest_marks)