from youtube_analyzer import build_youtube_agent
import streamlit as st

st.set_page_config(
    page_title="Youtube video Analyzer",
    layout="centered"
)

st.title("🎥 AI Youtube Video Analyzer")

@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()
# input box 
video_url = st.text_input("Enter Youtube Video Link") #str
button = st.button("Analyze Video") #True/False

if video_url and button:
    with st.spinner("Analyzing Video..."):
        response = agent.run(
            f"Analyse this video: {video_url}"
        )
    st.markdown("Analysis Report of Video:")
    st.markdown(response.content)
