import streamlit as st

audio_file = open('Cant Hold Us.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')

st.divider()

answer = st.radio(
    '이 노래는 무슨 노래일까요?',
    ('정답을 선택해주세요', '강남스타일', 'ETA', 'Can\'t Hold Us','Waiting for Love','이재학','We Are')
)
if answer == 'Can\'t Hold Us':
    st.write(':blue[쩡답]입니다!')
    st.write(':green[왼쪽의 페이지에서 다음 문제로 넘어가주세요!]')
    st.image('correct!.webp')
elif answer == '정답을 선택해주세요':
    st.write()
    st.image('thinking.jpg')
elif answer == '이재학':
    st.write(':red[하지만 그것은 틀렸습니다!]')
    st.image('https://blog.kakaocdn.net/dn/oWyNM/btrnkxpnCM4/Dt0q7ZdclokjMdEGdrEPT1/img.jpg')
else:
    st.write(':red[하지만 그것은 틀렸습니다!]')
    st.image('tryagain.jpg')
