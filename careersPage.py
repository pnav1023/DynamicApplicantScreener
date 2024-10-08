import streamlit as st
from dotenv import load_dotenv
from demo_data.conversation import stream_data

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
    {"title": "Software Engineer, Backend", "team": "Applied AI Engineering", "location": "San Francisco"}
]

demo_job = [
    {"title": "Software Engineer, Backend", "team": "Applied AI Engineering", "location": "San Francisco"}
]

if "filtered_jobs" not in st.session_state:
    st.session_state.filtered_jobs = [job for job in jobs if (team_filter == "All teams" or team_filter in job["team"]) and (location_filter == "All locations" or location_filter in job["location"])]

# Display the filtered job listings
for job in st.session_state.filtered_jobs:
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
        apply = st.button("Apply now", key=job["title"])
        if apply:
            st.session_state.filtered_jobs = demo_job

col1, col2, col3 = st.columns([1.5, 8, 1.5], vertical_alignment="bottom")
with col2:
    st.file_uploader(
        "Upload your resume and any other resources that you would like", accept_multiple_files=True
    )
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "curr" not in st.session_state:
        st.session_state.curr = 0

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Say hi to get started on your interview!"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(stream_data(st.session_state.curr))
            st.session_state.curr += 1
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
