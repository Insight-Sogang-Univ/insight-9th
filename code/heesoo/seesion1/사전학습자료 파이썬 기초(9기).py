#!/usr/bin/env python
# coding: utf-8

# # 파이썬 기초 사전자료

# **과제는 중간중간 별표로 표시된 부분을 스스로 채워서 코드 작성한 뒤 제출하시면 됩니다.**

# ## Python Programming

# ### 변수와 자료형

# **변수**
# * 데이터를 특정 이름을 붙여 저장함
# * 연산을 쉽게 처리하거나, 큰 데이터를 한번에 불러올 수 있음
# * 여러 형태의 데이터를 하나 이상의 변수로 선언 가능
# * Python에서 변수명을 한글로 선언 가능

# **자료형**
# * 데이터 자료형을 규명하는 것은 프로그래밍에 있어서 가장 기본적이고 중요함
# * 파이썬에서는 데이터의 자료형을 변수 선언 시, 자동으로 지정
# * 자료형에 따라 분석의 기법이 달라질 수 있음
# * 기본적으로 3가지 자료형이 가장 많이 사용됨
#   - 정수형 int: 양의 정수, 음의 정수, 0
#   - 실수형 float: 정수를 포함한 실수, 0.n 형태로 출력
#   - 문자형 str: 영어나 기호, 또는 숫자로 구성된 문자

# In[1]:


#파이썬에서 등호 (=) 기호는 '같다'를 의미하는 것이 아닌, '선언한다'라는 의미가 있음

a = 10
print(a)         # print(): 데이터나 변수를 출력
print(type(a))   # type(): 데이터의 타입을 확인


# In[2]:


b = 'B'
print(b)
print(type(b))


# In[3]:


num = 23.1
print(num)
print(type(num))


# In[4]:


a = 10
b = 'B'
a + b   #자료형이 일치하지 않으면 오류 발생


# In[5]:


#Jupyter Notebook의 경우, print함수를 사용하지 않고 변수명만 입력해도 데이터 출력 가능

a = float(10)   #자료형을 임의로 바꾸려면, 데이터 앞에 타입을 입력하여 변수 선언
type(a)


# -----

# ### 문자열 자료형 (String)

# * 프로그래밍 뿐만 아니라, 데이터 분석에 있어서 문자를 처리하는 것이 중요
# * 문자열: 문자, 단어 등으로 구성된 문자들의 집합 ex. "단어" / "A" / "123"
# * 문자열에는 모두 큰따옴표(") 또는 작은따옴표(')를 이용해 선언
# * 여러 줄의 문자열을 대입할 경우 큰따옴표 또는 작은 따옴표 세 개를 사용
# * 문자열을 여러 형태로 연산이 가능함
# * 인덱싱(indexing)과 슬라이싱(Slicing) 기능이 많이 사용됨
#   - Indexing: 특정 위치의 문자를 추출
#   - Slicing: 특정 위치의 문자를 잘라냄

# #### String

# In[6]:


#문자를 그대로 작성하면 오류가 발생

안녕하세요


# In[7]:


#따옴표를 활용하여 문자형을 문자열 자료형으로 사용할 수 있음

"안녕하세요"


# In[8]:


#여러 문장을 사용할 경우

"""
여러문장의 경우
따옴표를 세 개를 사용해 주면 됩니다.
감사합니다.
"""


# In[9]:


#문자열도 변수로 저장 가능

a = "안녕하세요"
b = """저는 문자형 입니다.
반갑습니다"""

print(a)
print(b)
type(a), type(b)


# In[10]:


#연산자를 활용해 문자열 연산 가능 (덧셈, 곱셈)

str1 = "인사이트"
str2 = "에 오신 여러분을 환영합니다."

str1 + str2


# In[11]:


str3 = "감사합니다"

str3 * 3


# In[12]:


#len(): 해당 문자열의 길이를 구하는 함수 (데이터의 길이나 크기를 구할 떄도 사용)

str4 = "이 문자열의 길이는 len함수를 이용해 구할 수 있습니다."

len(str4)


# #### String Indexing
# * Indexing: 특정 위치의 글자 추출
# * 대괄호를 이용해 추출하며, 0부터 순서가 매겨짐
# * 뒷부분부터 셀 땐, 음수를 붙여 세어줄 수 있음
# * 실무에서 복잡한 문자데이터를 다룰 때 (설문, 제품명, 항목명 등) 주로 사용

