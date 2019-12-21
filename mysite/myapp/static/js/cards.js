let matchesCorrect = 0;
let matchesIncorrect = 0;
let firstCard = null;
let secondCard = null;
let curCardsRotated = 0;

const boxes = document.querySelectorAll('.card_box');
const in_play = document.getElementById("play");
const complete = document.getElementById("finished");
boxes.forEach(box => box.addEventListener('click', cardRotate));

function cardRotate() {
    if (curCardsRotated < 2) {
        if (this === firstCard) {
            return;
        }

        this.classList.add('rotate');
        curCardsRotated++;

        if (curCardsRotated === 1) {
            firstCard = this;
            return;
        }

        secondCard = this;
        curCardsRotated++;

        if (firstCard.dataset.card === secondCard.dataset.card) {
            matchesCorrect++;
            console.log("Matches Correct: ", matchesCorrect);
            document.getElementById("correct").innerHTML = "Matches correct: " + matchesCorrect + "\n";

            curCardsRotated = 0;
            firstCard = null;
            secondCard = null;

            if (matchesCorrect === 10) {
                document.getElementById("results").innerHTML += "Finished! Guesses made correctly: " + Math.ceil((matchesCorrect / (matchesCorrect + matchesIncorrect)) * 100) + "%\n";
                in_play.classList.toggle('hidden');
                complete.classList.toggle('hidden');
            }
        } else {
            matchesIncorrect++;
            console.log("Matches Incorrect: ", matchesIncorrect);
            document.getElementById("incorrect").innerHTML = "Matches incorrect: " + matchesIncorrect + "\n";

            setTimeout(() => {
                firstCard.classList.remove('rotate');
                secondCard.classList.remove('rotate');

                curCardsRotated = 0;
                firstCard = null;
                secondCard = null;
            }, 1200);
        }
    } else {
        return;
    }
}

/* Self-executing anonymous function */
(function shuffle_boxes() {
    boxes.forEach(box => box.style.order = Math.floor(Math.random() * 20));
})();
