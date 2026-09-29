# 함수 2

# ===========================================================
# 1. 지역변수와 전역변수
# ===========================================================
# 함수 안에서 만든 변수는 지역변수로, 함수 밖에서는 사용할 수 없다.
# 함수 밖에서 선언된 변수는 전역변수이며, 함수 안에서는 기본적으로
# "읽기"만 가능하고, 값을 바꾸려면 global 키워드가 필요하다.
a=1

def f():
    global a
    a=10
    print(a)
f()
print(a)


# ===========================================================
#  2. 함수 인자 전달 방식
# ===========================================================
# 1) call-by-value: 값 자체가 복사되어 전달, 원본과 별도의 메모리 공간을 할당, 함수 내부에서 수정 시 원본 불변
# 2) call-by-reference: 변수의 주소가 전달, 원본과 같은 메모리 공간을 가리킴, 함수 내부에서 수정 시 원본 변경
# 3) call-by-assignment: 파이썬은 객체를 가리키는 참조 전달, 원본과 같은 객체를 가리킴(재할당 전까지)
#                        immutable 객체인 경우 call-by-value처럼 동작 -> 함수 내부에서 수정 시 원본 불변
#                        mutable 객체인 경우 call-by-reference처럼 동작 -> 함수 내부에서 수정 시 원본 변경
#                        mutable 객체라도 재할당을 하면 원본과 연결이 끊기고 새로운 객체 할당

def swap(a,b):
    a,b=b,a
    print(id(a),id(b))
    print(a,b)
a,b=1,2
print(id(a),id(b))
swap(a,b)
print(a,b)

def append_item(num):
    num.append(2)

num = [1]
append_item(num)
print(num)

def swap2(num):
    num[0],num[1]=num[1],num[0]
swap2(num)
print(num)

def ass(num):
    num = [10]
    print(num)
ass(num)
print(num)
# ===========================================================
# 3. 재귀함수
# ===========================================================

# 팩토리얼 계산하기 (1, 1, 2, 6, 24, ..)
def f2(a):
    return 1 if not a else a*f2(a-1)
#print(f2(10))


# 피보나치 계산하기 (0, 1, 1, 2, 3, 5, 8, ..)

def f3(a):
    return a if a<2 else f3(a-1)+f3(a-2)
#print(f3(10))
#print([f3(i) for i in range(11)])

# ===========================================================
# 4. 람다함수
# ===========================================================

# 람다함수 : 이름 없는(익명) 한 줄짜리 함수를 만듦
# lambda a, b, ...: 표현식



students = [
    {"name": "뽀로로", "score": 85},
    {"name": "크롱", "score": 92},
    {"name": "포비", "score": 78},
]
# Name lexicographic order sort
print(sorted(students, key=lambda s: s["name"]))
print(sorted(students, key=lambda s: s["score"]))

# =========================================================
#  🔥 실습 문제
# =========================================================

# 1️⃣ n이 짝수면 True, 홀수면 False를 반환하는 함수 작성하기

def is_even(n):
    return bool(~n&1)


print(is_even(4))                           # ✅ True
print(is_even(7))                           # ✅ False


# 2️⃣ 가변 인자로 여러 숫자를 받아 (최소값, 최대값, 합계, 평균) 튜플 리턴하기

def num_info(*args):
    mx=max(args)
    mn=min(args)
    s=sum(args)
    avg=s/len(list(args))
    return mx,mn,s,avg


print(num_info(4, 8, 1, 9, 3))              # ✅ (1, 9, 25, 5.0)


# 3️⃣ 이름과 키워드 가변 인자로 받은 정보로 아래와 같이 문자열을 만들어 리턴하기

def introduce(name,**kwargs):
    ans=name
    for k,v in kwargs.items():
        ans+=f" / {k}: {v}"
    return ans


print(introduce("카리나", age=26, team="에스파", hometown="수원"))
# ✅ 카리나 / age: 26 / team: 에스파 / hometown: 수원

print(introduce("장원영", age=22, team="아이브", bloodtype="O형"))
# ✅ 장원영 / age: 22 / team: 아이브 / bloodtype: O형

print(introduce("성현", age=17, team="코르티스"))
# ✅ 성현 / age: 17 / team: 코르티스


# 4️⃣ 5부터 카운트다운하여 로켓 발사시키기 (재귀함수)
# time.sleep(1)                     # 1초 동안 stop

import time
def countdown(n):
    if not n:
        print('로켓발사')
        return
    print(f"{n} ->",end=' ',flush=True)
    time.sleep(1)
    countdown(n-1)



countdown(5)                        # ✅ 5 -> 4 -> 3 -> 2 -> 1 -> 로켓 발사