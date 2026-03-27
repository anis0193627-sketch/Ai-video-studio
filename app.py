import streamlit as st
import google.generativeai as genai

# আপনার API Key
GEMINI_API_KEY = "AIzaSyCso-r5hspZki8AMOSkK-tfqM_Ui2c2gH4"
genai.configure(api_key=GEMINI_API_KEY)

# সব ধরণের মডেল সাপোর্ট করার জন্য এই অটো-লজিক
def get_model():
    models = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
    for m in models:
        try:
            test_model = genai.GenerativeModel(m)
            return test_model
        except:
            continue
    return genai.GenerativeModel('gemini-pro')

model = get_model()

st.set_page_config(page_title="Poding AI Video Studio", layout="wide")
st.title("🎬 Poding AI Video Studio")

video_prompt = st.text_area("ভিডিওর গল্পটি লিখুন:", placeholder="যেমন: নীল আকাশে পাখি উড়ছে...")

if st.button("🚀 ভিডিও জেনারেট করুন"):
    if video_prompt:
        with st.spinner("AI প্রম্পট তৈরি করছে..."):
            try:
                # সরাসরি টেক্সট জেনারেট করা
                response = model.generate_content(f"Act as an AI Video Engineer. Create a detailed 4K prompt for: {video_prompt}")
                st.success("আপনার ভিডিওর জন্য এআই প্রম্পট তৈরি হয়েছে!")
                st.write(response.text)
            except Exception as e:
                st.error(f"দুঃখিত, মডেলটি কাজ করছে না। এরর: {str(e)}")
    else:
        st.warning("দয়া করে আগে কিছু লিখুন!")
        
