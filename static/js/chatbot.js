// Chatbot functionality
class Chatbot {
    constructor() {
        this.isOpen = false;
        this.isTyping = false;
        this.init();
    }

    init() {
        // Create chatbot elements
        this.createChatbot();
        
        // Add event listeners
        this.addEventListeners();
        
        // Add welcome message
        setTimeout(() => {
            this.addMessage('Hello! I\'m Ayush\'s AI assistant. How can I help you today?', 'ai');
        }, 1000);
    }

    createChatbot() {
        const chatbotHTML = `
            <div class="chatbot-container">
                <div class="chatbot-toggle" id="chatbotToggle">
                    💬
                </div>
                <div class="chatbot-window" id="chatbotWindow">
                    <div class="chatbot-header">
                        <h3>Ayush's Assistant</h3>
                        <button class="chatbot-close" id="chatbotClose">×</button>
                    </div>
                    <div class="chatbot-messages" id="chatbotMessages">
                        <div class="typing-indicator" id="typingIndicator">
                            <span></span>
                            <span></span>
                            <span></span>
                        </div>
                    </div>
                    <div class="chatbot-input">
                        <input type="text" id="chatbotInput" placeholder="Type your message..." maxlength="500">
                        <button class="chatbot-send" id="chatbotSend">➤</button>
                    </div>
                </div>
            </div>
        `;
        
        document.body.insertAdjacentHTML('beforeend', chatbotHTML);
        
        // Store references
        this.toggleBtn = document.getElementById('chatbotToggle');
        this.window = document.getElementById('chatbotWindow');
        this.messagesContainer = document.getElementById('chatbotMessages');
        this.input = document.getElementById('chatbotInput');
        this.sendBtn = document.getElementById('chatbotSend');
        this.closeBtn = document.getElementById('chatbotClose');
        this.typingIndicator = document.getElementById('typingIndicator');
    }

    addEventListeners() {
        // Toggle chatbot
        this.toggleBtn.addEventListener('click', () => this.toggleChatbot());
        this.closeBtn.addEventListener('click', () => this.closeChatbot());
        
        // Send message
        this.sendBtn.addEventListener('click', () => this.sendMessage());
        this.input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.sendMessage();
            }
        });
        
        // Close on outside click
        document.addEventListener('click', (e) => {
            if (!this.window.contains(e.target) && !this.toggleBtn.contains(e.target)) {
                if (this.isOpen) {
                    this.closeChatbot();
                }
            }
        });
    }

    toggleChatbot() {
        this.isOpen = !this.isOpen;
        if (this.isOpen) {
            this.window.classList.add('active');
            this.toggleBtn.textContent = '✕';
            this.input.focus();
        } else {
            this.window.classList.remove('active');
            this.toggleBtn.textContent = '💬';
        }
    }

    closeChatbot() {
        this.isOpen = false;
        this.window.classList.remove('active');
        this.toggleBtn.textContent = '💬';
    }

    addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message message-${sender}`;
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        contentDiv.textContent = text;
        
        messageDiv.appendChild(contentDiv);
        this.messagesContainer.appendChild(messageDiv);
        
        // Scroll to bottom
        this.messagesContainer.scrollTop = this.messagesContainer.scrollHeight;
    }

    showTyping() {
        this.typingIndicator.style.display = 'block';
        this.messagesContainer.scrollTop = this.messagesContainer.scrollHeight;
    }

    hideTyping() {
        this.typingIndicator.style.display = 'none';
    }

    async sendMessage() {
        const message = this.input.value.trim();
        if (!message || this.isTyping) return;

        // Add user message
        this.addMessage(message, 'user');
        this.input.value = '';
        
        // Show typing indicator
        this.isTyping = true;
        this.showTyping();
        this.sendBtn.disabled = true;
        
        try {
            // Send to backend
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });
            
            const data = await response.json();
            
            // Hide typing indicator
            this.hideTyping();
            
            if (data.status === 'success') {
                this.addMessage(data.response, 'ai');
            } else {
                this.addMessage('Sorry, I encountered an error. Please try again.', 'ai');
                console.error('Chatbot error:', data.error);
            }
        } catch (error) {
            this.hideTyping();
            this.addMessage('Sorry, I\'m having trouble connecting. Please try again.', 'ai');
            console.error('Network error:', error);
        } finally {
            this.isTyping = false;
            this.sendBtn.disabled = false;
            this.input.focus();
        }
    }
}

// Initialize chatbot when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.chatbot = new Chatbot();
});
