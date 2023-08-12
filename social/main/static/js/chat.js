document.addEventListener("DOMContentLoaded", function () {
    const messageInput = document.getElementById("message-input");
    const sendButton = document.getElementById("send-button");
    const chatBox = document.querySelector(".chat-box");

    sendButton.addEventListener("click", function () {
        const messageContent = messageInput.value.trim();
        if (messageContent !== "") {
            const messageElement = document.createElement("div");
            messageElement.classList.add("message");
            messageElement.innerHTML = `<div class="message-content">${messageContent}</div>`;
            chatBox.appendChild(messageElement);
            messageInput.value = "";
        }
    });

    messageInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            sendButton.click();
            event.preventDefault();
        }
    });
});
