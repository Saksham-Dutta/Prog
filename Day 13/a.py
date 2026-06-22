def input_and_display_list():
    n=int (input("Enter a number of the elements you want in the array"))
user_array=[]
print(f"Enter {n} elements:")
for i in range(n):
    element=input(f"Element{i+1}:")
    user_array.append(element)
    print("\n--- Displaying Array ---")
    print("As a structure:", user_array)
    print("Element by element:", end=" ")
    for item in user_array:
        print(item, end=" ")
    print()
input_and_display_list()
