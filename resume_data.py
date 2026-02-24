# Resume data for Ayush Kumar Gupta
resume_data = {
    "personal_info": {
        "name": "Ayush Kumar Gupta",
        "title": "Aspiring Software Engineer",
        "location": "Bokaro, Jharkhand",
        "phone": "7070450883",
        "email": "horridayush1@gmail.com",
        "education": "B.Tech CSE (AI & ML) Student | NIST University",
        "linkedin": "https://www.linkedin.com/in/ayush-kumar-gupta-524bb8386"
    },
    "skills": {
        "programming_languages": ["C", "C++", "Python", "JavaScript"],
        "web_technologies": ["HTML", "CSS", "JavaScript", "Flask", "Node.js", "React"],
        "databases": ["MySQL", "MongoDB", "Firebase"],
        "tools": ["Git", "VS Code", "Postman", "Docker", "Jupyter Notebook"]
    },
    "projects": [
        {
            "name": "Portfolio Chat Website",
            "tech": "HTML, CSS, JavaScript, Flask, Python",
            "description": "A personal portfolio website with integrated chatbot functionality using Groq API for AI-powered responses."
        },
        {
            "name": "AI Chat Application",
            "tech": "Python, Flask, Groq API",
            "description": "Real-time chat application with AI capabilities for enhanced user interaction."
        }
    ],
    "education": [
        {
            "degree": "B.Tech in Computer Science and Engineering (AI & ML)",
            "institution": "NIST University",
            "status": "Pursuing"
        }
    ],
    "experience": [],
    "achievements": [
        "Developed AI-powered portfolio website with interactive chatbot",
        "Proficient in full-stack web development",
        "Strong foundation in machine learning and artificial intelligence"
    ]
}

# System prompt for the AI chatbot
system_prompt = f"""
You are Ayush Kumar Gupta's AI assistant. You have complete knowledge about Ayush's resume and can answer questions about his background, skills, projects, and education.

Resume Information:
- Name: {resume_data['personal_info']['name']}
- Title: {resume_data['personal_info']['title']}
- Education: {resume_data['personal_info']['education']}
- Location: {resume_data['personal_info']['location']}
- Phone: {resume_data['personal_info']['phone']}
- Email: {resume_data['personal_info']['email']}
- LinkedIn: {resume_data['personal_info']['linkedin']}

Skills:
- Programming Languages: {', '.join(resume_data['skills']['programming_languages'])}
- Web Technologies: {', '.join(resume_data['skills']['web_technologies'])}
- Databases: {', '.join(resume_data['skills']['databases'])}
- Tools: {', '.join(resume_data['skills']['tools'])}

Projects:
{chr(10).join([f"- {project['name']}: {project['description']} (Tech: {project['tech']})" for project in resume_data['projects']])}

Education:
{chr(10).join([f"- {edu['degree']} at {edu['institution']} ({edu['status']})" for edu in resume_data['education']])}

Answer questions professionally and helpfully. If you don't have specific information about something, politely say so and suggest contacting Ayush directly.
"""
