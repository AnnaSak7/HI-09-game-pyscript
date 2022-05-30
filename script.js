const containerH1 = document.querySelector(".title");

const createFirstPage = () => {
  containerH1.innerHTML += `
        <h1 class="type">Japan</h1>
        <div class="type">Put in the password: </div>
        <div class="input">
        <input
          id="my-input-field"
          class="input-filed border flex item-center mr-3 border-grey-300 p-2"
          type="text"
        />
        <button
          means="enter"
          id="my-button"
          type="submit"
          pys-onClick="on_click"
        >
          入力
        </button>
      </div>
      <div id="my-output"></div>
    
        `;
};

createFirstPage();
