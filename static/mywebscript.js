function RunSentimentAnalysis() {
    let textToAnalyze = document.getElementById("textToAnalyze").value;
    // Verificar si el campo está vacío
    if (!textToAnalyze) {
        document.getElementById("system_response").innerHTML = "Invalid text! Please try again!";
        return; // Salir de la función si el texto es inválido
    }

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let response = JSON.parse(this.responseText);
            document.getElementById("system_response").innerHTML = `
                Dominant Emotion: ${response.dominant_emotion}
                <br>
                Full Response: ${JSON.stringify(response)}
            `;
        } else if (this.readyState == 4 && this.status !== 200) {
            // Manejar errores del servidor
            document.getElementById("system_response").innerHTML = "Error: " + this.responseText;
        }
    };
    xhttp.open("GET", "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
}
