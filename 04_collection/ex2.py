# 리스트 심화

# ===========================================================
#  리스트에서 제공하는 메소드
# ===========================================================

langs = ["c", "c++", "java", "python"]

langs.append("umlang")                   # 끝에 추가
print(langs)

langs.insert(2,"c#")                # 인덱스 2에 "c#" 추가
print(langs)

langs[3] = "javascript"             # 인덱스 3을 "javascript"로 변경
print(langs)

langs.remove("c++")                  # "c++" 삭제 (첫번째 데이터만 삭제)
print(langs)

langs.pop(1)
print(langs)

langs.pop()
print()                          # 인덱스 생략 시 마지막 항목 삭제

print(langs.index("python"))        # "python" 인덱스 찾기

langs.reverse()                      # 리스트 순서를 거꾸로 뒤집기
print(langs)

langs.sort()                         # 오름차순 정렬
print(langs)

langs.sort(reverse=True)             # 내림차순 정렬
print(langs)

#                        # 모든 item 삭제
# print(langs)

# 리스트 복사
ori = [1, 2, 3]
res = ori.copy()
res[0] = 2
print(ori,res)

# 얕은 복사(shallow copy) vs 깊은 복사(deep copy)
ori = [[1, 2], [3, 4]]
res = ori.copy()
res[0].append(10)
print(ori,res)


# 깊은 복사를 하려면?
import copy
res = copy.deepcopy(ori)
print(id(ori[0]),id(res[1]))


# ===========================================================
#  그 외
# ===========================================================

# 중첩리스트
nested_list = [1, ["a", ["x", "y"], "b"], 2]

print(nested_list[1][1][0])         # x 출력하기
print(nested_list[1][2])            # b 출력하기
print(nested_list[2])               # 2 출력하기

# 리스트 언패킹
nums = [1,2,3,4]

print(*nums)
a,b,c,d = nums
print(a,b,c,d)

n2 = [5,6]
print(nums+n2)

print([*nums,*n2])

# zip함수: 반복 가능(iterable)한 여러 객체를 인자로 받아
# 동일한 인덱스에 있는 원소들끼리 튜플로 묶어주는 파이썬 내장 함수
subjects = ["국어", "수학", "영어"]
scores = [80, 90, 95]
print(list(zip(subjects,scores)))





# ===========================================================
#  List Comprehension
#  for문을 이용하여 각 원소에 식을 적용하여 리스트를 만드는 방법
# ===========================================================

# 1 ~ 10의 제곱수 리스트 만들기
l = [i**2 for i in range(1,11)]
print(l)

# 1 ~ 10 중 짝수의 제곱수로 된 리스트 만들기 (필터링 if문 추가)

l = [i**2 for i in range(1,11) if not i&1]
print(l)

# 1 ~ 10 중 짝수면 "짝", 홀수면 "홀" 출력하기

l = ['Odd' if i&1 else 'Even' for i in range(1,11)]
print(*l)

# 각 이름의 길이로 이루어진 리스트 만들기
names = ['marinette','adrien','alya','nino']
l = [len(s) for s in names]
print(l)

# 길이가 5 이상인 이름만 뽑기

l = [s for s in names if len(s)>=5]
print(l)

# 중첩 for문도 가능
l = [x*y for x in range(3) for y in range(4)]
print(l)

# =========================================================
#  🔥 실습 문제
# =========================================================

# 1️⃣ 60점 이상인 점수만 뽑기
scores = [85, 42, 73, 55, 90, 68, 35, 100]

result = [i for i in scores if i>=60]
print(result)                       # ✅ [85, 73, 90, 68, 100] 출력


# 2️⃣ 60점 이상인 경우 "합격", 60점 미만은 "불합격"으로 처리
result = ['Pass' if i >= 60 else "Not Pass" for i in scores]
print(result)                       # ✅ ['합격', '불합격', '합격', '불합격', '합격', '합격', '불합격', '합격']


# 3️⃣ 1 ~ 100 중 3 또는 5의 배수의 합 구하기 (sum() 함수 이용)
result = sum([i for i in range(1,101) if not i%3 or not i%5])
print(result)                       # ✅ 2418 출력


# 4️⃣ n을 포함하고 있는 단어만 뽑기
words = ["apple", "banana", "kiwi", "mango"]

result = [s for s in words if 'n' in s]  
result = [s for s in words if s.find('n')^-1]  
print(result)                       # ✅ ['banana', 'mango'] 출력


# 5️⃣ 세 학생의 3과목 점수표에서 과목별 평균 구하기
scores = [
     [90, 80, 70],       # 학생 1
     [100, 90, 80],      # 학생 2
     [80, 70, 60],       # 학생 3
]

result = [sum (s) / len(s) for s in zip(*scores)]
print(result)                       # ✅ [90.0, 80.0, 70.0]

print(round(0.5))
print(round(1.5))
print(round(2.5))
print(round(3.5))