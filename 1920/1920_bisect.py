import sys
import bisect

sys.stdin=open('bj1920_in.txt','r')

N=int(input())
card=list(map(int, input().split()))
card.sort()

M=int(input())
target=list(map(int,input().split()))