# In[13]:


str5 = "너의 삶은 짧지만, 계속 구하면 가치있는 것을 찾으리라"

str5[0]


# In[14]:


str5[14]


# In[15]:


str5[-2]


# In[16]:


str5[0] + str5[14] + str5[-2]


# In[17]:


str6 = str5[0] + str5[14] + str5[-2]
print(type(str6))
str6


# #### String Slicing
# * Slicing: 특정 글자를 잘라서 추출
# * str[n:m] : str 변수의 문자열에서, n번째 부터, m번째 글자 전까지 추출
# * str[:m] : 맨 처음부터 m 번째 글자 전 까지 추출
# * str[n:] : n 번째 글자부터 맨 끝 글자 까지 추출
# * 처음번호와 끝 번호를 생략하면 모든 문자열이 출력

# In[18]:


str5 = "발자국마다 이어진 별자리 그 서투른 걸음이 새겨놓은 밑그림"

str5[0:3]


# In[19]:


str5[:13]


# In[20]:


str5[16:]


# In[21]:


str5[:13] + str5[16:]


# In[22]:


str7 = "2021파이썬기초"
day = str7[:4]
lesson = str7[4:]

print(day)
print(lesson)


# #### String Function
# * count() : 특정 문자의 개수를 출력
# * find() / index() : 특정 문자가 어디에 위치해 있는지 출력 (index 함수의 경우, 해당 문자가 없으면 오류 발생) 
# * join() : 문자열에 특수기호나 특정 문자를 삽입
# * upper() / lower() : 영어 소문자를 대문자로 변경 (upper) / 영어 대문자를 소문자로 변경 (lower)
# * lstrip() / rstrip() / strip() : 문자열 좌,우 또는 전체 공백을 제거
# * replace() : 특정 문자를 다른 문자로 변환
# * split() : 문자를 공백 기준으로 리스트의 형태로 나누어 출력 (쌍반점(:) 기호 사용 시, 전체 문자열이 리스트에 하나의 객체로 출력) 

# In[23]:


#count

str8 = "Insight Python Data Analyze"
str8.count('a')


# In[24]:


#find

str8.find("D")


# In[25]:


#index

str8.index("D")


# In[26]:


#join

",".join('가나다라마')


# In[27]:


#upper

str8.upper()


# In[28]:


#lower

str8.lower()


# In[29]:


#lstrip

str9 = "    Python     "
str9.lstrip()


# In[30]:


#rstrip

str9.rstrip()


# In[31]:


#strip

str9.strip()


# In[32]:


#replace

str10 = "python Big 데이터"
str10.replace('데이터', 'data')


# In[33]:


#split

str10.split()


# In[34]:


str10.split(":")


# #### 과제 1~2

# 1. 어떤 회원이 생년월일 입력란에 890724를 입력하였을 때, 해당 문자를 연/월/일로 각각 나누어 출력하기

# In[10]:


str12='890724'

year = str12[:2]
month = str12[2:4]
day = str12[4:]

print("{}/{}/{}".format(year, month, day))


# 2. 어떤 고객이 휴대전화번호를 010-1234-5678으로 입력하였을 때, 해당 문자를 01012345678으로 출력하기

# In[9]:


str11="010-1234-5678"
str11[0:3]+str11[4:8]+str11[9:]


# -----

# ### 리스트 (List)

# * 리스트 (list) : 여러 개의 데이터 다룰 때, 하나의 변수에 많은 값을 집어 넣을 수 있음
# * 대괄호를 이용하여, 데이터를 묶어 줌 ex) a = [1,2,3,4,5] #5개의 데이터가 a라는 변수에 모두 담겨있음
# * C 언어의 배열(array)과 유사한 List 를 이용
# * 서로 다른 데이터 타입의 값들도 하나의 List에 넣을 수 있음
# * 리스트 내 데이터 간 순서가 존재
# * 리스트 내 데이터를 삭제하거나 추가, 수정이 가능함
# * 리스트 내 데이터를 삭제하거나 추가, 수정이 가능함
#     - append() : 추가
#     - insert() : 삽입
#     - remove() : 삭제
# * Size가 정해져 있지 않고 유동성 있음

# In[35]:


list1 = [100, 200, 300, 400, 500]
list1


# In[36]:


type(list1)


# In[37]:


#문자열도 리스트로 선언이 가능

list2 = ['서울', 70, 170, '강남']
list2


# In[38]:


type(list2)


