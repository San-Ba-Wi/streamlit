import streamlit as st
from variables_config import A

if A[2] == 1:
    audio_file = open('Oort Cloud.mp3', 'rb')
    audio_bytes = audio_file.read()
    
    st.audio(audio_bytes, format='audio/mp3')
    
    st.divider()
    
    answer = st.radio(
        '이 노래는 무슨 노래일까요?',
        ('정답을 선택해주세요', '오르트구름', '좋은날', '낙하','노래 이름 뭐하지','이재학','노래 이름 뭐하지22')
    )
    if answer == '오르트구름':
        st.write(':blue[쩡답]입니다!')
        st.write(':green[왼쪽의 페이지에서 다음 문제로 넘어가주세요!]')
        st.image('correct!.webp')
        A[3] = 1
    elif answer == '정답을 선택해주세요':
        st.write()
        st.image('thinking.jpg')
        A[3] = 0
    elif answer == '이재학':
        st.write(':red[하지만 그것은 틀렸습니다!]')
        st.image('https://blog.kakaocdn.net/dn/oWyNM/btrnkxpnCM4/Dt0q7ZdclokjMdEGdrEPT1/img.jpg')
        A[3] = 0
    else:
        st.write(':red[하지만 그것은 틀렸습니다!]')
        st.image('tryagain.jpg')
        A[3] = 0
else:
    st.title(':red[앞의 문제를 먼저 풀어주세요!]')
