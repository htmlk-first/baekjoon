import sys

sys.stdin = open('bj1920_in.txt', 'r')

N = int(input())
card = list(map(int, input().split()))
card.sort()

M = int(input())
target = list(map(int, input().split()))


def search(ordered_list, targets):
    ordered_list_size = len(ordered_list)
    for i in range(ordered_list_size):
        if targets == ordered_list[i]:
            return 1
        elif ordered_list[i] > targets:
            return None


for n in range(M):
    if search(card, target[n]):
        print(1)
    else:
        print(0)
