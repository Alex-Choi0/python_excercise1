import random

random_number = random.randint(1, 100)

print(random_number)

count = 0
check = False

# while loop를 사용

while check == False :
  answer = int(input("enter number : "))
  if answer > random_number :
    print("해당 입력값은 정답보다 큽니다.")
    count += 1
  elif answer < random_number :
    print("해당 입력값은 정답보다 작습니다.")
    count += 1
  else :
    print("정답입니다.")
    break



print("finish")
print("입력 횟수 : ", count)



