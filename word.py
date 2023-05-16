def find_short(s):
    # Split the string into words
    words = s.split()
    
    # Find the length of the shortest word
    shortest_length = min(len(word) for word in words)
    
    return shortest_length

# Test cases
print(find_short("Hello world"))  # Output: 5
print(find_short("This is a test"))  # Output: 1
print(find_short("Python is fun"))  # Output: 2
