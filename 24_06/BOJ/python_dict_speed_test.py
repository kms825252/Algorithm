import time
import random

'''
## Dictionary과 List에서 탐색의 성능 비교 ##

- 비교 상황 key 값이 n(0~1000000) 인
value를 찾는 시간을 비교

조건 1. list와 dict의 key와 value는 동일
조건 2. list와 dict에 값을 넣는 순서 동일
조건 3. key값은 중복없이 랜덤(0~1000000)
조건 4. value는 중복없이 랜덤(0~1000000)
'''


def create_data(n):
    keys = [i for i in range(n)]
    random.shuffle(keys)
    # values = [random.randrange(0, 100) for i in range(n)]
    values = [i for i in range(n)]
    random.shuffle(keys)
    data = [[keys[i], values[i]] for i in range(n)]
    return data


def create_dict(li):
    d = {}
    for i in li:
        d[i[0]] = i[1]
    return d


def find_list(key, li):
    start = time.time()
    for i in li:
        if i[0] == key:
            t = (time.time() - start) * 1000
            return {'key': i[0], 'value': i[1], 'time': t}
    # -1의 의미는 에러 발생 / 0 : 정상종료
    return -1


def find_dict(key, d):
    start = time.time()
    try:
        value = d[key]
        t = (time.time() - start) * 1000
        return {'key': key, 'value': value, 'time': t}

    except:
        return -1


def find_dict_byValue(value, d):
    start = time.time()
    for k, v in d.items():
        if v == value:
            t = (time.time() - start) * 1000
            return {'key': k, 'value': value, 'time': t}

    return -1


def time_test(n, key):
    NUM_DATA = n
    KEY = key
    li = create_data(NUM_DATA)
    d = create_dict(li)
    t_li = find_list(KEY, li)
    t_d = find_dict(KEY, d)
    t_d_byValue = find_dict_byValue(KEY, d)

    return {'list': t_li, 'dict': t_d, 'dict_byValue': t_d_byValue}


if __name__ == '__main__':
    num = 5

    print('[10개 탐색 시]')
    r = time_test(10, num)
    print(f'리스트 탐색: {r["list"]}')
    print(f'딕셔너리 탐색: {r["dict"]}')
    print(f'딕셔너리 value 탐색: {r["dict_byValue"]}')
    print()

    print('[10^2개 탐색 시]')
    r = time_test(100, num)
    print(f'리스트 탐색: {r["list"]}')
    print(f'딕셔너리 탐색: {r["dict"]}')
    print(f'딕셔너리 value 탐색: {r["dict_byValue"]}')
    print()

    print('[10^3개 탐색 시]')
    r = time_test(1000, num)
    print(f'리스트 탐색: {r["list"]}')
    print(f'딕셔너리 탐색: {r["dict"]}')
    print(f'딕셔너리 value 탐색: {r["dict_byValue"]}')
    print()

    print('[10^4개 탐색 시]')
    r = time_test(10000, num)
    print(f'리스트 탐색: {r["list"]}')
    print(f'딕셔너리 탐색: {r["dict"]}')
    print(f'딕셔너리 value 탐색: {r["dict_byValue"]}')
    print()

    print('[10^6개 탐색 시')
    r = time_test(1000000, num)
    print(f'리스트 탐색: {r["list"]}')
    print(f'딕셔너리 탐색: {r["dict"]}')
    print(f'딕셔너리 value 탐색: {r["dict_byValue"]}')
    print()

    print('[10^7개 탐색 시')
    r = time_test(10000000, num)
    print(f'리스트 탐색: {r["list"]}')
    print(f'딕셔너리 탐색: {r["dict"]}')
    print(f'딕셔너리 value 탐색: {r["dict_byValue"]}')

"""
결과
1. 10000개 미만에서 탐색 시 list dict의 탐색 속도 차이는 없다
2. 10000개 이상에서는 dict의 탐색속도가 list보다 빠르다
    (dict는 hash table을 이용해서 배열 전체를 탐색하지 않고 value를 얻기 때문)
3. dict 탐색 시 key를 탐색하나 value를 탐색하나 속도 차이는 없다
"""