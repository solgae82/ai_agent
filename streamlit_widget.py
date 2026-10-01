import streamlit as st

# 버튼 위젯
button = st.button("클릭하세요")
print(button) # 버튼 클릭 / True

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