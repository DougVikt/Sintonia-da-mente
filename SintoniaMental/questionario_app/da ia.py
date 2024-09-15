<!-- quiz.html -->
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulário de Perguntas</title>
    <style>
        .question {
            display: none;
        }
        .question.active {
            display: block;
        }
    </style>
</head>
<body>
    <form id="quizForm">
        <div id="questionContainer" class="question active"></div>
        <button type="button" id="prevButton" onclick="prevQuestion()" style="display: none;">Voltar</button>
        <button type="button" id="nextButton" onclick="nextQuestion()">Próxima</button>
        <button type="submit" id="submitButton" style="display: none;">Enviar</button>
    </form>

    <script>
        const questions = [
            {% for question in questions %}
                "{{ question.text }}",
            {% endfor %}
        ];

        let currentQuestion = 0;

        function loadQuestion() {
            const questionContainer = document.getElementById('questionContainer');
            questionContainer.innerHTML = `
                <p>${questions[currentQuestion]}</p>
                <input type="radio" name="q${currentQuestion + 1}" value="A"> A<br>
                <input type="radio" name="q${currentQuestion + 1}" value="B"> B<br>
                <input type="radio" name="q${currentQuestion + 1}" value="C"> C<br>
                <input type="radio" name="q${currentQuestion + 1}" value="D"> D<br>
                <input type="radio" name="q${currentQuestion + 1}" value="E"> E<br>
                <input type="radio" name="q${currentQuestion + 1}" value="F"> F<br>
            `;

            document.getElementById('prevButton').style.display = currentQuestion > 0 ? 'inline' : 'none';
            document.getElementById('nextButton').style.display = currentQuestion < questions.length - 1 ? 'inline' : 'none';
            document.getElementById('submitButton').style.display = currentQuestion === questions.length - 1 ? 'inline' : 'none';
        }

        function nextQuestion() {
            if (currentQuestion < questions.length - 1) {
                currentQuestion++;
                loadQuestion();
            }
        }

        function prevQuestion() {
            if (currentQuestion > 0) {
                currentQuestion--;
                loadQuestion();
            }
        }

        loadQuestion();
    </script>
</body>
</html>
