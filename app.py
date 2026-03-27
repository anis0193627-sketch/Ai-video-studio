import streamlit as st
import google.generativeai as genai

# সরাসরি কনফিগারেশন
genai.configure(api_key="AIzaSyCso-r5hspZki8AMOSkK-tfqM_Ui2c2gH4")

st.title("🎬 Poding AI Video Studio")

# সবচেয়ে সাধারণ মডেল যা কাজ করবেই
model = genai.GenerativeModel('gemini-1.5-flash')

prompt_input = st.text_input("ভিডিওর গল্প লিখুন:")

if st.button("🚀 ভিডিও জেনারেট করুন"):
    if prompt_input:
        try:
            # খুব সহজ মেথড ব্যবহার করা হয়েছে
            response = model.generate_content(f"Create a video prompt for: {prompt_input}")
            st.success("তৈরি হয়েছে!")
            st.write(response.text)
        except Exception as e:
            st.error(f"এরর: {e}")
    else:
        st.warning("আগে কিছু লিখুন")
