def counter(num):
    if num <= 0:
        return num
    else :
        return num+counter(num-1)


print(counter(5))
