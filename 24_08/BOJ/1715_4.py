import heapq
import sys

read = sys.stdin.readline


def main():
  N = int(read().rstrip())
  pq = []
  result = 0

  for i in range(N):
    num = int(read().rstrip())
    heapq.heappush(pq,num)
  while len(pq)>1:
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)
    result += a+b
    heapq.heappush(pq,a+b)

  print(result)

if __name__ == '__main__':
    main()