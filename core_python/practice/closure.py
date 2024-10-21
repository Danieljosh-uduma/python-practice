def speak():
    msg = 'hello'
    
    def say(name):
        nonlocal msg
        msg += name
        return msg
    
    return say

word = speak()
print(word('josh'))