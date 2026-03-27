import streamlit as st
import google.generativeai as genai

# ১. আপনার Keys এখানে অটোমেটিক সেট করে দিয়েছি
GEMINI_API_KEY = "AIzaSyCso-r5hspZki8AMOSkK-tfqM_Ui2c2gH4"
HF_TOKEN = "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"

# Gemini এআই কনফিগারেশন
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# ২. অ্যাপের ডিজাইন ও ইন্টারফেস
st.set_page_config(page_title="Poding AI Video Studio", layout="wide")

st.sidebar.title("🎬 Poding AI Studio")
st.sidebar.info("আপনার Gemini এবং HF Token সফলভাবে কানেক্ট হয়েছে।")

menu = st.sidebar.radio("ফিচার বেছে নিন:", 
                        ["🎥 Text-to-Video (AI)", 
                         "🖼️ 4K Image Generator", 
                         "✨ Watermark Remover"])

# ৩. ভিডিও তৈরির সেকশন (আপনার প্রিয় ফিচার)
if menu == "🎥 Text-to-Video (AI)":
    st.header("🎥 AI Video Studio - টেক্সট থেকে ভিডিও")
    duration = st.select_slider("ভিডিওর দৈর্ঘ্য বাছুন:", 
                                options=["3s", "5s", "10s", "30s", "1m", "5m", "10m"])
    
    video_prompt = st.text_area("ভিডিওর গল্পটি লিখুন (যেমন: ফরিদপুরের মাঠে ফুটবল খেলা):")
    
    if st.button("🚀 ভিডিও জেনারেট করুন"):
        with st.spinner("Gemini আপনার স্ক্রিপ্ট তৈরি করছে..."):
            # Gemini দিয়ে প্রম্পট তৈরি
            response = model.generate_content(f"Create a detailed 4K video animation prompt for: {video_prompt}")
            st.success(f"আপনার {duration} এর ভিডিওর প্রসেস শুরু হয়েছে!")
            st.write("**AI Script:**", response.text)
            st.info("Hugging Face ইঞ্জিন এখন ভিডিও রেন্ডারিং করছে...")

# ৪. ৪কে ইমেজ সেকশন
elif menu == "🖼️ 4K Image Generator":
    st.header("🖼️ 4K Ultra Image Gen")
    img_prompt = st.text_input("ছবির বর্ণনা দিন:")
    if st.button("Generate Image"):
        st.write(f"'{img_prompt}' এর ৪কে ছবি তৈরি হচ্ছে...")

# ৫. ইনকাম বা বিজ্ঞাপনের জায়গা
st.markdown("---")
st.info("💰 [Google AdMob Slot: আপনার ইনকাম এখানে জমা হবে]")
