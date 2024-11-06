document.addEventListener('DOMContentLoaded', function() {
    const messagesContainer = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    const loadingIndicator = document.querySelector('.loading-indicator');

    function addMessage(content, isUser = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
        messageDiv.textContent = content;
        messagesContainer.appendChild(messageDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    function setLoading(isLoading) {
        console.log('Setting loading state:', isLoading);
        if (isLoading) {
            loadingIndicator.classList.remove('d-none');
            console.log('Loading indicator shown');
        } else {
            loadingIndicator.classList.add('d-none');
            console.log('Loading indicator hidden');
        }
        userInput.disabled = isLoading;
        sendButton.disabled = isLoading;
    }

    async function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;

        console.log('Sending message:', message);
        addMessage(message, true);
        userInput.value = '';

        setLoading(true);

        try {
            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt: message })
            });

            const data = await response.json();

            if (response.ok) {
                console.log('Response received:', data.response);
                addMessage(data.response);
            } else {
                console.error('Error:', data.error);
                addMessage('Error: ' + (data.error || 'Unknown error occurred'));
            }
        } catch (error) {
            console.error('Failed to communicate with server:', error);
            addMessage('Error: Failed to communicate with the server');
        } finally {
            setLoading(false);
        }
    }

    // Event listeners
    sendButton.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
});

