async function analyzeSentiment() {
    const text = document.getElementById("inputText").value;
    const resultDiv = document.getElementById("result");

    if (!text.trim()) {
        resultDiv.innerText = "Please enter some text.";
        return;
    }

    try {
        const response = await fetch("http://localhost:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text })
        });

        const data = await response.json();

        if (response.ok) {
            resultDiv.innerText = `Sentiment: ${data.sentiment}`;
        } else {
            resultDiv.innerText = data.error || "Error analysing sentiment";
        }
    } catch (error) {
        resultDiv.innerText = "Unable to connect to backend API.";
    }
}

