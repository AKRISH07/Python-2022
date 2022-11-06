scores = [10,20,30,55,88,90,67,99]

def res(score):
    return score>75

result = list(filter(res,scores))

print(result)


