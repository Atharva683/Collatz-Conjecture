import matplotlib.pyplot as plt

def conjecture():
    while True:
        try:
            test_number = int(input("Enter any integer "))
            break
        except ValueError:
            print("Please enter a valid integer")
    
    original_number = test_number
    loop_times = 0
    numbers = []
    loop_start = None

    if test_number == 0:
        print("You entered zero which leads to undefined sequence in Collatz Conjecture")
        return
    
    while test_number not in [1, -1] and abs(test_number) < 10**8:
        numbers.append(test_number)

        if test_number % 2 == 0:
            test_number = test_number // 2
        else:
            test_number = 3 * test_number + 1
        loop_times += 1
        
        if test_number in numbers:
            loop_start = numbers.index(test_number)
            print(f"\Loop detected! The sequence loops back starting at step {loop_start}, with the number {test_number}.")  
            break

        if abs(test_number) > 10**8:
            print("The sequence is too large to be computed.")
            break
    numbers.append(test_number)

    print(f"\nResults for starting number {original_number}:")
    print(f"Number of steps: {loop_times}")
    if numbers:
        print(f"Highest value reached: {int(max(numbers))}")
        print(f"Lowest value reached: {int(min(numbers))}")

    print("\nSequence of numbers:")
    for step, value in enumerate(numbers, start=1):
        print(f"Step {step}: {value}")
    
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(numbers)), numbers, 
             linestyle='-', marker='o', 
             color='red', 
             markersize=4)
    plt.xlabel("Step")
    plt.ylabel("Number")
    plt.title(f"Collatz Sequence for {original_number}")
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    conjecture()


#the positive loop P: 4→2→1→4

#the zero loop Z: 0→0

#the small negative loop S: -1→-2→-1

#the medium-sized negative loop M: -5→-14→-7→-20→-10→-5

#the large negative loop L: -17→-50→-25→-74→-37→-110→-55→-164→-41→-122→-61→-182→-91→-272→-136→-68→-34→-17