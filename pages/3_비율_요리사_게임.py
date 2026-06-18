import streamlit as st
import math

# 페이지 설정
st.set_page_config(page_title="황금 비율 요리사 | 비와 비율", layout="wide")

# 제목
st.title("🌟 도전! 최고의 황금 비율 요리사")
st.markdown("---")

# 소개
st.write(
    "너만의 초콜릿 우유 레시피를 만들어보세요! 🍫🥤 "
    "초콜릿 파우더와 물의 양을 조절하며 가장 맛있는 비율을 찾아보세요!"
)

st.markdown("---")

# 학생 제어 영역
st.subheader("📝 나만의 레시피 만들기")

col1, col2 = st.columns(2)

with col1:
    chocolate = st.slider(
        "🍫 초콜릿 파우더 (숟가락)",
        min_value=1,
        max_value=10,
        value=5,
        step=1,
        help="초콜릿 파우더의 양을 선택하세요 (1-10 숟가락)"
    )

with col2:
    water = st.slider(
        "🥤 물 (컵)",
        min_value=1,
        max_value=10,
        value=5,
        step=1,
        help="물의 양을 선택하세요 (1-10 컵)"
    )

st.markdown("---")

# 색상 계산 함수
def calculate_color(chocolate, water):
    """
    초콜릿과 물의 비율에 따라 색상 계산
    초콜릿이 많으면 진한 갈색, 물이 많으면 연한 갈색
    """
    # 비율 계산 (0 ~ 1 범위로 정규화)
    ratio = chocolate / (chocolate + water)
    
    # RGB 값 계산
    # 연한 갈색 (물이 많을 때): RGB(210, 180, 140)
    # 진한 갈색 (초콜릿이 많을 때): RGB(101, 67, 33)
    
    r = int(210 - (210 - 101) * ratio)
    g = int(180 - (180 - 67) * ratio)
    b = int(140 - (140 - 33) * ratio)
    
    return f"rgb({r}, {g}, {b})"


# 실시간 시각화 - 컵
st.subheader("🥛 나의 초콜릿 우유")

color = calculate_color(chocolate, water)

# 컵 시각화 - 간단한 디자인
cup_html = f"""<div style="display: flex; justify-content: center; margin: 40px 0;"><div style="width: 200px; height: 200px; background: {color}; border: 3px solid #8B4513; border-radius: 0 0 20px 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.2);"></div></div>"""

st.markdown(cup_html, unsafe_allow_html=True)

st.markdown("---")

# 레시피 카드 영역
st.subheader("📋 나의 레시피 카드")

# 1단계
with st.container():
    col_num, col_content = st.columns([0.3, 0.7])
    with col_num:
        st.markdown("#### 1단계")
    with col_content:
        st.write("**준비한다**")
        st.write("컵 하나를 준비하고 물을 붓는다!")

st.divider()

# 2단계
with st.container():
    col_num, col_content = st.columns([0.3, 0.7])
    with col_num:
        st.markdown("#### 2단계")
    with col_content:
        st.write("**초콜릿을 넣는다**")
        st.write(f"초콜릿 파우더를 **{chocolate}번** 넣는다!")
        st.info(f"📊 비율 체크: 초콜릿 : 물 = {chocolate} 대 {water}")

st.divider()

# 3단계
with st.container():
    col_num, col_content = st.columns([0.3, 0.7])
    with col_num:
        st.markdown("#### 3단계")
    with col_content:
        st.write("**완성!**")
        st.write("잘 섞어서 맛있게 마신다!")

st.markdown("---")

# 저장 버튼
if st.button("💾 레시피 카드 저장하기", use_container_width=True):
    st.success("✅ 레시피가 저장되었습니다!")
    
    saved_info = f"""
    **나의 초콜릿 우유 레시피**
    
    1단계. 준비한다
    - 컵 하나를 준비하고 물을 붓는다!
    
    2단계. 초콜릿을 넣는다
    - 초콜릿 파우더를 {chocolate}번 넣는다!
    - 비율: 초콜릿 : 물 = {chocolate} : {water}
    
    3단계. 완성!
    - 잘 섞어서 맛있게 마신다!
    """
    
    st.info(saved_info)

st.markdown("---")

# 추가 정보
with st.expander("💡 팁: 황금 비율 찾기"):
    st.write("""
    - **1:9** - 연한 우유 맛 🤍
    - **5:5** - 중간 정도의 초콜릿 맛 💜
    - **9:1** - 진한 초콜릿 맛 🤎
    
    여러 비율을 시도해보고 가장 마음에 드는 맛을 찾아보세요!
    """)
