import sys

sys.stdin=open('bj1920_in.txt','r')

N=int(input())
card=list(map(int, input().split()))
card.sort()

M=int(input())
target=list(map(int,input().split()))


def binary_search(ordered_list, target):
    left, right = 0, len(ordered_list)-1

    while left <= right:
        mid=(left+right)//2
        ...

        if target < ordered_list[mid]:
            right=mid-1
        elif target > ordered_list[mid]:
            left=mid+1
        else:
            return 1
    return 0

for i in range(len(card)):
    print(binary_search(card, target[i]))
    # result=binary_search(card, target[i])
    # if result is None:
    #     print('0')
    # else:
    #     print('1')
