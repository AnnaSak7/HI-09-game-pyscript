const secondChallenge = document.querySelector(".second-challenge");
const guessedWord = document.getElementById("unknown-letters");
const secondChallengeInit = () => {
  secondChallenge.innerHTML += `
      <img src="../assets/makimono02.png" alt="challenge 2 instruction"/>
      <div id="input-btn-container">
        <input id="letter_input"></input>
        <button id="guess_letter_btn" class='enter-button' pys-onClick="on_click_letter">入力</button>
      </div>
      <div id="unknown-letters"></div>
      <div id='key'></div>
      <py-script src="../python/hangman.py"></py-script>
    `;
};

secondChallengeInit();
