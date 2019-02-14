var tID; //we will use this variable to clear the setInterval()

function stopAnimate() {
  clearInterval(tID);
} //end of stopAnimate()


window.onload = function animateScript(){
  idleAnimation();
};

 function idleAnimation() {
  clearInterval(tID);
  var position = 3 * 256; //start position for the image slicer
  const interval = 300; //100 ms of interval for the setInterval()
  const diff = 256; //diff as a variable for position offset
  var player = document.getElementById("image");
  var opponent = document.getElementById("op_image");

  tID = setInterval(() => {

    opponent.style.backgroundPosition = player.style.backgroundPosition =
      `-${position}px 0px`;

    if (position < 5 * 256) {
      position = position + diff;
    }
    else {
      position = 4 * 256;
    }

  }, interval);
}


function delayAnim(tionA, actionB, milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
    actionB();
}


function kickAss(actionPlayer, actionOpponent) {
  clearInterval(tID);
  if(actionPlayer == "strong" || actionPlayer == "guick"){
    if(actionOpponent == "strong" || actionOpponent == "quick"){
      window[actionPlayer + "Animation"]("image")
      delayAnim(window[actionOpponent + "Animation"]("op_image"))
    }
    else if(actionOpponent == "defend" || actionOpponent == "dodge"){
      window[actionPlayer + "Animation"]("image")
      window[actionOpponent + "Animation"]("op_image")
    }
    else if(actionOpponent == "rest"){
      window[actionPlayer + "Animation"]("image")
      delayAnim(window[actionOpponent + "Animation"]("op_image"))
    }
  }
  else if(actionPlayer == "defend" || actionPlayer == "dodge") {
    window[actionOpponent + "Animation"]("op_image")
    window[actionPlayer + "Animation"]("image")
  }
  else if(actionPlayer == "rest"){
    if(actionOpponent == "strong" || actionOpponent == "quick"){
      window[actionOpponent + "Animation"]("op_image")
      delayAnim(window[actionPlayer + "Animation"]("image"))
    }
    else {
      window[actionOpponent + "Animation"]("op_image")
      window[actionPlayer + "Animation"]("image")
    }
  }
  clearInterval(tID);
  idleAnimation();
}

function strongAnimation(id){
  clearInterval(tID);
  var position = 9 * 256; //start position for the image slicer
  const interval = 200; //100 ms of interval for the setInterval()
  const diff = 256; //diff as a variable for position offset
  var player = document.getElementById(id);

  tID = setInterval(() => {
    player.style.backgroundPosition =
      `-${position}px -1280px`;

    if (position < 11 * 256) {
      position = position + diff;
    }
    else {
      clearInterval(tID);
      idleAnimation();
    }
  }, interval);
}

function quickAnimation(id){
  clearInterval(tID);
  var position = 0 * 256; //start position for the image slicer
  const interval = 200; //100 ms of interval for the setInterval()
  const diff = 256; //diff as a variable for position offset
  var player = document.getElementById(id);

  tID = setInterval(() => {
    player.style.backgroundPosition =
      `-${position}px -1024px`;

    if (position < 3 * 256) {
      position = position + diff;
    }
    else {
      clearInterval(tID);
      idleAnimation();
    }
  }, interval);
}
function defendAnimation(id){
  clearInterval(tID);
  var position = 9 * 256; //start position for the image slicer
  const interval = 150; //100 ms of interval for the setInterval()
  const diff = 256; //diff as a variable for position offset
  var player = document.getElementById(id);

  tID = setInterval(() => {
    player.style.backgroundPosition =
      `-${position}px -1024px`;

    if (position < 12 * 256) {
      position = position + diff;
    }
    else {
      clearInterval(tID);
      idleAnimation();
    }
  }, interval);
}
function dodgeAnimation(id){
  clearInterval(tID);
  var position = 14 * 256; //start position for the image slicer
  const interval = 50; //100 ms of interval for the setInterval()
  const diff = 256; //diff as a variable for position offset
  var player = document.getElementById(id);

  tID = setInterval(() => {
    player.style.backgroundPosition =
      `-${position}px 0px`;

    if (position < 15 * 256) {
      position = position + diff;
    }
    else {
      clearInterval(tID);
      idleAnimation();
    }
  }, interval);
}
function restAnimation(id){
  clearInterval(tID);
  var position = 17 * 256; //start position for the image slicer
  const interval = 300; //100 ms of interval for the setInterval()
  const diff = 256; //diff as a variable for position offset
  var player = document.getElementById(id);
  var i = 0;

  tID = setInterval(() => {
    player.style.backgroundPosition =
      `-${position}px 0px`;

    if (i<3) {
      i++;
    }
    else {
      clearInterval(tID);
      idleAnimation();
    }
  }, interval);
}
function dieAnimation(id){
   clearInterval(tID);
  var position = 9 * 256; //start position for the image slicer
  const interval = 300; //100 ms of interval for the setInterval()
  const diff = 256; //diff as a variable for position offset
  var player = document.getElementById(id);
  var i = 0;

  tID = setInterval(() => {
    player.style.backgroundPosition =
      `-${position}px -768px`;
    position = position + diff;


    if (i<2) {
      i++;
    }
    else {
      player.style.backgroundPosition =
      `-${7*256}px -768px`;
      clearInterval(tID);
    }
  }, interval);
}
function cheerAnimation(id){
  clearInterval(tID);
  var position = 0 * 256; //start position for the image slicer
  const interval = 200; //100 ms of interval for the setInterval()
  const diff = 256; //diff as a variable for position offset
  var player = document.getElementById(id);

  tID = setInterval(() => {
    player.style.backgroundPosition =
      `-${position}px -1280px`;

    if (position < 2 * 256) {
      position = position + diff;
    }
    else {
      clearInterval(tID);
    }
  }, interval);
}
