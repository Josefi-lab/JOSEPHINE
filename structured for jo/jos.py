names =["Petra","Jo", "Sean"]
#Change an item by index
names[1] ="Paul"

#Add to the End
names.append("Grace")
#insert a position 
names.insert(1, "David")
#Extend with another list
names.extend(["Eve","Noah"])

print(names)


marks =[23,40,56,93,20]
n = int(input("How many marks?"))

for i in range(n):
    value = int(input("Enter mark:"))
    marks.append(value)
    
if len(marks) > 0:
    average = sum(marks) / len(marks)
    print("Average:", average)
    print("Highest:", max(marks))
    print("Lowest:", min(marks))
else:
    print("No marks entered.")
    

def count_above_50(numbers):
    count=0
    for n in numbers:
        match n > 50:
            case True:
                count = count + 1
            case False:
                pass
    return count
scores =[10,60,45,90]
print(count_above_50(scores))

    


