import random
def captcha():
    operators=['+','-','*','//']
    a=random.randint(1,100)
    b=random.randint(1,100)
    op=random.choice(operators)
    print("Captcha:",a,op,b)
    value=int(input("Enter the value after evaluating the above expression:"))
    if value==eval(str(a)+op+str(b)):
        return True
    else:
        return False



