var tID; //we will use this variable to clear the setInterval()

function stopAnimate() {
  clearInterval(tID);
} //end of stopAnimate()


window.onload = function op_animateScript() {

  var position = 4 * 256; //start position for the image slicer
  const interval = 200; //100 ms of interval for the setInterval()
  const diff = 256; //diff as a variable for position offset

  tID = setInterval(() => {

    document.getElementById("op_image").style.backgroundPosition =
      `-${position}px 0px`;
    //we use the ES6 template literal to insert the variable "position"

    if (position < 5 * 256) {
      position = position + diff;
    }
    //we increment the position by 256 each time
    else {
      position = 4 * 256;
    }
    //reset the position to 256px, once position exceeds 1536px

  }, interval); //end of setInterval
} //end of animateScript()