import streamlit as st
st.title('석리송의 웹앱!!!')
st.write('안녕하세요!!!')

import streamlit as st
from datetime import datetime
import random

# 페이지 설정
st.set_page_config(
    page_title="석리송의 웹앱",
    page_icon="🔥",
    layout="wide"
)

# CSS 꾸미기
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
}

.big-title {
    font-size: 60px;
    font-weight: 900;
    text-align: center;
    color: #ffffff;
    text-shadow: 3px 3px 10px rgba(0,0,0,0.4);
}

.sub-title {
    text-align: center;
    font-size: 22px;
    color: #eeeeee;
}

.card {
    background-color: rgba(255,255,255,0.12);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(8px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
}

.stButton>button {
    width: 100%;
    border-radius: 12px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
    background: linear-gradient(90deg, #ff9966, #ff5e62);
    color: white;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# 헤더
st.markdown("<div class='big-title'>🔥 석리송의 초간지 웹앱 🔥</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>세상에서 제일 멋진 Streamlit 앱 😎</div>", unsafe_allow_html=True)

st.write("")
st.write("")

# 컬럼 배치
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.header("🎉 환영합니다!")

    name = st.text_input("이름을 입력하세요", placeholder="예: 석리송")

    if name:
        st.success(f"{name}님 반갑습니다 😎")

    mood = st.selectbox(
        "오늘 기분은 어떤가요?",
        ["😁 최고!", "😴 피곤함", "🔥 열정폭발", "🥲 살려줘"]
    )

    st.write(f"현재 상태: **{mood}**")

    if st.button("✨ 운세 보기"):
        fortunes = [
            "오늘은 대박나는 날!",
            "맛있는 걸 먹게 됩니다 🍗",
            "코딩이 술술 풀립니다 💻",
            "행운이 찾아옵니다 🍀",
            "집중력이 MAX 찍습니다 ⚡"
        ]
        st.balloons()
        st.info(random.choice(fortunes))

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.header("⏰ 현재 시간")

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.metric("현재 시각", now)

    st.write("---")

    st.header("📊 오늘의 랜덤 점수")

    score = random.randint(50, 100)
    st.progress(score)

    st.metric("행운 수치", f"{score}%")

    st.markdown("</div>", unsafe_allow_html=True)

st.write("")
st.write("")

# 하단
st.markdown("""
---
<center>
<h3>💎 Made by 석리송 💎</h3>
<p>Streamlit으로 만든 간지폭발 웹앱</p>
</center>
""", unsafe_allow_html=True)
