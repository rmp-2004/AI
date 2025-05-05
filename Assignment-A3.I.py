# Assignment-A3.I (Selection Sort)

numbers=[]

# Function to take input for numbers
def input_numbers():
        total=int(input("How many numbers you wish to enter?\nTotal numbers:\t"))
        for i in range(1, total+1):
                numIn=float(input(f"Enter number {i}:\t"))
                numbers.append(numIn)
        print("The numbers you've entered are:\t", numbers)

# Function for selection sort
def selection():
    for i in range(len(numbers)):
        min_index=i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index=j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    print("Numbers sorted in ascending order using selection sort:\t", numbers)

def choose_optn():
        while True:
                print("Choose an option from the menu below:")
                print("1 -> Input numbers")
                print("2 -> Apply Selection Sorting")
                print("3 -> Exit")
                optn=int(input("Choose an option (1-3):\t"))

                if optn==1:
                        input_numbers()
                elif optn==2:
                        selection()
                elif optn==3:
                    print("\n## END OF CODE\n")
                    quit()
                else:
                        print("\nPlease choose a valid option (1-3).\n")
choose_optn()

