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
            popped = temp
            self.top = temp.next
            temp = None
            return popped

    # "reverseCheck" examine the elements of the stack in reverse order
    def reverseCheck(self):
        if self.top is not None:
            reverseList = [] # a list to store alphanumeric characters from the input string "palindra_palooza" in reversed order
            temp = self.top
            while temp:
                # it appends the "data" of the current node to the list "reverseList"
                reverseList.append(temp.data)
                temp = temp.next
            return reverseList
        else:
            print("Stack underflow.")


# "palindrome_checker" is designed to check if the input string is a palindrome
def palindrome_checker(palindra_palooza):
    palindrome = palindra_palooza.lower()
    cleanedL = []  # a list to store alphanumeric characters from the input string "palindra_palooza"
    reversedS = Stack() # an instance to store the reversed order of the alphanumeric characters from the input string "palindra_palooza"

    for char in palindrome:
        if char.isalnum():  # if the character is alphanumeric...[1][2]
            cleanedL.append(char)  # [1] appends the character to list "cleanedL"
            reversedS.push(char)  # [2] pushes the character onto the stack "reversedS"

    reverseList = reversedS.reverseCheck()  # calls the "reverseCheck" to obtain a list of characters in reversed order
    cleanedPalindrome = ''.join(cleanedL)  # joins the list "cleanedL" into the string "''"
    reversedPalindrome = ''.join(reverseList)  # joins the list "reverseList" into the string "''"

    print(f"Inputted Element/s: {palindra_palooza}")
    print(f" Cleaned Element/s: {cleanedPalindrome}")
    print(f"Reversed Element/s: {reversedPalindrome}\n")

    # compares "cleanedPalindrome" and "reversePalindrome" to determine if it is a palindrome or not
    if cleanedPalindrome == reversedPalindrome:
        print(f"Therefore, {palindra_palooza} is a palindrome.")
    else:
        print(f'Therefore, "{palindra_palooza}" is not a palindrome.')


# where the code begins when run and make you input a sentence/word that you think is a palindrome
palindra_palooza = input("Enter your palindrome:\nFor example, 'Racecar' or 'A man, a plan, a canal, Panama!' are palindromes.\n-----> ")
palindrome_checker(palindra_palooza)


# Reflection:
# So far, this activity took a toll from my brain cells as it made me think how to reverse the order of the inputted palindrome and compare it to determine if it is a palindrome or not. To determine every characters of the inputted palindrome, I learned about .isalmun() that helped me along the code. The activity is quite hard only if I didn't stared at it hard enough for me understand.
