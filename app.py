import streamlit as st
import google.generativeai as genai

# আপনার API Key
GEMINI_API_KEY = "AIzaSyCso-r5hspZki8AMOSkK-tfqM_Ui2c2gH4"
genai.configure(api_key=GEMINI_API_KEY)

# মডেল আপডেট করা হয়েছে (gemini-1.5-flash-latest)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

st.set_page_config(page_title="Poding AI Video Studio", layout="wide")
st.title("🎬 Poding AI Video Studio")

video_prompt = st.text_area("ভিডিওর গল্পটি লিখুন:", placeholder="যেমন: ডাইনোসর গভীর জঙ্গলে হাঁটছে...")

if st.button("🚀 ভিডিও জেনারেট করুন"):
    if video_prompt:
        with st.spinner("AI কাজ করছে..."):
            try:
                # লেটেস্ট মেথড ব্যবহার করে রেসপন্স জেনারেট করা
                response = model.generate_content(f"Create a high-quality 4K AI video animation prompt for: {video_prompt}")
                st.success("আপনার ভিডিওর জন্য প্রম্পট তৈরি হয়েছে!")
                st.write(response.text)
            except Exception as e:
                st.error(f"দুঃখিত, আবার এরর আসছে: {str(e)}")
    else:
        st.warning("আগে কিছু লিখুন!")
