const container1 = document.querySelector(".part1");
const container2 = document.querySelector(".part2");
const imageContainer = document.querySelector(".image-container");

const createFirstChallengePart1 = () => {
  container1.innerHTML += `
        <h1 class="type">無限城</h1>
        <p>You have to figure out the pass code in order to get out this Mugen castle. Figure out the numbers that are written in Japanese to crack the code.</p>
        <div class="type">Type in a number between 1 - 9: </div>
        <div class="input">
        <input
          id="number-input-field"
          class="input-filed border flex item-center mr-3 border-grey-300 p-2"
          type="text"
        />
        <button
          means="enter"
          id="my-button"
          type="submit"
          pys-onClick="on_click_number"
        >
          入力
        </button>
      </div>
      <div id="number-output"></div>
    
        `;
};

// const createFirstChallengePart2 = () => {
//   container2.innerHTML += `
//   <h2>合言葉</h2>
//   <input id='password-input-field'
//   class="input-filed border flex item-center mr-3 border-grey-300 p-2"
//   type="text"
// />
// <button
// means="enter"
// id="my-button"
// type="submit"
// pys-onClick="on_click_password"
// >
// 入力
// </button>
// <div id="password-output"></div>
//   `;
// };

function getRndInteger(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

let imgNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8];

function shuffleArray(array) {
  let curId = array.length;
  // There remain elements to shuffle
  while (0 !== curId) {
    // Pick a remaining element
    let randId = Math.floor(Math.random() * curId);
    curId -= 1;
    // Swap it with the current element.
    let tmp = array[curId];
    array[curId] = array[randId];
    array[randId] = tmp;
  }
  return array;
}

// const pressedButton = (e) => {
//   e.classList.add("active");
// };

const pressedButton = () => {
  document.addEventListener("click", function handleClick(event) {
    if (event.target.classList.contains("active")) {
      event.target.classList.remove("active");
    } else {
      event.target.classList.add("active");
    }
  });
};
const kanjiNumbers = () => {
  let shuffledArray = shuffleArray(imgNumbers);

  for (let i = 0; i < imgNumbers.length; i++) {
    imageContainer.innerHTML += `
        <button
        class="numbers"
        onclick="pressedButton()"
        >
        <img
        id="${shuffledArray[i] + 1}"
        style="width: 200px; height: 200px"
        class="grid-img"
        src="./assets/0${shuffledArray[i]}.png"
        alt="${shuffledArray[i] + 1}"
        />
        </button>
        `;
  }
};

createFirstChallengePart1();
// createFirstChallengePart2();
kanjiNumbers();
