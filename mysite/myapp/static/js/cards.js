let matchesCorrect = 0;
let matchesIncorrect = 0;
let firstCard = null;
let secondCard = null;
let cardsFlipped = 0;

const cards = document.querySelectorAll('.memory-card');
cards.forEach(card => card.addEventListener('click', flipCard));

function flipCard() {
    if (cardsFlipped < 2) {
        if (this === firstCard) {
            return;
        }

        this.classList.add('flip');
        cardsFlipped++;

        if (cardsFlipped === 1) {
            firstCard = this;
            return;
        }

        secondCard = this;
        cardsFlipped++;

        if (firstCard.dataset.framework === secondCard.dataset.framework) {
            matchesCorrect++;
            console.log("Matches Correct: ", matchesCorrect);
            document.getElementById("correct").innerHTML = "Matches correct: " + matchesCorrect + "\n";

            firstCard.removeEventListener('click', flipCard);
            secondCard.removeEventListener('click', flipCard);

            cardsFlipped = 0;
            firstCard = null;
            secondCard = null;

            if (matchesCorrect === 10) {
                document.getElementById("results").innerHTML += "Guesses made correctly: " + Math.ceil((matchesCorrect / (matchesCorrect + matchesIncorrect)) * 100) + "%\n";
            }
        } else {
            matchesIncorrect++;
            console.log("Matches Incorrect: ", matchesIncorrect);
            document.getElementById("incorrect").innerHTML = "Matches incorrect: " + matchesIncorrect + "\n";

            setTimeout(() => {
                firstCard.classList.remove('flip');
                secondCard.classList.remove('flip');

                cardsFlipped = 0;
                firstCard = null;
                secondCard = null;
            }, 1500);
        }
    } else {
        return;
    }
}

/* Self-executing anonymous function */
(function shuffle() {
    cards.forEach(card => card.style.order = Math.floor(Math.random() * 20));
})();
