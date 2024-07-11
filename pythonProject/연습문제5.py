# i = 0
# while i < 100 :
#     i = i+1
# if i%2 == 1 :
#



#1.
i = 1
#result 하는 역할 : 연산 결과 값을 저장
result = 0
while i <100 :
    i = i + 1

#2. 반복되는 수가 홀수인지를 확인
if i % 2 == 1 :

#3. 홀수라면 그 값을 저장
    result.append(i)

#4. 저장된 값을의 합을 구함
print(sum(result))