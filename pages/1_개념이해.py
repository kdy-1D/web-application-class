import streamlit as st

# 페이지 설정
st.set_page_config(page_title="개념 이해 | 비와 비율", layout="wide")

# ============================================
# 제목 및 개념 설명
# ============================================
st.title("🌐 Part 1. 개념 이해 — 비(比)란 무엇일까요?")

st.markdown("---")
st.subheader("📚 비(比)의 의미")
st.write(
    """
    비(比)는 **두 가지 양을 비교**하는 방법입니다.
    
    ✨ **핵심 개념:**
    - **`:` 기호**는 두 수를 연결합니다
    - **오른쪽 수 (기준량)**: 기준이 되는 '⚓' 같은 역할 — 안정적인 기준점
    - **왼쪽 수 (비교하는 양)**: 기준과 비교하는 '🎭' 같은 역할 — 주인공
    
    💡 **예시**: 잼과 빵의 비 `3 : 5` → "빵 5개에 잼 3개를 발라요" (빵이 기준)
    """
)

st.markdown("---")

# ============================================
# Step 1: 재료 선택 (Ingredient Selection)
# ============================================
st.subheader("🎯 Step 1. 재료 선택")
st.write("학습할 상황을 선택해주세요!")

ingredient_options = {
    "🍓 Jam & 🍞 Bread": {
        "left_emoji": "🍓",
        "left_name": "잼",
        "right_emoji": "🍞",
        "right_name": "빵",
    },
    "⚽ Goals & 👟 Matches": {
        "left_emoji": "⚽",
        "left_name": "골",
        "right_emoji": "👟",
        "right_name": "경기",
    },
    "🍫 Chocolate Powder & 🥤 Water": {
        "left_emoji": "🍫",
        "left_name": "초코파우더",
        "right_emoji": "🥤",
        "right_name": "물",
    },
    "🍎 Apple & 🍊 Orange": {
        "left_emoji": "🍎",
        "left_name": "사과",
        "right_emoji": "🍊",
        "right_name": "오렌지",
    },
    "📚 Pages & ⏰ Minutes": {
        "left_emoji": "📚",
        "left_name": "쪽수",
        "right_emoji": "⏰",
        "right_name": "분",
    },
    "🍌 Bananas & 🍓 Strawberries": {
        "left_emoji": "🍌",
        "left_name": "바나나",
        "right_emoji": "🍓",
        "right_name": "딸기",
    },
    "🥕 Carrots & 🥗 Salad": {
        "left_emoji": "🥕",
        "left_name": "당근",
        "right_emoji": "🥗",
        "right_name": "샐러드",
    },
}

selected_scenario = st.selectbox(
    "시나리오를 선택하세요:",
    options=list(ingredient_options.keys()),
    index=0,
)

# 선택된 재료 정보 추출
ingredient_info = ingredient_options[selected_scenario]
left_emoji = ingredient_info["left_emoji"]
left_name = ingredient_info["left_name"]
right_emoji = ingredient_info["right_emoji"]
right_name = ingredient_info["right_name"]

st.markdown("---")

# ============================================
# Step 2: 슬라이더로 비 조절 (Ratio Sliders)
# ============================================
st.subheader("🎚️ Step 2. 슬라이더로 비를 조절해보세요!")

col1, col2 = st.columns(2)

with col1:
    comparison_amount = st.slider(
        f"{left_emoji} {left_name} (비교하는 양)",
        min_value=1,
        max_value=10,
        value=3,
        help=f"{left_name}의 개수를 선택하세요",
    )

with col2:
    standard_amount = st.slider(
        f"{right_emoji} {right_name} (기준량)",
        min_value=1,
        max_value=10,
        value=5,
        help=f"{right_name}의 개수를 선택하세요",
    )

st.markdown("---")

# ============================================
# Step 3: 시각적 표현 (Visual Ratio Display)
# ============================================
st.subheader("👁️ Step 3. 시각적 표현")

ratio_text = f"{left_emoji} {left_name} {comparison_amount}개  :  {right_emoji} {right_name} {standard_amount}개"
st.markdown(f"**비 시각화:** {ratio_text}")

col_left, col_center, col_right = st.columns([4, 1, 4])

with col_left:
    st.markdown(f"### {left_emoji} {left_name}")
    for row in range((comparison_amount + 9) // 10):
        count = min(10, comparison_amount - row * 10)
        st.markdown("&nbsp;".join([left_emoji] * count), unsafe_allow_html=True)

with col_center:
    st.markdown("<div style='font-size: 40px; text-align: center;'>:</div>", unsafe_allow_html=True)

with col_right:
    st.markdown(f"### {right_emoji} {right_name}")
    for row in range((standard_amount + 9) // 10):
        count = min(10, standard_amount - row * 10)
        st.markdown("&nbsp;".join([right_emoji] * count), unsafe_allow_html=True)

st.markdown("---")

# ============================================
# Step 4: 비의 4가지 표현 방식
# ============================================
st.subheader("📖 Step 4. 비의 4가지 읽는 방법")

st.write("**현재 설정된 비:**")
st.markdown(f"## `{comparison_amount} : {standard_amount}`")

st.write("")  # 간격

col1, col2 = st.columns(2)

with col1:
    st.write(
        f"""
        **1️⃣ {comparison_amount} 대 {standard_amount}**
        - 가장 기본적인 읽기 방법입니다.
        
        **2️⃣ {comparison_amount}과 {standard_amount}의 비**
        - 두 양의 관계를 나타냅니다.
        """
    )

with col2:
    st.write(
        f"""
        **3️⃣ {standard_amount}에 대한 {comparison_amount}의 비** (기준 강조)
        - 기준량({standard_amount})을 먼저 명시합니다.
        - "{right_name} {standard_amount}개에 {left_name} {comparison_amount}개"
        
        **4️⃣ {comparison_amount}의 {standard_amount}에 대한 비** (비교 강조)
        - 비교량({comparison_amount})을 먼저 명시합니다.
        - "{left_name} {comparison_amount}개는 {right_name} {standard_amount}개에 대한 비"
        """
    )

st.markdown("---")

# ============================================
# 팁 및 격려
# ============================================
st.info(
    "💡 **팁**: 슬라이더를 움직여 다양한 비를 만들어보세요! "
    "재료를 바꾸고 비의 표현이 어떻게 달라지는지 관찰해봅시다."
)

