import streamlit as st
st.title("소수 개수 찾기")
data = 1
num = st.number_input(
    label='양의 정수를 입력해주세요.',
    value=1,
    step=1
)

A = []  # 초기값을 포함한 리스트
B = []  # 소수만 출력될 리스트

button = st.button("소수 찾기")
if button:
    # 2부터 입력값까지 리스트 생성
    for i in range(2, num + 1):
        A.append(i)
    
    # 에라토스테네스의 체 원리를 사용하여 걸러진 수를 문자열 "removed"로 변경
    for i in range(0, len(A)):
         if type(A[i]) == int:
            for j in range(i + 1, len(A)):
                if type(A[j]) == int:
                     if A[j] % A[i] == 0:
                         A[j] = "removed"
    
    
    for i in range(0, len(A)):
         if type(A[i]) == int:
             B.append(A[i])
    
    st.write(f'{len(B)}개의 소수가 있습니다.')
    st.write(f'{B}')
    
    if len(B) >= 1000:
        st.write("이정도는 좀 힘든걸..?")
