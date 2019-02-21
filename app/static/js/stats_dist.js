var total = 20
var value = {
    strength: 1,
    agility: 1,
    stamina: 1
}
function initValues(){
    document.getElementById("strength").value = value["strength"];
    document.getElementById("agility").value = value["agility"];
    document.getElementById("stamina").value = value["stamina"];
}

function increaseValue(id) {
  // var value = parseInt(document.getElementById('strength').value, 10);
  // value = 0;
  if(total<1){alert("Brak punktów do rozdania")}
  else{
    if(total>1){total--;value[id]++;}
    document.getElementById(id).value = value[id];
  }
  document.getElementById("total").innerHTML = total;
}

function decreaseValue(id) {
  // var value = parseInt(document.getElementById('strength').value, 10);
  // value = 0
    if(total>=20 || value[id]<=1){alert("Nic ująć ://")}
    else{
        if(total<20){total++;value[id]--;}
        document.getElementById(id).value = value[id];
    }
  document.getElementById("total").innerHTML = total;

}