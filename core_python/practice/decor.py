def main(func):
    def check(num):
        val = func(num)
        return val.upper()
        
    return check

@main
def get(num):
    return num

num = input('enter number: ')
val = get(num)
print(val)