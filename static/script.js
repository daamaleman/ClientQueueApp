let recognition;
let isRecording = false;

function startRecording() {
    if (!('webkitSpeechRecognition' in window)) {
        alert("Tu navegador no soporta reconocimiento de voz");
        return;
    }

    recognition = new webkitSpeechRecognition();
    recognition.lang = "es-ES";
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onresult = function(event) {
        const text = event.results[0][0].transcript;
        document.getElementById("recognizedText").value = text;
        fetch('/add_name', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name: text })
        }).then(res => res.json())
          .then(data => updateQueue(data.queue));
    };

    recognition.start();
    isRecording = true;
}

function stopRecording() {
    if (recognition && isRecording) {
        recognition.stop();
        isRecording = false;
    }
}

function updateQueue(queue) {
    const list = document.getElementById('queueList');
    list.innerHTML = '';
    queue.forEach(name => {
        const li = document.createElement('li');
        li.textContent = name;
        list.appendChild(li);
    });
}