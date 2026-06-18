import streamlit as st

# 페이지 설정
st.set_page_config(page_title="연습 문제 | 비와 비율", layout="wide")

# 문제 목록 정의
problem_groups = {
    "쉬운 문제": {
        "남학생과 여학생": {
            "type": "multiple_choice",
            "question": "남학생이 6명, 여학생이 3명입니다. 남학생 수 : 여학생 수의 비는?",
            "options": ["① 6:3", "② 3:6", "③ 9:3"],
            "correct_answer": "① 6:3",
        },
        "빨간색 공과 파란색 공": {
            "type": "multiple_choice",
            "question": "빨간색 공이 4개, 파란색 공이 2개입니다. 빨간색 공 : 파란색 공의 비는?",
            "options": ["① 4:2", "② 2:4", "③ 6:2"],
            "correct_answer": "① 4:2",
        },
        "초콜릿과 마시멜로우": {
            "type": "multiple_choice",
            "question": "초콜릿이 5개, 마시멜로우가 2개입니다. 초콜릿 : 마시멜로우의 비는?",
            "options": ["① 5:2", "② 2:5", "③ 7:2"],
            "correct_answer": "① 5:2",
        },
        "딸기와 포도": {
            "type": "multiple_choice",
            "question": "딸기가 8개, 포도가 4개입니다. 딸기 : 포도의 비는?",
            "options": ["① 8:4", "② 4:8", "③ 12:4"],
            "correct_answer": "① 8:4",
        },
        "연필과 지우개": {
            "type": "multiple_choice",
            "question": "연필이 3자루, 지우개가 1개입니다. 연필 : 지우개의 비는?",
            "options": ["① 3:1", "② 1:3", "③ 4:1"],
            "correct_answer": "① 3:1",
        },
    },
    "중간 문제": {
        "초콜릿과 우유": {
            "type": "text_input",
            "question": "초콜릿 4개와 우유 7잔을 비교해요. 우유를 기준으로 초콜릿의 비를 쓰세요.",
            "comparison_label": "초콜릿",
            "standard_label": "우유",
            "comparison": 4,
            "standard": 7,
        },
        "바구니 감자와 당근": {
            "type": "text_input",
            "question": "감자 8개와 당근 2개가 있어요. 당근을 기준으로 감자의 비를 쓰세요.",
            "comparison_label": "감자",
            "standard_label": "당근",
            "comparison": 8,
            "standard": 2,
        },
        "자동차와 자전거": {
            "type": "text_input",
            "question": "주차장에 자동차 12대와 자전거 4대가 있어요. 자전거를 기준으로 자동차의 비를 쓰세요.",
            "comparison_label": "자동차",
            "standard_label": "자전거",
            "comparison": 12,
            "standard": 4,
        },
        "주스와 물": {
            "type": "text_input",
            "question": "주스 3병과 물 5병이 있어요. 물을 기준으로 주스의 비를 쓰세요.",
            "comparison_label": "주스",
            "standard_label": "물",
            "comparison": 3,
            "standard": 5,
        },
        "과일과 야채": {
            "type": "text_input",
            "question": "사과 6개와 당근 3개를 비교해요. 당근을 기준으로 사과의 비를 쓰세요.",
            "comparison_label": "사과",
            "standard_label": "당근",
            "comparison": 6,
            "standard": 3,
        },
    },
    "어려운 문제": {
        "축구와 농구": {
            "type": "fill_blank",
            "context": "학생 9명 중 3명이 축구를 좋아하고 6명이 농구를 좋아해요.",
            "question": "()에 대한 ()의 비를 쓰세요.",
            "first_blank": "농구",
            "second_blank": "축구",
            "comparison": 3,
            "standard": 6,
        },
        "케이크와 크림": {
            "type": "fill_blank",
            "context": "케이크 2개에 크림 5컵을 사용했어요.",
            "question": "()에 대한 ()의 비를 쓰세요.",
            "first_blank": "케이크",
            "second_blank": "크림",
            "comparison": 5,
            "standard": 2,
        },
        "사과와 바나나": {
            "type": "fill_blank",
            "context": "사과 5개와 바나나 3개가 있어요.",
            "question": "()에 대한 ()의 비를 쓰세요.",
            "first_blank": "바나나",
            "second_blank": "사과",
            "comparison": 5,
            "standard": 3,
        },
        "의자와 책상": {
            "type": "fill_blank",
            "context": "책상 4개에 의자 8개가 있어요.",
            "question": "()에 대한 ()의 비를 쓰세요.",
            "first_blank": "의자",
            "second_blank": "책상",
            "comparison": 4,
            "standard": 8,
        },
        "물감과 붓": {
            "type": "fill_blank",
            "context": "물감 6통과 붓 2자루를 비교해요.",
            "question": "()에 대한 ()의 비를 쓰세요.",
            "first_blank": "붓",
            "second_blank": "물감",
            "comparison": 6,
            "standard": 2,
        },
    },
}