# In[39]:


#리스트에서 특정 값을 추출 (Indexing)

list1[0]


# In[40]:


list1[1], list1[2], list1[3]


# In[41]:


sub = ['국어', '영어', '수학', '과학']
sub


# In[42]:


#append(): 리스트에 해당 값을 추가

sub.append('사회')
sub


# In[43]:


#insert(): 리스트 특정위치에 해당 값을 추가

sub.insert(0, '한국사')
sub


# In[44]:


#remove(): 특정 값을 리스트에서 삭제

sub.remove('수학')
sub


# In[45]:


score = [10, 20, 30, 40]
score


# In[46]:


#리스트 간 연산 가능

score * 3


# In[47]:


score + sub


# -----

# ### 튜플 (Tuple)
# * 튜플 (tuple) : 리스트와 같이 여러 개의 데이터를 집어넣을 수 있는 공간
# * 소괄호를 이용하여, 데이터를 묶어 줌 ex) c = (1,2,3,4,5) #5개의 데이터가 c라는 변수에 모두 담겨있음
# * 튜플 내 데이터 간 순서가 존재
# * 한번 선언된 튜플은 변경이 불가능 함
# * Packing과 Unpacking을 활용하여, 데이터를 추출하거나 튜플을 생성할 수 있음
#     - Packing : 여러 개의 데이터를 쉼표(,) 구분자를 이용해, 하나의 변수로 생성
#     - Unpacking : 하나의 튜플을 여러 개의 변수로 선언하여, 변수에 각 데이터를 선언
# * 함수와 반복문 같이 중요한 하이퍼파라미터(Hyper Parameter)들을 보호 할 때 사용 (하이퍼파라미터 : 수식 내 값이 변하지 않는 인자나 상수)

# In[48]:


#소괄호를 이용해 튜플 생성 가능

t1 = (1, 2, 3, 4, 5)
print(type(t1))
t1


# In[49]:


#튜플은 한 번 선언되면 변경이 불가능

t1.append("A")


# In[50]:


t1.remove(3)


# In[51]:


#그러나 각 데이터를 하나의 튜플로부터 추출 가능

t2 = (1, 2, '삼', 4, 5)
t2[2]


# In[52]:


#Packing: 각각의 데이터를 하나의 변수로 선언할 때, 해당 변수들을 하나의 튜플로 선언 가능

pack1 = 1,2,3,4,5,6
type(pack1)


# In[53]:


pack1


# In[54]:


#Unpacking: 하나의 튜플 내 데이터를 각각의 변수로 선언 가능

a,b,c,d,e,f = pack1
type(a)


# In[55]:


a


# In[56]:


a + b + c + d + e + f


# In[57]:


#Indexing과 Slicing은 가능

a = (10,20,30,40,50)
a[0]


# In[58]:


a[-1]


# In[59]:


a[2:]


# In[60]:


#기본 연산자를 이용한 연산 가능

b = (1, 2, 3, 4)
c = (5, 6, 7, 8)
c + b


# In[61]:


c * 2


# -----

# ### 세트 (Set)

# * 세트 (Set) : 리스트와 같이 여러 개의 데이터를 집합의 형태로 집어넣을 수 있는 공간
# * 중괄호를 이용하여, 데이터를 묶어 줌  ex) c = {1,2,3,4,5} #5개의 데이터가 c라는 변수에 모두 담겨있음
# * 집합 내 데이터 간 순서 없음, 중복을 허용하지 않음
# * 집합 내 데이터 변경이 가능
# * 집합연산이 가능 (Van Diagram의 개념)

# In[62]:


#중복된 값은 스스로 제외하고 출력

A = {10,20,30,40,10}
print(A)
print(type(A))


# In[63]:


B = {10,10,10,10,10,10}
print(B)


# In[64]:


#괄호 내부에 있는 list를 set 형태로 선언

S = set([1,2,3,4,5,6])
print(S)
print(type(S))


# In[65]:


C = {10,20,30,40,50}
D = {40,50,60,70}

#교집합 연산
print(C&D)

#합집합 연산
print(C|D)

#차집합 연산: C 집합에서 D 집합의 원소를 뺸 나머지
print(C-D)

#대상 차집합 연산: 교집합을 제외한 나머지 원소 출력
print(C^D)


