import sys

sys.stdin = open('bj1920_in.txt', 'r')

N = int(input())
card = list(map(int, input().split()))
card.sort()

M = int(input())
target = list(map(int, input().split()))


def binary_search(ordered_list, targets):
    left, right = 0, len(ordered_list)-1

    while left <= right:
        mid = (left+right)//2
        ...

        if targets < ordered_list[mid]:
            right = mid-1
        elif targets > ordered_list[mid]:
            left = mid+1
        else:
            return 1
    return 0


for n in range(M):
    if binary_search(card, target[n]):
        print(1)
    else:
        print(0)
