def fb(a):
    a = int(a)
    if a % 15 == 0:
        return "FizzBuzz"
    elif a % 5 == 0:
        return "Buzz"
    elif a % 3 == 0:
        return "Fizz"
    else:
        return str(a)

def fizz_buzz(begin,end):
    res = [str(i) for i in range(begin,end+1)]
    res = " ".join(map(fb,res))
    return res