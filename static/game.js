let score = 0;
let total = 0;
let currentQuestion = null;

const elements = {
    loading: document.getElementById('loading'),
    gameArea: document.getElementById('game-area'),
    errorMessage: document.getElementById('error-message'),
    celebrityImage: document.getElementById('celebrity-image'),
    optionsContainer: document.getElementById('options-container'),
    feedback: document.getElementById('feedback'),
    feedbackText: document.getElementById('feedback-text'),
    nextButton: document.getElementById('next-button'),
    scoreDisplay: document.getElementById('score'),
    totalDisplay: document.getElementById('total')
};

function updateScore() {
    elements.scoreDisplay.textContent = score;
    elements.totalDisplay.textContent = total;
}

async function loadQuestion() {
    elements.loading.classList.remove('hidden');
    elements.gameArea.classList.add('hidden');
    elements.errorMessage.classList.add('hidden');
    elements.feedback.classList.add('hidden');
    
    try {
        const response = await fetch('/api/game/question');
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Failed to load question');
        }
        
        currentQuestion = await response.json();
        displayQuestion();
    } catch (error) {
        showError(error.message);
    }
}

function displayQuestion() {
    elements.loading.classList.add('hidden');
    elements.gameArea.classList.remove('hidden');
    
    elements.celebrityImage.src = currentQuestion.image_url;
    
    elements.optionsContainer.innerHTML = '';
    
    currentQuestion.options.forEach((option, index) => {
        const button = document.createElement('button');
        button.className = 'option-btn';
        button.textContent = option.label;
        button.onclick = () => handleAnswer(option, button);
        elements.optionsContainer.appendChild(button);
    });
}

function handleAnswer(selectedOption, buttonElement) {
    total++;
    
    const allButtons = elements.optionsContainer.querySelectorAll('.option-btn');
    allButtons.forEach(btn => btn.disabled = true);
    
    if (selectedOption.is_correct) {
        score++;
        buttonElement.classList.add('correct');
        elements.feedbackText.textContent = '🎉 Correct!';
        elements.feedback.className = 'feedback correct-answer';
    } else {
        buttonElement.classList.add('incorrect');
        
        allButtons.forEach(btn => {
            const optionText = btn.textContent;
            if (optionText === currentQuestion.correct_answer) {
                btn.classList.add('correct');
            }
        });
        
        elements.feedbackText.textContent = `❌ Wrong! The correct answer is: ${currentQuestion.correct_answer}`;
        elements.feedback.className = 'feedback wrong-answer';
    }
    
    updateScore();
    elements.feedback.classList.remove('hidden');
}

function showError(message) {
    elements.loading.classList.add('hidden');
    elements.gameArea.classList.add('hidden');
    elements.errorMessage.classList.remove('hidden');
    elements.errorMessage.textContent = message;
}

elements.nextButton.addEventListener('click', () => {
    loadQuestion();
});

loadQuestion();
