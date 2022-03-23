import sys
import bisect

sys.stdin = open('bj1920_in.txt', 'r')

N = int(input())
card = list(map(int, input().split()))
card.sort()

M = int(input())
target = list(map(int, input().split()))


def binary_search(ordered_list, targets):
    index = bisect.bisect_left(ordered_list, targets)

    if index < len(ordered_list) and ordered_list[index] == targets:
        return 1
    else:
        return None


for n in range(M):
    if binary_search(card, target[n]):
        print(1)
    else:
        print(0)
