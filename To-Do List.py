f = open("To-Do List Files.txt")


print("========== To-Do List ==========")
print(f.read())

userChoose = 0

while(userChoose != 5):
    print("[1]  Add Task")
    print("[2] Edit Task")
    print("[3] Delete Task")
    print("[[4] View Tasks")
    print("[5] Exit")
    
    userChoose = int(input("Choose an option: "))
    print(userChoose)

    if userChoose > 0 and userChoose < 5:
        match userChoose:
            case 1:   
                task = input("Enter Task you want to add: ")
                with open("To-Do List Files.txt", "a") as f:
                    f.write(task)
            