# * A.intersection(B) : A와 B의 교집합을 연산 (A&B와 같은 결과) 
# * A.union(B) : A와 B의 합집합을 연산 (A|B와 같은 결과) 
# * A.difference(B) : A와 B의 차집합을 연산 (A-B와 같은 결과) 
# * A.add(n) : A의 Set에 n이라는 값을 추가
# * A.update([n1,n2,n3]) : A의 Set에 [n1,n2,n3]의 여러 값을 추가

# In[66]:


print(C.intersection(D))
print(C.union(D))
print(C.difference(D))


# In[67]:


C.add(100)
C


# In[68]:


C.update([1,2,3,4,5])
C


# -----

# ### 딕셔너리 (Dictionary)

# * 딕셔너리 (Dictionary) : 데이터를 Key와 Value의 Pair 형태로 하나의 변수에 선언
# * 중괄호를 이용하여, key-value Pair 형태로 묶어줌  
#     ex) d = {“name” : “Kim”, “value” : 100 } -> Kim이라는 데이터가 name이라는 키값과 쌍을 이룸. 100이라는 데이터가 value라는 키값과 쌍을 이룸. 
# * 매우 많이 사용되는 데이터 자료형 중 하나
# * 데이터를 구조적으로 다룰 수 있음
# * Key 값은 중복 되지 않음
# * 이후, Pandas 라이브러리의 Series 와 비슷한 개념

# In[69]:


D = {'A':100, 'B':200, 'C':300}
print(D)
print(type(D))


# In[27]:


dict1 = {"이름":"제니", "전공":"경영", "학번":17}
dict1


# In[28]:


#D['Key']: D라는 딕셔너리의 Key값에 해당하는 Value값을 출력

dict1['이름']


# In[29]:


#D.get('Key'): D라는 딕셔너리의 Key값에 해당하는 Value값을 출력

dict1.get('전공')


# In[30]:


#D.keys() : D라는 딕셔너리의 Key값을 모두 가져옴

dict1.keys()


# In[31]:


#D.value() : D라는 딕셔너리의 Value 값을 모두 가져옴

dict1.values()


# In[32]:


#딕셔너리의 Value값도 List 형태로 넣을 수 있음

dict1['이름'] = ['로제', '리사']
dict1['전공'] = ['경영학', '수학']
dict1['학번'] = [16, 19]
dict1


# In[33]:


#딕셔너리와 리스트를 이용하여, 해당 Key 값에 Value를 계속 추가해 줄 수 있음

names = ["제니"]
majors = ['경영']
classes = [17]

dict3 = {"이름": names, '전공':majors, "학번": classes}
dict3


# In[34]:


names.append('지수')
majors.append('경영학')
classes.append(19)


# In[35]:


dict3 = {"이름": names, '전공':majors, "학번": classes}
dict3


# #### 과제 3

# 3. 간단한 영한 사전 만들기 -> 1부터 10까지 영어를 입력하면 한글로 출력되는 프로그램
# 
#   (input 함수를 이용해서 값을 입력 받을 수 있음, Key-Value Pair를 이용해 프로그램 제작)

# In[ ]:


dic= {'one':'하나', 'two':'둘', 'three':'셋', 'four':'넷', 'five':'다섯', 'six':'여섯', 'seven':'일곱', 'eight':'여덟', 'nine':'아홉', 'ten':'열'}
a= input('1부터 10까지 영어를 입력하세요=')

print(dic.get(a))


# -----

# ### 기본 연산자

# * 산술 연산자
#   - 연산의 우선순위 존재 : 거듭제곱 -> 곱셈 및 나눗셈 -> 나머지 및 몫 -> 덧셈 뺄셈 연산 (연산의 순위가 같을 경우, 왼쪽에서 오른쪽으로 연산 진행)
# 
# * 비교 연산자
#   - 두 개의 연속형 데이터를 비교
#   - 명제가 맞는 경우 True, 틀린 경우 False의 Bool 형태 결과를 출력 (Boolean : 참 또는 거짓을 나타내는 자료형)
#   - Boolean의 경우 조건문에서 많이 사용
# 
# * 논리 연산자 
#   - And / Or / Not : ~이고, 그리고 / ~이거나, 또는 / ~이 아니다

# In[79]:


a = 100
b = 35


# In[80]:


#쉼표를 이용해, 여러 개의 결과를 동시에 출력 가능

a+b, a-b


# In[81]:


a*b, a/b


# In[82]:


a//b, a%b


# In[83]:


a = 50
b = 67

a>b, a<b


# In[84]:


a>=b, a<=b


