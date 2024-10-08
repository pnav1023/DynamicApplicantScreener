import random

def stream_questions():
    randomInt = random.randint(0, len(questions)-1)
    yield questions[randomInt]

questions = [
    "Can you walk me through your educational background and how it has prepared you for a role in software engineering?",
    "What were some of the most challenging courses or projects you worked on during your academic career?",
    "Did you work on any AI, machine learning, or deep learning projects during your studies? If so, can you describe one?",
    "How did your education help you develop the skills necessary for this position, especially in terms of programming or AI?",
    "Can you tell us about your most recent role? What were your primary responsibilities and challenges?",
    "What were the technologies and tools you worked with in that role?",
    "Have you worked on any projects related to artificial intelligence or machine learning in your previous positions? Could you describe one of them?",
    "What was the most technically challenging project you've worked on in your past roles? How did you overcome the challenges?",
    "Was this a team project? How did you collaborate with other engineers?",
    "Have you worked in an agile development environment? How did you manage tight deadlines or rapidly changing requirements?",
    "In your previous jobs, what programming languages did you primarily use? Why were those chosen for your projects?",
    "Have you worked with cloud platforms (AWS, Azure, GCP)? If so, can you describe a project where you utilized cloud infrastructure?",
    "What version control systems (e.g., Git) did you use in your previous projects? Can you describe a time you resolved a conflict during a merge?",
    "Have you worked with any machine learning frameworks (e.g., TensorFlow, PyTorch)? If yes, could you describe a project where you used one of these?",
    "Have you ever worked on developing or fine-tuning machine learning models? Could you give an example?",
    "In your experience, what are some challenges when deploying machine learning models to production?",
    "Can you describe any projects where you had to experiment with hyperparameter tuning for a deep learning model?",
    "Have you had any experience working with large language models (LLMs) or transformer-based architectures like GPT?",
    "Have you contributed to any open-source projects? If so, can you describe your contributions?",
    "How did you identify the areas where you could make contributions?",
    "Have you worked on any side projects or personal coding challenges outside of work? Can you tell us about a particularly interesting one?",
    "Do you have a GitHub profile or portfolio that showcases your personal projects? Can you walk us through a project that you're particularly proud of?",
    "Have you had the chance to lead a team or mentor other engineers in your previous roles? How did you approach that?",
    "Can you describe a time when you worked on a large project with a team? How did you ensure good collaboration and communication?",
    "What role do you usually take when working on a team project? Are you more of a leader, a problem solver, or someone who prefers focusing on a particular technical area?",
    "Can you describe a situation where you had a disagreement with a colleague or team member on how to approach a problem? How did you handle it?",
    "Can you walk me through a time when you had to make a critical technical decision? What was the context, and how did you arrive at your solution?",
    "Tell me about a time when something went wrong in a project you were working on. How did you troubleshoot the issue and resolve it?",
    "Have you ever had to balance technical debt with feature development in your previous roles? How did you approach that?",
    "How has your career in software engineering progressed over time? What are some key milestones or achievements that you're particularly proud of?",
    "Why did you move from your last role? What are you looking for in your next position?",
    "Where do you see yourself in 5 years? How do you think a position at OpenAI will help you achieve your long-term career goals?",
    "What made you interested in applying to OpenAI?",
    "What excites you the most about working in the field of AI?",
    "What specific aspects of this role at OpenAI caught your attention, and how do your past experiences align with what we’re looking for?",
    "Do you have experience with any of the models developed by OpenAI (e.g., GPT, DALL-E, Codex)? If so, what has been your experience using them?",
    "Have you had any experience with DevOps, including CI/CD pipelines, containerization (Docker), or Kubernetes?",
    "Are you familiar with distributed systems? Can you describe a project where you had to build or maintain a distributed system?",
    "Have you worked with large datasets in the past? What were some challenges you faced, and how did you resolve them?"
]
