from sys import stdin as ss

'''
31900KB 1260ms
최소힙을 이용하여 가장 작은 카드뭉치를 더함

N == 1일때 비교를 할 필요x

N == 1일때의 조건이 필요x
31900KB 1124ms
'''
class Heap:
    def __init__(self):
        self.heap = []
        self.heap.append(None)

    def swap_up(self, idx):
        if idx <= 1:
            return False

        parent_idx = idx//2

        if self.heap[idx] < self.heap[parent_idx]:
            return True
        else:
            return False

    def heappush(self, data):
        self.heap.append(data)
        idx = len(self.heap) - 1

        while self.swap_up(idx):
            parent_idx = idx // 2
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx

        return 1

    def swap_down(self, idx):
        left_idx = idx * 2
        right_idx = idx * 2 + 1

        if left_idx >= len(self.heap):
            return False

        elif right_idx >= len(self.heap):
            if self.heap[left_idx] < self.heap[idx]:
                self.flag = 1
                return True
            else:
                return False

        else:
            if self.heap[left_idx] < self.heap[right_idx]:
                if self.heap[left_idx] < self.heap[idx]:
                    self.flag = 1
                    return True
                else:
                    return False

            else:
                if self.heap[right_idx] < self.heap[idx]:
                    self.flag = 2
                    return True
                else:
                    return False

    def heappop(self):
        if len(self.heap) <= 1:
            return 0

        heap_min = self.heap[1]
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        idx = 1

        while self.swap_down(idx):
            left_idx = idx * 2
            right_idx = idx * 2 + 1

            if self.flag == 1:
                self.heap[idx], self.heap[left_idx] = self.heap[left_idx], self.heap[idx]
                idx = left_idx
            else:
                self.heap[idx], self.heap[right_idx] = self.heap[right_idx], self.heap[idx]
                idx = right_idx

        return heap_min


    def heaplen(self):
        return len(self.heap) - 1



N = int(ss.readline())
heap = Heap()
result = 0
temp = 0

for _ in range(N):
    card = int(ss.readline())
    heap.heappush(card)

while heap.heaplen()-1:
    temp1 = heap.heappop()
    temp2 = heap.heappop()
    temp = temp1 + temp2
    heap.heappush(temp)
    result += temp


print(result)