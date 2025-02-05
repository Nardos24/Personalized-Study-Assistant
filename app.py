import streamlit as st
from utils.ai_utils import generate_summary
from utils.wikipedia_utils import get_wikipedia_summary

# ✅ Set page config at the very top
st.set_page_config(page_title="📚 Personalized Study Assistant", layout="wide")

# Load custom styles
with open("assets/style.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Streamlit UI
st.title("✍️ Personalized Study Assistant")
st.write("Learn topics with AI-generated summaries.")

# User Inputs
topic = st.text_input("Enter a topic to learn about:", "")
detail_level = st.selectbox("Select level of detail:", ["Short", "Medium", "In-depth"])
output_format = st.radio("Select output format:", ["Bullet Points", "Paragraph"])

# Button to Generate Summary
if st.button("Generate Summary"):
    if topic:
        with st.spinner("Generating summary..."):
            summary = generate_summary(topic, detail_level, output_format)
            wikipedia_summary = get_wikipedia_summary(topic)
            
            st.subheader("Summary:")
            st.write(summary)
            
            if wikipedia_summary:
                st.subheader("🔎 Additional Info from Wikipedia:")
                st.write(wikipedia_summary)
    else:
        st.warning("Please enter a topic!")
