import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
from questionBank import questions, stream_questions
import random

# Set page layout to wide mode
st.set_page_config(layout="wide")

load_dotenv()

# Create two dropdown filters: Teams and Locations
col1, col2, col3, col4, col5, col6 = st.columns([1.5, 3, 3, 1.5, 1.5, 1.5], vertical_alignment="center")
with col2:
    st.subheader("Careers at OpenAI")
with col3:
    st.write("62 jobs")
with col4:
    team_filter = st.selectbox("All teams", ["All teams", "Sales", "Applied AI Engineering", "IT", "Leverage Engineering", "Communications"])
with col5:
    location_filter = st.selectbox("All locations", ["All locations", "San Francisco", "Tokyo, Japan", "Remote - Singapore"])

# Jobs data (mocked for this example)
jobs = [
    {"title": "Account Director - Japan", "team": "Sales, Platform", "location": "Tokyo, Japan"},
    {"title": "Account Director, Strategics", "team": "Sales", "location": "Remote - Singapore"},
    {"title": "Analytics Data Engineer, Applied Engineering", "team": "Applied AI Engineering", "location": "San Francisco"},
    {"title": "Android Engineer, ChatGPT", "team": "Applied AI Engineering", "location": "San Francisco"},
    {"title": "Audiovisual Engineer, IT", "team": "IT", "location": "San Francisco"},
    {"title": "Backend Software Engineer, Leverage Engineering", "team": "Leverage Engineering", "location": "San Francisco"},
    {"title": "Communications Strategy & Operations Lead", "team": "Communications", "location": "San Francisco"},
]

# Filter jobs based on the selected filters
filtered_jobs = [job for job in jobs if (team_filter == "All teams" or team_filter in job["team"]) and (location_filter == "All locations" or location_filter in job["location"])]

# Display the filtered job listings
for job in filtered_jobs:
    col1, col2, col3, col4, col5 = st.columns([1.5, 6, 2, 1, 1.5], vertical_alignment="center")
    with col2:
        st.write(f"**{job['title']}** {job['team']}")
    with col3:
        st.markdown(f"""
        <div style="text-align: right;">
            <p>{job['location']}</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.button("Apply now", key=job["title"])

col1, col2, col3 = st.columns([1.5, 8, 1.5], vertical_alignment="center")
with col2:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "answeredQs" not in st.session_state:
        st.session_state.answeredQs = {1,2}

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Let's work together"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container

        filtered_numbers = [num for num in list(range(0, len(questions))) if num not in st.session_state.answeredQs]
        random_i = random.choice(filtered_numbers)
        st.session_state.answeredQs.add(random_i)

        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("system"):
            messages_w_q = []
            for m in st.session_state.messages:
                new_message = {"role": m["role"], "content": m["content"]}
                messages_w_q.append(new_message)
            # messages_w_q[-1]["content"] = messages_w_q[-1]["content"] + questions[random_i]
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=messages_w_q,
                stream=True,
            )
            response = st.write_stream(stream) 
            question = st.write_stream(stream_questions)
            print(messages_w_q)

        st.session_state.messages.append({"role": "system", "content": response+" "+question}) #"Let's set up a call "+"https://calendly.com/naraharipranav/30min"})
        