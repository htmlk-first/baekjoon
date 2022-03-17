import sys
import bisect

#sys.stdin=open('bj1920_in.txt','r')

N=int(input())
card=list(map(int, input().split()))
card.sort()

M=int(input())
target=list(map(int,input().split()))

def binary_search(ordered_list, target):
    index=bisect.bisect_left(ordered_list, target)

    if index<len(ordered_list) and ordered_list[index]==target:
        return 1
    else:
        return 0

card_list_size=len(card)
for i in range(card_list_size):
    print(binary_search(card,target[i]))