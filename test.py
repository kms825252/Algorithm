# whiteBall_x, whiteBall_y : 흰 공의 X, Y 좌표를 나타내기 위해 사용한 변수
whiteBall_x = balls[0][0]
whiteBall_y = balls[0][1]

# targetBall_x, targetBall_y : 목적구의 X, Y 좌표 나타내는 변수
targetBall_x = balls[1][0]
targetBall_y = balls[1][1]

# width, height : 목적구와 흰 공의 X 좌표 간의 거리, Y 좌표 간의 거리
width = abs(targetBall_x - whiteBall_x)
height = abs(targetBall_y - whiteBall_y)

# radian : width 와 height 를 두 변으로 하는 직각삼각형의 각도를 구한 결과
# - lradian = 180 / PI (도)
# - 1도 = PI / 180 (radian)
# angle : 아크탄젠트로 얻은 각도 radian 을 degree 로 환산한 결과
radian = math.atan(width / height) if height > 0 else 0
angle = 0

# 목적구가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력
if whiteBall_x == targetBall_x:
    if whiteBall_y < targetBall_y:
        angle = 0
    else:
        angle = 180
elif whiteBall_y == targetBall_y:
    if whiteBall_x < targetBall_x:
        angle = 90
    else:
        angle = 270


# 목적구가 흰 공을 중심으로 1사분면에 위치했을 때 각도를 재계산
if whiteBall_x < targetBall_x and whiteBall_y < targetBall_y:
    radian = math.atan(height / width)
    angle = 90 - (180 / math.pi * radian)

# 목적구가 흰 공을 중심으로 2사분면에 위치했을 때 각도를 재계산
elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
    radian = math.atan(width / height)
    angle = (180 / math.pi * radian) + 270
# 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
elif whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
    radian = math.atan(width / height)
    angle = 270 - (180 / math.pi * radian)

# 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
    radian = math.atan(height / width)
    angle = (180 / math.pi * radian) + 90

# distance : 두 점(좌표) 사이의 거리를 계산
distance = math.sqrt(width**2 + height**2)

# power : 거리 distance 에 따른 힘의 세기를 계산
power = distance * 0.5

# 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
# 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 함.





# 흰 공을 기준으로 사분면으로 나눈 뒤, 그에 합당한 hole 정하기
목적구 = x2, y2
흰공 = x1, y1



# 거리에 따라 각도와 세기를 조절해야 함


# 파울 피하기
# 상대방 공 혹은 검은 공이 흰 공과 목적구 사이에 위치한다면 다른 목적구를 찾는 방법 사용
# 이미 다른 목적구를 넣은 상태라면 흰 공과 목적구 사이의 벽을 쳐서 목적구 맞추도록 구현

# 파울 유도 코드