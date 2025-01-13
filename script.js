document.addEventListener('DOMContentLoaded', () => {
    fetch('formatted_chat.json')
        .then(response => response.json())
        .then(data => {
            const chatContainer = document.getElementById('chat-container');
            data.forEach(chat => {
                const chatMessage = document.createElement('div');
                chatMessage.classList.add('chat-message');

                const message = document.createElement('span');
                message.classList.add('message');
                message.innerHTML = `<strong>${chat.username}:</strong> ${chat.message}`;

                chatMessage.appendChild(message);
                chatContainer.appendChild(chatMessage);
            });
        })
        .catch(error => console.error('Error fetching chat data:', error));
});
