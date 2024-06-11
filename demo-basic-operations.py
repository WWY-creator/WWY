import streamlit as st
st.title("干饭人，干饭魂，干饭都人上人！")
st.header("人是铁饭是钢")
st.subheader("一顿不吃饿得慌")
st.text("什么时候吃饭")

st.markdown("this is an image: \n \
            ![](https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.alicdn.com%2Fi4%2F2200612686982%2FO1CN01PCgEQp21RnyYh0QMS_%21%212200612686982.png&refer=http%3A%2F%2Fimg.alicdn.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1720703666&t=4846a8e190500c4f709de755744e7a9f)")

if st.checkbox("Show/Hide"):
    st.text("You checked the box")


status = st.radio("select gender:" ,
                  ('Male',
                   'Female'))
if status == 'Male':
    st.success("Male")
else:
    st.success("Female")

tastes = st.multiselect("tastes:",
               ['sweet',
                'sour',
                'spicy',
                'salty'])
st.write("You selected: ", tastes)

if st.button("about"):
    st.text("Streamlit is a great tool")

name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write("Hello, ", name)

level = st.slider("Select your level", 1, 5)
st.write("You selected: ", level)

from fastai.vision.all import *
upload_img = st.file_uploader("Upload an image",
                               type=['jpg',
                                      'png'])

if upload_img is not None:
    img = PILImage.create(upload_img)
    st.image(img.to_thumb(256,256), 
             caption="Uploaded Image")

    