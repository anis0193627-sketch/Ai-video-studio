import streamlit as st
import google.generativeai as genai

# ১. আপনার API Key এখানে সেট করা আছে
GEMINI_API_KEY = "AIzaSyCso-r5hspZki8AMOSkK-tfqM_Ui2c2gH4"
genai.configure(api_key=GEMINI_API_KEY)

# ২. নতুন মডেল ব্যবহার (যা এরর দূর করবে)
model = genai.GenerativeModel('gemini-1.5-flash')

# ৩. অ্যাপের ডিজাইন
st.set_page_config(page_title="Poding AI Video Studio", layout="wide")
st.title("🎬 Poding AI Video Studio")

st.markdown("---")

# ভিডিওর ইনপুট সেকশন
video_prompt = st.text_area("ভিডিওর গল্পটি লিখুন (যেমন: ফরিদপুরের সবুজ মাঠে ফুটবল খেলা):", placeholder="এখানে আপনার আইডিয়াটি লিখুন...")

if st.button("🚀 ভিডিও জেনারেট করুন"):
    if video_prompt:
        with st.spinner("জেমিনী আপনার জন্য প্রম্পট তৈরি করছে..."):
            try:
                # এআই থেকে রেসপন্স নেওয়া
                response = model.generate_content(f"Create a high-quality, detailed AI video animation prompt and camera movement for: {video_prompt}")
                
                st.success("আপনার ভিডিওর জন্য এআই প্রম্পট তৈরি হয়েছে!")
                st.subheader("আপনার প্রম্পটটি নিচে দেওয়া হলো:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"দুঃখিত, একটি সমস্যা হয়েছে: {e}")
    else:
        st.warning("দয়া করে আগে ভিডিওর জন্য কিছু লিখুন!")

st.markdown("---")
st.info("টিপস: এই প্রম্পটটি কপি করে আপনি যেকোনো ভিডিও এআই-তে ব্যবহার করতে পারবেন।")