# In[85]:


a==b


# In[86]:


a!=b


# In[87]:


#결과에 대한 자료형을 type() 기능을 이용해 파악 가능

type(a!=b)


# #### 과제 4~5

# 4. 값을 입력 받아 원의 넓이를 구하는 프로그램 만들기 
# 
#  * input 함수를 이용해서 값을 입력 받을 수 있음, 입력 받은 변수를 활용해 계산식 세우기
#  * 원 넓이 구하는 공식 : y = π x r² (π= 3.14 로 계산))

# In[3]:


a= float(input('반지름 길이를 입력하세요:'))
y= 3.14*a*a
print(y)


# 5. 금액을 입력했을 때, 상품 가격에 따른 잔돈을 반환하는 자판기 프로그램 만들기
#     - 금액과 상품가격은 input함수로 선언
#     - 잔돈은 500,100,50,10원 단위로 반환
#     - 잔돈은 가장 큰 금액부터 반환 예) 잔돈 760원 : 500원1개, 100원2개, 50원 1개, 10원 1개

# In[5]:


a= int(input('금액을 입력하세요:'))
b= int(input('가격을 입력하세요:'))
c= a-b
q= c//500
w=(c-500*q)//100
e=(c-500*q-100*w)//50
r=(c-500*q-100*w-50*e)//10
print("잔돈 {}원: 500원{}개, 100원{}개, 50원{}개, 10원{}개".format(c,q,w,e,r))


# -----

# ##  Statement & Function

# ### 조건문 (if)

# * 조건문 : 특정 상황에 대한 판단 또는 해당 조건에 대한 실행여부 결정
# * If문을 사용하여 구현함
# * 들여쓰기를 이용해, 해당 조건에 대한 수행문의 종속을 표현
# * 주로 비교 연산자와 함께 사용됨
# * 특히 데이터 전처리를 할 때, apply 함수와 함께 매우 많이 사용됨

# In[88]:


#if 조건문을 이용한 연속형 변수 비교

A = 100
B = 200

if A>B:
    print("Hi")
else:
    print("안녕하세요")


# In[89]:


#입력 함수를 이용하여 숫자를 비교하는 프로그램

C = int(input("첫번째 정수를 입력하세요 : "))
D = int(input("두번째 정수를 입력하세요 : "))

if C>D:
    print("첫번째 정수 ",C,"가 더 큽니다.")
else :
    print("두번째 정수 ",D,"가 더 큽니다.")

if C==D:
    print("첫번째 정수와 두번째 정수가 같습니다.")
else:
    print("첫번째 정수와 두번째 정수가 다릅니다.")


# - 여러 가지 조건을 동시에 판별할 땐, elif 구문을 이용
# - elif문은 개수의 제한 없이 사용 가능
# - 특정 조건에 수행할 문장을 사용하지 않을 땐, Pass 구문을 이용

# In[90]:


#if문을 이용한 성적처리 프로그램

score = int(input("성적을 입력하세요! : "))

if score >= 95:
    print("학생의 성적은 A+입니다.")
elif score >= 90:
    print("학생의 성적은 A입니다.")
elif score >=80 :
    print("학생의 성적은 B입니다.")
elif score >=70 :
    print("학생의 성적은 C입니다.")
else:
    print("학생의 성적은 F입니다.")


# In[91]:


#Pass 구문의 사용

A,B = 100, 20

if A>B:
    pass
else:
    print("Error")


# #### 과제 6

# 6. 값을 입력 받아 홀수인지 짝수인지 판별하는 프로그램 만들기

# In[7]:


a= int(input('값을 입력하세요:'))

if a%2 == 0 : print('짝수')
else : print('홀수')


# -----

# ### 반복문 (While, For)

# * 반복문 : 특정 수식이나 기능을 반복 수행할 때 사용
# * 특정 조건이 맞을 때, 계속 반복되는 구조
# * 들여쓰기를 이용해, 반복 조건에 대한 수행문의 종속을 표현
# * 주로 수학연산에서 사용
# * 데이터 전처리를 할 때, 문자열 처리에서 많이 사용됨
# 
# 

# #### While문

# In[92]:


i = 0 

while i <5:
    print("Hi Python~!")
    i = i+1

print("반복종료")


# In[93]:


#While문은 일반적으로 특정 조건만 만족되면 수행문이 반복되기 때문에
#중간에 수행문을 멈출 조건을 걸어줘야 함

