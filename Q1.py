import streamlit as st
from variable_config import ANSWERS

audio_file = open('school-music.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')

st.divider()

answer = st.radio(
    '이 노래는 무슨 노래일까요?',
    ('정답을 선택해주세요','Hype Boy', '대구고등학교 교가', '바람기억')
)
if answer == '대구고등학교 교가':
    st.write(':blue[쩡답]입니다!')
    ANSWERS[0] = 1
    st.write(':green[왼쪽의 페이지에서 다음 문제로 넘어가주세요!]')
    st.image('correct!.webp')
elif answer == '정답을 선택해주세요':
    st.write()
    ANSWERS[0] = 0
    st.image('thinking.jpg')
else:
    st.write(':red[하지만 그것은 틀렸습니다!]')
    ANSWERS[0] = 0
    st.image('tryagain.jpg')

font_dirs = [os.getcwd() + '/customFonts']
font_files = fm.findSystemFonts(fontpaths=font_dirs)

for font_file in font_files:
    fm.fontManager.addfont(font_file)
fm._load_fontmanager(try_read_cache=False)
