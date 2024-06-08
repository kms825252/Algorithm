import sys
points = sys.stdin.readlines()[1:]
'''
readlines로 읽은 것들은 ^Z가 나오기 전까지 list로 저장됨. 컴퓨터마다 다름.
^Z 또는 ^D의 역할은 raising End Of File.

따라서 미리 코드를 실행시켜볼 땐 ctrl+Z 또는 D를 통해 EOF를 일으켜줘야함. 어차피 채점할땐 알아서 eof을 읽어주므로 상관없음. 
'''
points.sort(key=lambda y:int(y.split()[1]))
'''
key option은 단일인자를 받는 함수를 기준으로 정렬한다는 소리

예를 들어서 다음과 같은 문자열로 된 리스트가 있다고 하자. list = ['aa', 'a']
이걸 길이가 짧은 것부터 나열하고 싶다면 key option에 len 함수를 지정하면 된다. 즉
list.sort(key=len) 이러면 'a', 'aa' 가 됨.

lambda a, b : a+b 하면 인자 두 개를 받아서 더한다는 소리임.
그래서 위 문장 중 key option의 뜻은 다음과 같다.

 points라는 list에 있는 애들 하나하나 받아올건데, 그놈을 y라고 하면, y를 일단 공백을 기준으로 쪼개서 리스트로 저장한 다음 1번째에 있는 애를 가져다가 정수로 바꿈. (이때 개행문자는 무시됨.)
 예를 들어서, points 리스트가 ['1 2\n', ... ...] 일때 첫번째놈 '1 2\n' 를 받아오고, 얘를 쪼개서 ['1', '2\n']로 만들고, 1번째에 있는 '2\n'를 int에 대입함. 그러면 intger 2가 됨.
그리고 해당 option을 기준으로 오름차순 정렬을 시작하는 것임.

(정렬 옵션은 key, reverse 두 개가 있고, reverse는 boolean algebra를 인수로 받음. 따라서 내림차순으로 하고 싶으면 false넣으셈)

'''
points.sort(key=lambda x : int(x.split()[0]))

'''
tuple의 lexicographic order는 우선순위가 former coordinate에 있음. 
(2,1), (2,2), (1,2), (1,1) 있으면
먼저 (2,1), (1,1), (2,2), (1,2) 
그 다음에 (1,1), (1,2), (2,1), (2,2)

만약 반대로 하면
먼저 (1,2), (1,1), (2,1), (2,2)
그 다음에 (1,1), (2,1), (1,2), (2,2)
y-coordinate에 가중한 lexicographic order가 됨.

만약 tuple의 갯수가 m개라면

points.sort(key=lambda x : int(x.split()[m-1]))
points.sort(key=lambda x : int(x.split()[m-2]))
.
.
.
points.sort(key=lambda x : int(x.split()[1]))
points.sort(key=lambda x : int(x.split()[0]))
하면 된다.
'''

'''
현재 list로 저장된 points들은 정렬이 됐지만 'n m\n' 꼴임.
모두 string이고, 개행문자가 이미 붙어있으므로 join을 통해 바로 원하는 형태 출력 가능함.
예를 들어서 현재 points가 다음 리스트와 같다면 
['1 2\n', '3 5\n']
join을 통해서
['1 2\n3 5\n']가 됨
이는 출력시
1 2(개행)
3 5(개행)

로 나옴

'''
print(''.join(points))

'''

참고 : qkralsrms99님의 38524496제출답안 참고.
많은 도움 됐습니다.'''