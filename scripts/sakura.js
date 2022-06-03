const thirdChallenge = document.querySelector(".third-challenge");
const modal = document.getElementById("modal");
const span = document.querySelector(".close");

const thirdChallengeInit = () => {
  thirdChallenge.innerHTML += `
        <img src="../assets/makimono03.png" alt="challenge 3 instruction"/>

        <div class='tobaku'>
            <p>よろしゅうござんすか？　入ります。</p>
            <p>さぁ、張った張った！！</p>
            <p>Click 丁 or 半</p>
        </div>

        <div class="cho-han-btns-container">
            <button class='chohanBtns' id="cho" pys-onClick="on_click_chohan">丁</button>
            <button class='chohanBtns' id="han" pys-onClick="on_click_chohan">半</button>
        </div>

        <div id="modal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <div id='modal-content'></div>
        </div>
    `;

  document.getElementById("cho").addEventListener("click", btnPressed);
  document.getElementById("han").addEventListener("click", btnPressed);
};

const btnPressed = (e) => {
  e.target.classList.toggle("pushed");
  document.getElementById("modal").style.display = "block";

  document.getElementById("modal-content").innerHTML == "半"
    ? document.getElementById("soundHan").play()
    : document.getElementById("soundCho").play();
};

thirdChallengeInit();

document.querySelector(".close").onclick = () => {
  document.getElementById("modal").style.display = "none";
  document.getElementById("cho").classList.contains("pushed")
    ? document.getElementById("cho").classList.toggle("pushed")
    : document.getElementById("han").classList.toggle("pushed");
};