# 제목
st.title("📝 Part 2. 연습 문제 — 비와 비율 문제 풀기")
st.markdown("---")

# 난이도 선택
difficulty = st.radio("난이도를 선택하세요:", options=list(problem_groups.keys()))
selected_group = problem_groups[difficulty]

# 문제 선택
selected_problem = st.selectbox("문제를 선택하세요:", options=list(selected_group.keys()))
problem = selected_group[selected_problem]

# 선택 문제 내용 보기
st.subheader("문제")
if problem.get("type") == "fill_blank":
    st.write(problem["context"])
    st.write(f"**{problem['question']}**")
else:
    st.write(problem["question"])

st.markdown("---")

# 힌트 상태 초기화 및 유지
if "hint_shown" not in st.session_state:
    st.session_state.hint_shown = False
if "current_problem" not in st.session_state or st.session_state.current_problem != selected_problem:
    st.session_state.current_problem = selected_problem
    st.session_state.hint_shown = False

# 문제 타입에 따른 답 입력 방식
is_multiple_choice = problem.get("type") == "multiple_choice"
is_fill_blank = problem.get("type") == "fill_blank"

if is_fill_blank:
    # 빈칸 채우기 문제
    st.subheader("답 입력")
    col1, col2 = st.columns(2)
    with col1:
        first_blank_input = st.text_input("첫 번째 괄호에 오는 단어:", value="")
    with col2:
        second_blank_input = st.text_input("두 번째 괄호에 오는 단어:", value="")
    
    st.write("⚠️ **약분하지 마세요!** 문제의 숫자 그대로 입력하세요.")
    ratio_input = st.text_input("비를 입력하세요 (예: 3:6)", value="")
    
    check_clicked = st.button("✅ 정답 확인")
    
    if check_clicked:
        # 정답 확인
        first_correct = first_blank_input.strip() == problem["first_blank"]
        second_correct = second_blank_input.strip() == problem["second_blank"]
        
        normalized_ratio = ratio_input.replace(" ", "").replace("：", ":")
        correct_ratio = f"{problem['comparison']}:{problem['standard']}"
        reversed_ratio = f"{problem['standard']}:{problem['comparison']}"
        ratio_correct = normalized_ratio == correct_ratio or normalized_ratio == reversed_ratio
        
        if first_correct and second_correct and ratio_correct:
            st.session_state.hint_shown = False
            st.success("🎉 완벽해요! 모든 답이 맞습니다!")
        else:
            st.session_state.hint_shown = True
            if not first_correct:
                st.error(f"첫 번째 괄호가 틀렸어요. 정답: {problem['first_blank']}")
            if not second_correct:
                st.error(f"두 번째 괄호가 틀렸어요. 정답: {problem['second_blank']}")
            if not ratio_correct:
                st.error(f"비가 틀렸어요. 정답: {problem['comparison']}:{problem['standard']} 또는 {problem['standard']}:{problem['comparison']}")
elif is_multiple_choice:
    # 객관식 문제
    st.subheader("답 선택")
    selected_answer = st.radio("정답을 선택하세요:", options=problem["options"])
    check_clicked = st.button("✅ 정답 확인")
    
    if check_clicked:
        if selected_answer == problem["correct_answer"]:
            st.session_state.hint_shown = False
            st.success("정답이에요! 잘했어요 😊")
        else:
            st.session_state.hint_shown = True
            st.error("틀렸어요. 다시 생각해보세요!")
    
    # 객관식 문제 힌트
    if st.session_state.hint_shown:
        st.info(
            "💡 **힌트**: 비는 '비교하고자 하는 수 : 기준' 순서로 읽습니다. 문제에서 기준이 되는 것이 무엇인지 다시 한번 확인해보세요!"
        )
