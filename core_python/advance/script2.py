# decorators

def gender(func):
    def check_gender():
        val = func()
        if val == 'male':
            print('you are a man')
        else:
            print('you are a woman')
    return check_gender


@gender
def gender_check():
    gender = input()
    return gender

gender_check()
