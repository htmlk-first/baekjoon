import sys
import bisect
import random

sys.stdin=open('bj1920_in.txt','r')

N=int(input())
card=list(map(int, input().split()))
card.sort()

M=int(input())
target=list(map(int,input().split()))


def search(ordered_list, target):
    ordered_list_size=len(ordered_list)
    for i in range(ordered_list_size):
        if target == ordered_list[i]:
            return 1
        elif ordered_list[i] > target:
            return None

card_list_size=len(card)
for i in range(card_list_size):
    result=search(card, target[i])
    if result is None:
        print('0')
    else:
        print('1')
