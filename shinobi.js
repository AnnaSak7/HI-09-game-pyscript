const secondChallenge = document.querySelector(".second-challenge");

const secondChallengeInit = () => {
  secondChallenge.innerHTML += `
    <py-title>Hangman</py-title>
      <div id="shinobi">
        <div id="msg" style="color: #000"></div>
        <input id="letter_input"></input>
        <button id="guess_letter_btn" pys-onClick="on_click_letter">Click</button>
        <div id="response"></div>
      </div>
      <div id="unknown-letters"></div>
      <py-script src="hangman.py"></py-script>
    `;
};

secondChallengeInit();
