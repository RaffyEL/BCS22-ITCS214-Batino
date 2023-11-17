# represents a node, which has two attributes namely "data (stores the value of node)" and "next (points to the next node in the list)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# represents the stack data structure that has one attribute, namely "top (points to the top element of the stack)"
class Stack:
    def __init__(self):
        self.top = None

    # "push" adds a new element into the top of the stack
    def push(self, data):
        new_node = Node(data)

        if self.top is None:
            self.top = new_node
            self.top.next = None

        else:
            new_node.next = self.top
            self.top = new_node

    # "pop" removes and returns the top element of the stack
    def pop(self):
        if self.top is None:
            print("Stack underflow.")
            return

        elif self.top.next is None:
            popped = self.top.data
            self.top = None
            return popped

        else:
            temp = self.top
            popped = temp.data
            self.top = temp.next
            temp = None
            return popped


# "palindrome_checker" is designed to check if the input string is a palindrome
def palindrome_checker(palindra_palooza):
    palindrome = palindra_palooza.lower()
    cleanedL = []  # a list to store alphanumeric characters from the input string "palindra_palooza"
    reversedS = Stack() # an instance to store the reversed order of the alphanumeric characters from the input string "palindra_palooza"

    list_of_alphanumeric_elements = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for char in palindrome:
        if char in list_of_alphanumeric_elements:  # if the character is alphanumeric...[1][2]
            cleanedL.append(char)  # [1] appends the character to list "cleanedL"
            reversedS.push(char)  # [2] pushes the character onto the stack "reversedS"

    reverseList = [] # a list to store alphanumeric characters in REVERSE order from the input string "palindra_palooza"

    # Iterates over the characters in list "cleanedL" and calls the "pop" method, reversing the order character by character as it stores it in the list "reverseList"
    for char in range(len(cleanedL)):
        popped = reversedS.pop()
        reverseList.append(popped)


    cleanedPalindrome = ''.join(cleanedL)  # joins the list "cleanedL" into the string "''"
    reversedPalindrome = ''.join(reverseList)  # joins the list "reverseList" into the string "''"

    print(f"Inputted Element/s: {palindra_palooza}")
    print(f" Cleaned Element/s: {cleanedPalindrome}")
    print(f"Reversed Element/s: {reversedPalindrome}\n")

    # compares "cleanedPalindrome" and "reversePalindrome" to determine if it is a palindrome or not
    if cleanedPalindrome == reversedPalindrome:
        print(f'!!! Therefore, "{palindra_palooza}" is a palindrome. !!!\n')
    else:
        print(f'!!! Therefore, "{palindra_palooza}" is not a palindrome. !!!\n')


while True:
    # where the code begins when run and make you input a sentence/word that you think is a palindrome
    palindra_palooza = input("Enter your palindrome:\nFor example, 'Racecar' or 'A man, a plan, a canal, Panama!' are palindromes.\n-----> ")
    palindrome_checker(palindra_palooza)
    option = input("Continue using the checker? [yes] [no]\n-----> ")
    if option.lower() == "yes":
        print()
        continue
    elif option.lower() == "no":
        print()
        print("Closing the checker...")
        break
    else:
        print("Invalid option. Please choose between [yes] [no].\n")


# Reflection:
# So far, this activity has taken a toll on my brain cells as it made me think about how to reverse the order of the inputted palindrome and compare it to determine if it is a palindrome or not. To determine every character of the inputted palindrome, I learned about .isalmun() which helped me along the code. Unfortunately, .isalnum() is not allowed to be used so I created a list of alphabets and numbers to compare characters from the inputted value. The activity was quite hard only if I didn't stare at it hard enough for me to understand.
