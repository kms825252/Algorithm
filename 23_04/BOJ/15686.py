n = int(input())

car_input = []
car_output = []
for _ in range(n):
    car_input.append(input())
for _ in range(n):
    car_output.append(input())

def check(car_output, car_input):
    car_check = True
    for i in range(len(car_output)):
        if car_output[i] != car_input[i]:
            car_check = False
            break
    return car_check

for i in range(len(car_output)-1, -1, -1):
    if check(car_output[i], car_input[i]):