i=1
while i>0:
    print("Hello")
    i = i+1
    
    if i>3 :
        print("강제 탈출")
        break             #break문을 이용하면, 바로 While문을 나올 수 있음.

print("반복종료")


# #### for문

# In[94]:


#For문은 기본적으로 range( ) 함수와 같이 사용이 됨

for i in range(1,10):  # range(0,n+1) : 0부터 n까지의 범위를 부여한다.
    print(i)


# In[95]:


#여러 가지 자료형을 이용한 For 문

list1 = ['a','b','c','d']
for i in list1:
    print(i)


# In[96]:


a = [(1,2),(3,4),(5,6)]
for (n1,n2) in a:
    print(n1+n2)


# In[97]:


# for문과 if문을 같이 사용한 경우 (자동업무 구현에 많이 사용)

score = [100,23,30,76,34,50]
num=0

for i in score:
    num = num+1
    if i>60:
        print("합격입니다.")
    else:
        print("불합격입니다.")


# In[98]:


# 1부터 n까지 더하는 프로그램

sum = 0

for i in range(1,101):
    sum=sum+i

print(sum)


# #### 과제 7~8

# 7. For 반복문을 중첩하여, 아래와 같이 * 기호를 피라미드로 출력하는 프로그램 제작

# In[8]:


for i in range(1,6):
    print('*'*i)


# 8. For문과 If문을 이용하여, 아래의 리스트의 최댓값을 구하는 프로그램 제작
# 
#     list = [1,24,3,44,1000,2,0,74] / 결과 : 1000

# In[15]:


list = [1,24,3,44,1000,2,0,74]
best_score = 0
for score in list:
    if score > best_score:
        best_score = score
        
print(f"결과: {best_score}")


# -----

# ### 함수
# * 함수 : 입력 X 값에 대한 결과 Y값을 반환(Return)하는 기능을 하나의 묶음으로 선언
# * Input X 와 Output Y
# * 반복적으로 사용되는 특별한 기능을 함수로 선언
# * 여러 함수들의 집합을 ‘모듈(module)’이라고 부름
# * 복잡한 데이터를 전처리할 때, 특정 기능을 반복적으로 구현하고 싶을 때 사용
# 
# 

# In[99]:


#함수는 코드가 진행될 때, 함수 이름이 언급되지 않으면 실행 되지 않음
#입력 받은 수의 합을 구하는 함수

def sum(num): 
    for i in range(1,num+1): 
        sum = num*(num+1)/2 
    return sum

num = int(input('정수를 입력하시오 : ')) 
sum(num)


# In[100]:


#한번 선언된 함수는 다른 코드 입력 창에서 입력을 해도 사용 가능

def circle_area(r):
    return (r**2)*(3.14)


# In[101]:


data = 1000
circle_area(data)


# In[102]:


# 두 개의 입력 값을 받아 하나의 결과 값을 출력

def cylinder_volume(r,h):
    return (r**2)*(3.14)*h

num1 = 1000
num2 = 2000

cylinder_volume(num1,num2)


# In[103]:


#하나의 값을 입력해 여러 개의 결과 값을 출력

def timetable(data):
    list1 = [data * 1, data * 2, data * 3]
    return list1[0], list1[1], list1[2]

timetable(5)


# In[54]:


# 날짜 데이터를 함수를 이용해 처리

def datetime(date):
    date = str(date)
    result1 = date[0:4]+"-"+date[4:6]+"-"+date[6:]
    return result1

datetime(20210301)


# #### 과제 9

# 9. 입력하는 모든 수의 평균을 계산하는 함수 만들기

# In[3]:


a = int(input= '숫자를 입력하세요: '))

def means(*args):
    a = 0
    for i in args:
        a= a + i
    return a

print('a/count(a)')
    #입력 개수에 상관없이 사용하기 위해, 함수 입력 값 자리에 *args를 사용


print(means(1, 5, 6, 7, 222))


# -----

# ### 라이브러리 (Numpy & Pandas)

# * 모듈 : 여러 함수들을 모아놓은 집합
# * 라이브러리 : 특정 기능을 지원하는 모듈 및 함수를 모아놓은 집합
# * 기능에 따라 여러 가지 라이브러리가 존재 (시각화, 웹 서비스, 데이터 분석, 머신러닝, 등…) 
# * 필요에 따라 라이브러리를 직접 만들기도 함
# * Anaconda를 설치하면, 데이터 분석에 필요한 기본 라이브러리들이 포함되어 설치됨
# * 데이터 분석에서 기초적으로 Numpy 와 Pandas 를 많이 사용

