f = open("To-Do List Files.txt")


print("========== To-Do List ==========")
print(f.read())

userChoose = input()

while(userChoose != 5):
    print("[1]  Add Task")
    print("[2] Edit Task")
    print("[3] Delete Task")
    print("[4] View Tasks")
    print("[5] Exitk")

    match userChoose:
        case 1:
            
            

