sum=0
total=0
while True:
    numbers=float(input("Enter Student Number:"))
    sum+=numbers
    total +=1

    inter=input("You Want To Add More Numbers:(y/n)")
    if inter.casefold()=="n":
     break
average=sum/total
add=sum
percentage=(sum/100)*100
operator=input("What You Want To Do:(average/total/percentage)")
if operator=="average":
 print (f"Average of all class is:{average}")
if operator=="total":
 print (f"Sum of all student marks is:{add}")
if operator=="percentage":
 print (f"Percentage of all class is:{percentage}")
