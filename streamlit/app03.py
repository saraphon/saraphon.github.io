import streamlit as st
h = st.header('My wed Site on Diffusion')
s = st.subheader('เว็บไซต์ส่วนตัวของฉัน')
p = st.write('เว็บไซตืนี้แลกมาด้วยหยาดเหงื่อและความอดทน')
banner = st.image('https://picsum.photos/800/250')
text = st.text_input('prompt: ')
if text:
    #textt
    st.image('https://picsum.photos/400/200')
    b = st.button('จะไปต่อหรือ...')