# #### Numpy

# - Numpy : Numeric + Python의 약자 , 수학 및 과학 연산 라이브러리
# - 배열이나 행렬계산에 필요한 함수 제공
# - 수열 데이터를 다룰 때 용이, 이후에 Pandas에서 DataFrame 형태로 사용
# - 다차원 배열(Array)를 다룰 때 주로 사용 (인공신경망, 비정형 데이터 처리, 자연어 처리 등)

# In[20]:


#Numpy 라이브러리 호출하여, np라는 약자로 사용
#Numpy 내에 함수를 사용할 때, 반드시 np라는 문자를 붙임

import numpy as np


# In[21]:


#에러 발생 - 리스트의 경우 통계연산이 불가능 

data = [6,5,7,3,4,2]
data.mean() 


# In[22]:


#다차원 배열(ndarray)의 경우 통계를 포함한 모든 수학적 연산 지원

arr = np.array(data) 
arr.mean()  


# In[23]:


#리스트와 배열의 데이터 타입

print(type(data))
print(type(arr))


# In[24]:


#배열 내부에는 여러 형태의 데이터 타입이 올 수 있음
#변수 선언 시 자동으로 데이터 타입 결정

arr1 = np.array([1,2,3,4,5])
arr1.dtype


# In[25]:


arr2 = np.array([1.1, 2.3, 3.4, 4.5, 5.3])
arr2.dtype


# In[26]:


arr3 = np.array(['A', 'B', 'C', 'D', 'E'])
arr4 = np.array(['제니', '로제', '지수', '리사'])
print(arr3)
print(arr4)
print(arr3.dtype)
print(arr4.dtype)


# In[112]:


#이중 리스트를 이용해 행렬(Matrix)을 구현 가능
# 3X3 행렬의 구현

data = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix = np.array(data)
print(type(matrix))
matrix


# In[113]:


# 행렬간 사칙연산

matrix = np.array([[1,2],[2,3],[19,30]])
matrix


# In[114]:


matrix_2 = np.array([[3,4],[5,6],[3,5]])
matrix_2


# In[115]:


print(matrix * matrix_2)
print("---------------")
print(matrix - matrix_2)


# In[116]:


#행렬의 제곱연산

matrix **2


# In[117]:


#shape: 행렬의 구조 출력, n개의 행의 m개의 열로 구성된 행렬은 (n,m)으로 출력

arr_b = np.array([[1,2,],[2,3]])
arr_b.shape


# * np.arange(n) : 0부터 n까지의 값을 가지는 배열 생성
# * np.arange(n,m) : n부터 m-1 까지 값을 갖는 배열 생성 
# * np.arrange(n,m,k) : n부터 m-1 까지 k씩 증가시켜 배열 생성 
# * np.random.randn(n) : 평균이 0이고 표준편차가 1인 n개의 데이터를 무작위로 생성
# * np.random.randn(n,m) : 평균이 0이고 표준편차가 1인 n개의 데이터를 nxm 행렬의 형태로 생성

# In[118]:


# arange함수를 이용한 데이터 자동 생성

arr5 = np.arange(10)
arr5


# In[119]:


arr6 = np.arange(1,10,2)
arr6


# In[120]:


#Random data 생성

arr7 = np.random.randn(10)
arr7


# In[121]:


arr8 = np.random.randn(10,5)
arr8


# In[122]:


#np.astype( ) : 현재 array내 데이터를 원하는 형태의 데이터 타입으로 변경

arr = np.array([1,2,3,4,5])
print("before ",arr.dtype)

arr = arr.astype(np.float)
print("After ",arr.dtype)
arr


# In[123]:


# 2차원 array에서 Indexing

arr_1 = np. array([[1,2,5],[4,5,9],[6,7,34]])
arr_1


# In[124]:


arr_1[0,0]


# In[125]:


arr_1[2,1]


# In[126]:


arr_1[:,0]


# In[127]:


arr_1[0,:]


# In[128]:


#행 또는 열 형태로 출력

arr_1[0:2, :]


# In[129]:


arr_1[:, 0:2]


# In[130]:


arr_1[:,:]


# In[131]:


# 전체 데이터 shape 변환하기

print(arr_1)
print("------------")
print(arr_1.reshape(1,9))


