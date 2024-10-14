from collections import deque
# Check Palindrome.
def checkPalindrome(word):
    word= word.lower()
    d = deque(word)
    while(len(d)>1):
        if d.pop()!= d.popleft():
            return False
    return True
    
def main():
    word = "Tacocat"
    
    print(checkPalindrome(word))

if __name__ == "__main__":
    main()