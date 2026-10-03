import streamlit as st
import os
import uuid

# 버튼 위젯
button = st.button("클릭하세요")
print(f"버튼 클릭: {button}") # 버튼 클릭 / True

if button: 
    st.write("button 클릭했어유")

st.link_button("네이버","https://www.naver.com/") 

# 입력 위젯
input_text = st.text_input("입력하세요")
if input_text: 
    st.write(f"입력 완료: {input_text}")

chat_text = st.chat_input("무슨 과일을 좋아하세요?")
if chat_text: 
    st.write(f"당신은 {chat_text}를 좋아하시는군요!")

# 선택형 위젯
option = st.selectbox("좋아하는 과일을 선택하세요", ["사과","포도","수박","바나나"])
st.write(f"선택한 과일: {option}")

options = st.multiselect("좋아하는 과일을 모두 선택하세요", ["포도","수박","배","사과","바나나"])
st.write(f"좋아하는 과일들: {options}")

# 파일 위젯
upload_file = st.file_uploader("파일 업로드") # test.txt 로 테스트
st.write(f"업로드 파일객체 정보: {upload_file}")

if upload_file is not None: 
    temp_dir = "upload_files"
    if not os.path.exists(temp_dir): # 디렉토리 없으면 만든다 
        os.makedirs(temp_dir)   


    copy_file_name = upload_file.name + "_" + str(uuid.uuid4())[:10]
    print(f"파일복사이름: {copy_file_name}")

    # 복사 이동 파일 절대경로
    file_path = os.path.join(temp_dir, copy_file_name) # 

    with open(file_path, "wb") as f: 
        f.write(upload_file.getbuffer())

    # 복사 파일 체크(잘 이동 되었나)
    if os.path.exists(file_path) and os.path.isfile(file_path): 

        file_size = os.path.getsize(file_path) / 1024

        st.success("파일 업로드 성공!")
        st.info(f"**저장경로:** {os.path.abspath(file_path)}")
        st.info(f"**저장된 파일크기:** {file_size:.2f} KB")

if upload_file: 
    st.write(f"원본파일명: {upload_file.name}") # 원본 파일명
    file_content = upload_file.read().decode("utf-8")
    st.write(f"파일내용: {file_content}")


# 다운로드 버튼(데이터 다운로드 버튼)
text_data ="""여러줄 테스트
뭐냐이건
허허허"""

download_button = st.download_button(
    "텍스트 다운로드",
    data = text_data,
    file_name="결과.txt"
)
