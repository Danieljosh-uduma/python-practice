# annotations

def incre(n: list) -> int:
    sum: int = 0
    for x in n:
        sum += x
    return sum

print(incre([1,2,3,4]))    


# exceptions

try:
    greet = lambda n: 55 / n
    print(greet(0))
except:
    print('enter a non zero num')
else:
    pass
finally:
    pass

try:
    raise Exception('i hate you!')
except Exception as e:
    print(e)
    
class NotFound(Exception):
    print('not found!')


try:
    raise NotFound()
except NotFound as nf:
    print(nf)