else:
    # 텍스트 입력 문제
    st.subheader("답 입력")
    st.write("⚠️ **약분하지 마세요!** 문제의 숫자 그대로 입력하세요.")
    answer = st.text_input("정답을 기호로 입력하세요 (예: 3:1)", value="")
    
    check_clicked = st.button("✅ 정답 확인")
    
    # 정답 확인 로직
    if check_clicked:
        normalized = answer.replace(" ", "").replace("：", ":")
        correct_answer = f"{problem['comparison']}:{problem['standard']}"
        reversed_answer = f"{problem['standard']}:{problem['comparison']}"
        
        # 어려운 문제는 두 가지 비 표현식(B에 대한 A의 비, A의 B에 대한 비) 모두 정답
        if difficulty == "어려운 문제":
            # 어려운 문제: 두 가지 형식 모두 정답 인정
            if normalized == correct_answer or normalized == reversed_answer:
                st.session_state.hint_shown = False
                st.success("정답이에요! 잘했어요 😊\n비의 순서는 다양하게 표현될 수 있습니다.")
            else:
                st.session_state.hint_shown = True
                st.error(
                    "아직 정답이 아니에요.\n정답을 `A:B` 형태로 다시 입력해보세요.\n기준량은 ':' 오른쪽입니다."
                )
        else:
            # 중간 문제: 기존 로직 유지
            if normalized == correct_answer:
                st.session_state.hint_shown = False
                st.success("정답이에요! 잘했어요 😊 기준량은 항상 ':'의 오른쪽이에요.")
            elif normalized == reversed_answer:
                st.session_state.hint_shown = True
                st.error(
                    "순서를 바꿔 쓰셨나요? \n기준량은 항상 ':'의 오른쪽에 와야 합니다. \n다시 확인해보세요!"
                )
            else:
                st.session_state.hint_shown = True
                st.error(
                    "아직 정답이 아니에요.\n정답을 `A:B` 형태로 다시 입력해보세요.\n기준량은 ':' 오른쪽입니다."
                )

st.markdown("---")

# 힌트 표시 (텍스트 입력 문제에서만 틀렸을 때만)
if not is_multiple_choice and not is_fill_blank and st.session_state.hint_shown:
    if difficulty == "어려운 문제":
        # 어려운 문제용 상세 힌트
        st.info("💡 **힌트**: 어려운 문제는 비의 두 가지 표현 방식을 모두 정답으로 인정합니다!")
        st.markdown(
            "<div style='border: 2px solid #ff6b6b; padding: 16px; border-radius: 8px; background: #ffe0e0;'>"
            "<div style='font-size: 18px; margin-bottom: 12px;'><strong>📌 비의 두 가지 표현 방식</strong></div>"
            "<div style='font-size: 16px; margin-bottom: 10px;'>"
            "<strong>1️⃣ B에 대한 A의 비 (기준 강조)</strong><br/>"
            "기준이 B입니다. 따라서 A:B 형태로 씁니다.<br/>"
            "예: '농구에 대한 축구의 비' → 축구:농구 = 3:6"
            "</div>"
            "<div style='font-size: 16px;'>"
            "<strong>2️⃣ A의 B에 대한 비 (비교 강조)</strong><br/>"
            "비교하고자 하는 것이 A입니다. 따라서 A:B 형태로 씁니다.<br/>"
            "예: '축구의 농구에 대한 비' → 축구:농구 = 3:6"
            "</div>"
            "</div>",
            unsafe_allow_html=True,
        )
        st.write("✨ **두 표현 모두 같은 의미**이므로 A:B, B:A 어느 것이든 정답입니다!")
    else:
        # 중간/쉬운 문제용 힌트
        st.info(
            "힌트: 비를 읽을 때는 항상 '비교하고자 하는 수 : 기준' 형태로 생각하세요."
        )
        st.markdown(
            "<div style='border: 1px solid #8ecae6; padding: 16px; border-radius: 8px; background: #edf6f9;'>"
            "<div style='font-size: 18px; margin-bottom: 8px;'><strong>생각하는 방법</strong></div>"
            "<div style='font-size: 24px; text-align: center; margin-bottom: 8px;'>'비교하고자 하는 수 : 기준'</div>"
            "<div style='font-size: 16px;'>"
            "왼쪽에는 비교하고 싶은 수를, 오른쪽에는 기준이 되는 수를 놓습니다."
            "</div>"
            "</div>",
            unsafe_allow_html=True,
        )
        st.write("- 예: '사과 : 오렌지'에서 왼쪽은 비교하고자 하는 수, 오른쪽은 기준입니다.")
        st.write("- 이 구조를 먼저 떠올린 뒤, 실제 문제에 맞는 단어를 채워보세요.")

st.markdown("---")

st.caption("Hint: 'A에 대한 B'에서 B가 기준량이 되어 ':' 오른쪽에 옵니다.")
