import streamlit as st

st.set_page_config(page_title="신나는 비와 비율 학습", layout="wide")

# Main title and subtitle
st.title("🎯 신나는 수학 탐험: [6학년 1학기] 4. 비와 비율")
st.markdown("#### 스마트한 학습 공간 — 비의 개념을 차근차근 즐겁게 익혀봐요!")

# Curriculum achievement standard
st.info(
    "[6수02-02] 두 양의 크기를 비교하는 상황을 통해 비의 개념을 이해하고, 두 양의 관계를 비로 나타낼 수 있다."
)

# Introductory storytelling
st.markdown("---")
st.subheader("왜 `:` 기호를 사용할까요?")
st.write(
    "스포츠 경기 점수나 부엌 레시피처럼 두 가지 양을 비교할 때 `:` 기호를 사용합니다.\n"
    "예를 들어 축구 점수 3:1, 잼과 빵의 비율 1:4 처럼요. 함께 그 쓰임을 찾아볼까요?"
)

# Introduce the 3 pages / parts
st.markdown("---")
st.header("학습 구성 — 3개의 탐험 페이지")
cols = st.columns([1, 1, 1])

with cols[0]:
    st.subheader("🌐 Part 1. 개념 이해")
    st.write("- 슬라이더로 빵과 잼의 양을 조절하며 비를 쓰고 읽는 4가지 표현을 실시간으로 확인해요.")
    st.markdown('**핵심 목표:** 비의 표현 방법(":"), 분수, 나누기, 비율문장')

with cols[1]:
    st.subheader("📝 Part 2. 연습 문제")
    st.write("- 스포츠 경기, 요리 상황과 같은 실생활 문장제 문제를 풀어봅니다. 힌트와 시각적 단서를 통해 이해를 돕습니다.")
    st.markdown("**핵심 목표:** 상황해석 → 비 설정 → 계산과 표현 연습")

with cols[2]:
    st.subheader("🎮 Part 3. 황금 비율 요리사 게임")
    st.write("- 초코파우더와 물처럼 재료를 자유롭게 조절해 나만의 레시피를 만들어보는 창의 활동이에요. 정답은 없답니다!")
    st.markdown("**핵심 목표:** 비의 직관적 이해와 창의적 적용")

st.markdown("---")

# Short walkthrough / how to use
st.subheader("학습 방법 안내")
st.write(
    "왼쪽 사이드바 메뉴를 이용해 원하는 단계를 선택하여 학습을 시작해보세요!\n"
    "- `개념 이해`에서 슬라이더를 움직여 비의 표현을 관찰하고,\n"
    "- `연습 문제`에서 실생활 문제로 이해도를 확인하고,\n"
    "- `황금 비율 요리사 게임`에서 자유롭게 재료를 조합해 보세요."
)

st.caption("Tip: 모르는 내용이 있으면 힌트 버튼을 눌러보세요 — 힌트는 단계별로 친절히 도와줍니다.")

# Footer - encouragement
st.markdown("---")
st.write("**즐거운 학습 되세요! 필요한 기능이 있다면 선생님께 알려주세요. 🙂**) ")
