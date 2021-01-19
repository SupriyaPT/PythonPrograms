try:
    raise NameError('HiThere')
except NameError as err:
    print('An exception flew by!',err)