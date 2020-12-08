print('This is my first module')
test='likhitha'
def find_index(to_search,target):
    for i,value in enumerate(to_search):
        if value == target:
            return i
    return -1        