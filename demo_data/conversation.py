import time

def stream_data(i):
    for word in recruiter[i].split(" "):
        yield word + " "
        time.sleep(0.03)

recruiter = [
    "Hi Pranav! Thanks for joining the interview today. I’ve had a chance to look over your resume, and I’m excited to learn more about your experience. To start, could you give me a quick summary of your background and what led you to apply for this backend engineering position at OpenAI?",
    "That sounds like a great fit. I noticed you’ve done work with AWS and cloud infrastructure, especially during your time at Citizens. Could you tell me more about the cloud migration project you led there?",
    "Wow, that’s impressive. For the backend role here at OpenAI, we look for engineers who can work with large-scale distributed systems. Could you talk about your experience building or optimizing backend systems for scalability and performance?",
    "That’s great experience. OpenAI values engineers who are adaptable and can learn new technologies quickly. You’ve worked with Solidity, Python, and TypeScript, among others. How do you approach learning new languages or frameworks, especially in fast-moving fields like AI or blockchain?",
    "Hands-on projects are definitely a great way to learn. Speaking of projects, I noticed you’ve worked on some AI-related initiatives, like your dnAI chatbot. Could you tell me more about that project and what you found most challenging?",
    "That sounds like a complex and rewarding project. At OpenAI, collaboration is key. Can you tell me about a time when you worked closely with a team to solve a challenging problem?",
    "Team collaboration and fast iteration are definitely important here. Thanks for sharing, Pranav. Your experience and problem-solving approach sound like a great match for what we’re looking for at OpenAI. We’ll take this forward to the hiring team and be in touch soon!"
]

applicant = [
    "Sure! I have a background in full-stack and backend engineering with a focus on Python, Java, and AWS. I’ve worked on cloud migration projects, smart contract development, and infrastructure automation. Lately, I’ve been working with Outlier AI, improving machine learning models. OpenAI's mission of advancing AI for good aligns with my interests in the future of tech and AI ethics, which is why I’m excited to apply.",
    "Absolutely. At Citizens, I was responsible for automating the migration of hundreds of on-prem applications to the cloud. I developed a cloud migration service using AWS Lambda, Python, and ReactJS for the UI. By automating processes, we reduced migration time from three weeks to just 30 minutes, which was a huge win for the team.",
    "Definitely. Recently, I’ve been working on a blockchain-based contract solution, where we optimized the system to handle high traffic and complex dependencies. We used Rust for some performance-critical parts and employed caching mechanisms to handle scaling better. This experience has taught me a lot about designing for both efficiency and reliability.",
    "I usually start with small, hands-on projects to get a feel for the language or framework. For example, when I started with Solidity, I built a Web3 app to store game states on the Ethereum network. I also focus on understanding the fundamental principles behind the language, which helps me apply those skills across different contexts.",
    "dnAI was a personalized chatbot that used AI to recommend supplements based on a user’s genetics. I used Python for the backend and Selenium for web scraping. The challenge was integrating different data sources and ensuring the chatbot could adapt its responses based on the user’s input. It was a fun project that pushed my understanding of data-driven AI systems.",
    "At Outlier AI, we had to troubleshoot a recurring issue with model performance in production. I worked closely with data scientists and fellow engineers to analyze the data flow, and we pinpointed an issue with our preprocessing pipeline. We quickly iterated on solutions, and eventually improved model accuracy by 15%."
]
