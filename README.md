# 🌐 Portfolio Chat Website

A modern, interactive portfolio website with an AI-powered chatbot built using Flask, Groq API, and JavaScript.

## 🚀 Features

- **Professional Portfolio**: Clean, responsive design showcasing skills and projects
- **AI Chatbot**: Intelligent assistant trained on resume data using Groq's Llama API
- **Minimizable Interface**: Floating chat widget that can be toggled on/off
- **Conversation History**: Remembers previous interactions during the session
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Real-time Interaction**: Instant responses powered by AI

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Python Flask
- **AI Integration**: Groq API with Llama 3.1 model
- **Styling**: Custom CSS with modern animations
- **Deployment**: Local development server

## 📁 Project Structure

```
Portfolio-chat/
├── app.py                 # Flask application and API endpoints
├── resume_data.py         # Resume information and system prompt
├── test_chat.py           # Testing script for chat functionality
├── static/
│   ├── css/
│   │   └── style.css      # Main stylesheet
│   ├── js/
│   │   ├── script.js      # Portfolio animations and interactions
│   │   └── chatbot.js     # Chatbot frontend logic
│   └── images/
│       └── Myimage.jpeg   # Profile image
└── templates/
    └── index.html         # Main HTML template
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd d:\Portfolio-chat
   ```

2. **Install required dependencies:**
   ```bash
   pip install flask groq flask-cors python-dotenv httpx
   ```
   _`httpx` is included for HTTP testing or if you prefer an async-capable client._

3. **Configure environment variables:**
   - Copy `.env` or create it in the project root.
   - Add your Groq API key:
     ```ini
     GROQ_API_KEY=your_groq_api_key_here
     ```
   - The application loads variables from `.env` automatically using `python-dotenv`.
   - Make sure **not** to commit your real key; `.env` is included in `.gitignore`.

### Running the Application

#### Development Mode
1. **Start the Flask development server:**
   ```bash
   python app.py
   ```

2. **Access the website:**
   - Open your browser and go to: `http://127.0.0.1:5000`
   - Or use the network URL: `http://[your-ip]:5000`

#### Production Mode (Cross-Platform)

**For Linux/macOS (using Gunicorn):**
```bash
# Basic usage
gunicorn --config gunicorn.conf.py wsgi:app

# Or with custom settings
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app

# Run in background
gunicorn --config gunicorn.conf.py wsgi:app --daemon
```

**For Windows:**
- Use the development server with `python app.py`
- Or use Waitress (Windows-compatible WSGI server):
  ```bash
  pip install waitress
  waitress-serve --host=0.0.0.0 --port=5000 wsgi:app
  ```

3. **Access the website:**
   - Same URLs as development mode
   - Gunicorn provides better performance and stability for production

3. **Interact with the chatbot:**
   - Click the 💬 button in the bottom-right corner
   - Ask questions about the portfolio owner's skills, projects, and background

## 🤖 Chatbot Capabilities

The AI assistant can answer questions about:

### Personal Information
- Name, title, and professional background
- Contact details (email, phone, location)
- LinkedIn profile and social links

### Technical Skills
- Programming languages (C, C++, Python, JavaScript)
- Web technologies (HTML, CSS, Flask, React, Node.js)
- Databases (MySQL, MongoDB, Firebase)
- Development tools (Git, VS Code, Docker, Postman)

### Projects & Experience
- Detailed project descriptions
- Technologies used in each project
- Educational background and achievements

### Sample Questions
- "What are Ayush's skills?"
- "Tell me about the Portfolio Chat Website project"
- "What programming languages does Ayush know?"
- "Where is Ayush located?"
- "What is Ayush's educational background?"

## 🎨 Customization

### Updating Resume Data
Modify `resume_data.py` to update personal information:
```python
resume_data = {
    "personal_info": {
        "name": "Your Name",
        "title": "Your Title",
        # ... other fields
    },
    "skills": {
        # ... your skills
    }
    # ... other sections
}
```

### Changing Chatbot Appearance
Edit `static/css/style.css` to modify:
- Chatbot colors and themes
- Button styles and animations
- Message bubble designs
- Responsive breakpoints

### Modifying AI Behavior
Update the `system_prompt` in `resume_data.py` to change how the AI responds.

## 📱 Responsive Design

The website is fully responsive and optimized for:
- **Desktop**: Full feature set with side navigation
- **Tablet**: Adapts layout for medium screens
- **Mobile**: Collapsible menu and optimized chatbot size

## 🔧 API Endpoints

### POST `/chat`
Send a message to the AI assistant

**Request:**
```json
{
  "message": "Your question here"
}
```

**Response:**
```json
{
  "response": "AI generated response",
  "status": "success"
}
```

### POST `/clear-chat`
Clear conversation history

**Response:**
```json
{
  "status": "success",
  "message": "Chat history cleared"
}
```

## 🐛 Troubleshooting

### Common Issues

1. **"Model decommissioned" error**
   - Solution: Update the model name in `app.py` to a currently supported model
   - Check Groq documentation for latest models

2. **API key errors**
   - Verify your Groq API key is valid and correctly set in `.env` or your environment.
   - Ensure the `.env` file is named properly and not committed to source control.
   - Check internet connection and key permissions

3. **Chatbot not responding**
   - Check browser console for JavaScript errors
   - Verify Flask server is running
   - Ensure CORS is properly configured

4. **Styling issues**
   - Clear browser cache
   - Check that all CSS files are loading
   - Verify file paths in HTML

### Debugging

Enable debug mode in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

Use the test script:
```bash
python test_chat.py
```

## 🏗️ Production Deployment

### WSGI Server Options

**1. Gunicorn (Linux/macOS Recommended)**
- **Configuration**: `gunicorn.conf.py`
- **Entry Point**: `wsgi.py`
- **Best for**: Unix-like systems

**2. Waitress (Windows Alternative)**
- Install: `pip install waitress`
- Run: `waitress-serve --host=0.0.0.0 --port=5000 wsgi:app`
- **Best for**: Windows deployment

### Key Configuration Options

- **Workers**: 2-4 workers (based on CPU cores)
- **Timeout**: 30 seconds for request processing
- **Preload App**: Enabled for performance
- **Logging**: Structured logs to stdout

### Deployment Commands

**Gunicorn (Linux/macOS):**
```bash
# Default configuration
gunicorn --config gunicorn.conf.py wsgi:app

# Custom worker count (2x CPU cores)
gunicorn -w 4 --config gunicorn.conf.py wsgi:app

# Custom bind address
gunicorn -b 127.0.0.1:8000 --config gunicorn.conf.py wsgi:app
```

**Waitress (Windows):**
```bash
# Basic usage
waitress-serve --host=0.0.0.0 --port=5000 wsgi:app

# With threads
waitress-serve --threads=4 --host=0.0.0.0 --port=5000 wsgi:app
```

### Process Management

For production environments, consider using:
- **Systemd** (Linux): Create a service file
- **Supervisor**: Process control system
- **Docker**: Containerized deployment
- **PM2**: Process manager (cross-platform)

## 📄 License

This project is for personal/portfolio use. Feel free to customize and extend as needed.

## 🙏 Acknowledgments

- **Groq** for providing the AI API
- **Llama** models for natural language processing
- **Flask** for the web framework
- **FontAwesome** for icons (if used)

## 📞 Contact

For questions or support, contact the portfolio owner through the provided contact information on the website.

---

⭐ **Tip**: The chatbot works best with clear, specific questions about skills, projects, and experience!