import random

def generate_list():
    alist = [x for x in range(random.randint(-10,10))]
    assert len(alist)!=0,"alist is null"
    sum=0
    for i in alist:
        sum+=alist[i]
    print(sum)
    return alist

"""
print a generate list
"""

def printIt():
    print(generate_list())
    
def main():
    printIt()

"""
If this script file is called, it will run main() directly
"""

if __name__ == '__main__':
    print("Test printIt():")
    main()
    