# In[132]:


#값 초기화하기

arr_z = np.zeros((2,2))
arr_z


# In[133]:


arr_x = np.zeros(10)
arr_x


# In[134]:


arr_c = np.ones(10)
arr_c


# In[135]:


#배열 합 구하기 (전체합, 행 방향 합, 열 방향 합)

arr1 = np.arange(1,11).reshape(5,2)
arr1


# In[136]:


arr1.sum()  #전체합


# In[137]:


arr1.sum(axis=1) #행 방향합


# In[138]:


arr1.sum(axis=0)


# #### Pandas

# * Pandas : 데이터 과학에 사용되는 라이브러리로 데이터 불러오기, 전처리, 통계 분석에 사용
# * Numpy 기반으로 작성된 라이브러리
# * Series 형태와 DataFrame 형태 존재 
# * 실무에서 접하는 엑셀 파일이 DataFrame 형태
# * 데이터 분석에 있어서 필수적인 라이브러리
# * 데이터 전처리에 대부분은 Pandas로 이루어 짐
# 
# ⇒ 교육세션 시간에 더 자세히 살펴볼 예정

# In[2]:


#Pandas 라이브러리를 호출하여, pd라는 약자로 사용

import pandas as pd


# In[3]:


#Series의 기본적인 구조: 값(Value)과 순서(Index)로 구성

s1 = pd.Series([1,2,56,77,93])
s1


# In[4]:


s1.values


# In[5]:


s1.index


# In[7]:


#Series는 통계적 연산 가능

s1.mean()


# In[8]:


#여러 가지 Python 데이터 타입으로 Series 생성 가능

s2 = pd.Series(['제니','로제','지수','리사'], name ='출석부', 
               index=['일','이','삼','사'])
s2


# In[9]:


myDict = {'name':"Jenny","age":27,"gender":"female","job":"singer"}
person = pd.Series(myDict, name="Person")
person


# In[10]:


#Series도 [ ] 기호를 이용해 Indexing 가능

person[0]


# In[11]:


person['job']


# In[12]:


person[:]


# In[13]:


#비교 연산자를 이용해, 특정 데이터의 존재 여부를 알 수 있음

person == 'female'


# In[14]:


person[person == 'female']


# In[15]:


#describe(): 다양한 통계량 요약, 데이터 파악 시 굉장히 많이 사용

obj = pd.Series([2,3,7,8], index=['d','a','b','c'])
obj.describe()


# In[16]:


#sort_values로 series의 값 정렬 가능

obj.sort_values()   #내림차순 정렬 시 ascending=False 설정


# In[17]:


#sort_index로 series의 순서(인덱스) 정렬 가능

obj.sort_index()


# In[18]:


#value_counts로 series의 unique한 값의 수 집계

obj.value_counts()


# #### 과제 10~11

# 10. (5,2)의 random한 Matrix를 생성하고,
# Matrix의 전체합, 전체 평균, 각 열의 합, 각행의 합, 각 열의 평균, 각 행의 평균을 계산하기

# In[5]:


import numpy as np
a= np.random.randn(5.2)
print('전체합:', a.sum())
print('각 행의 합',a.sum(axis=1))
print('각 열의 합', a.sum(axis=0))
print('각 행의 평균', np.mean(a.sum(axis=1)))
print('각 열의 평균', np.mean(a.sum(axis=0)))


# 11. Series를 이용하여, 아래와 같은 성적표를 만들기
#  - 1) 각 과목의 합격/불합격 여부 출력하기 (50점 이상 , 합격)
#  - 2) 과목의 전체평균을 계산하여, 70점 기준으로 합격 불합격 여부 판별하기
#  
# 

# In[4]:


import pandas as pd

#1
grade = {'국어':70,"영어":30,"수학":80,"과학":90}


if int(grade['국어']) >= 50:
    print ('국어:합격')
    else: print ('국어:불합격')
if '영어' >= 50:
    print '합격'
    else print '불합격'
if '수학' >= 50:
    print '합격'
if '과학' >= 50:
    print '합격'


# In[14]:


#2
grade = {'국어':70,"영어":30,"수학":80,"과학":90}
avg=('국어'+'영어'+'수학'+'과학')/4
if 0<=국어<=100 and 0<=영어<=100 and 0<=수학<=100 and 0<=과학<=100:
    if avg>= 70:
        print('합격')
    else:
        print('불합격')
else:
    print('오류')


# In[ ]:




