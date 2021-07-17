#!/usr/bin/env python3

def triple(num):
    return num * 3
    
def square(num):
    return num ** 2

def main():

    for num in range(1, 11):
        tri = triple(num)
        squ = square(num)
        
        if squ > tri:
            break
        else:
            print('triple({})=={} square({})=={}'.format(num, tri, num, squ))

if __name__ == "__main__":
    main()
