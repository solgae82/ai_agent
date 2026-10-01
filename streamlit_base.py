import streamlit as st

# st.write("안녕")

# st.text("이건 그냥 텍스트")
# my_text = "이건 변수에 저장한 텍스트"
# st.text(my_text)

# st.markdown("**굵은 글씨**")
# st.markdown("*기울임*")
# st.markdown("-글머리기호1")
# st.markdown("-글머리기호2")

# tb_text = """
# |열제목1|열제목2|
# |------|------|
# |데이터으하하|데이터2|
# """
# st.markdown(tb_text)

# st.markdown("어떤 글씨는 **볼드**로 , 어떤 글씨는 *이탤릭*으로 표시")
# st.markdown("""
# | 이름 | 나이 | 직업 |
# |-----|------|-----|
# | 홍길동 | 25 | 개발자 |
# | 김철 | 30 | 데이터 분석가 |
# | 이영희 | 28 | 디자이너 |
# """)

# st.title("타이틀")
# st.header("헤더")
# st.subheader("서브헤더")
# st.text("안녕")

# st.write("어떤 글씨는 **볼드**로, 어떤 글씨는 *이탤릭*으로 표시(.write)")

# st.write("# 타이틀")
# st.write("## 헤더")
# st.write("### 서브헤더")
# st.write("안녕2")

# st.write("# write 메소드")
# st.write(10 + 3)
# st.write(13)
# st.write([1,2,3,4,5])
# st.write({"mail":"소년","femail":"소녀"})

# # 기본 레이아웃 , 아래도 계속 쌓인다
# st.write("첫번째 테스트")
# st.write("두번째 테스트")
# st.write("세번째 테스트")
# st.write("네번째 테스트")

# # 열 레이아웃
# col1, col2 = st.columns(2)
# with col1: 
#     st.write("왼쪽열")
#     st.write("왼쪽열 아래")
# with col2: 
#     st.write("오른쪽열") 

# col1, col2, col3 = st.columns([1,3,1])
# with col1:
#     st.write("1열")
# with col2: 
#     st.write("2열-넓은열")
# with col3: 
#     st.write("3열")

# # 사이드바 레이아웃
# with st.sidebar: 
#     st.title("사이드바")
#     st.write("사이드바에 표시할 텍스트")

# 페이지 설정
st.set_page_config(
    page_title = "AI_에이전트",
    page_icon ="🤣",
    layout = "wide"
)

col1, col2 = st.columns(2)
with col1: 
    st.write("1열")
    st.write("Hi")
with col2: 
    st.write("2열")
    st.write("there!")

