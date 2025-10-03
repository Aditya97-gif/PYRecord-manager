ch = 1
while ch in [1,2,3]:
    ch=int(input("Enter choice (1-Write with new entries, 2-Append, 3-Read,any other no to exit): "))
    if ch==1:
        num=int(input("Enter number of employees: "))
        with open('rec.txt','w') as f:
            for i in range(num):
                name=input(f"Enter name of employee {i+1}: ")
                age=input(f"Enter age of employee {i+1}: ")
                dept=input(f"Enter department of employee {i+1}: ")
                f.write(f"Name: {name}, Age: {age}, Department: {dept}\n")
        print("Employee records saved to rec.txt")
    elif ch==2:
        num=int(input("Enter number of employees: "))
        with open('rec.txt','a') as f:
            for i in range(num):
                name=input(f"Enter name of employee {i+1}: ")
                age=input(f"Enter age of employee {i+1}: ")
                dept=input(f"Enter department of employee {i+1}: ")
                f.write(f"Name: {name}, Age: {age}, Department: {dept}\n")
        print("Employee records appended to rec.txt")
    elif ch==3:
        with open('rec.txt','r') as f:
            print("\nEmployee Records:")
            print(f.read())
    else:
        print("Exiting...")
        break
    print("Do you want to enter the details in a new file? (yes/no) ")
    ans=input().lower()
    if ans=='yes':
        num=int(input("Enter number of employees: "))
        with open('new_rec.txt','w') as f:
            for i in range(num):
                name=input(f"Enter name of employee {i+1}: ")
                age=input(f"Enter age of employee {i+1}: ")
                dept=input(f"Enter department of employee {i+1}: ")
                f.write(f"Name: {name}, Age: {age}, Department: {dept}\n")
        print("Employee records saved to new_rec.txt")
    else:
        print("No new file created.")