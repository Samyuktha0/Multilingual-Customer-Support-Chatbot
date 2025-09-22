async function sendMessage() {
    const msg = document.getElementById('message').value;
    const lang = document.getElementById('lang').value;
    const res = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: msg, lang: lang })
    });
    const data = await res.json();
    document.getElementById('chatbox').innerHTML += `<p><b>You:</b> ${msg}</p><p><b>Bot:</b> ${data.response}</p>`;
    document.getElementById('message').value = '';
}
