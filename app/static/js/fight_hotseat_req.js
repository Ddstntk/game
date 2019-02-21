// function updateParams(data){
//     $("#playerHP").text(data["playerHP"]);
//     $("#playerSTA").text(data["playerSTA"]);
//     $("#opponentHP").text(data["opponentHP"]);
//     $("#opponentSTA").text(data["opponentSTA"]);
// }
var actionList = {
    "player": "xd",
    "opponent": "xd"
};

$('button.actionHs').attr("disabled", false);
$('button.actionHsO').attr("disabled", true);

$(function() {
        $('button.actionHs').bind('click', function(event) {
            sendThings("player", event.target.id);
          // $.getJSON('/fight_hotseat_do', {
          //   action: event.target.id
          // }, function(data) {
            $('button.actionHs').attr("disabled", true);
            $('button.actionHsO').attr("disabled", false);
          //   updateParams(data);
          //   staminaBar();
          //   healthBar();
          // });
          // return false;
        });
});

$(function() {
        $('button.actionHsO').bind('click', function(event) {
            sendThings("opponent", event.target.id);
          // $.getJSON('/fight_hotseat_do', {
          //   actionOpponent: event.target.id
          // }, function(data) {
            $('button.actionHs').attr("disabled", false);
            $('button.actionHsO').attr("disabled", true);
          //   updateParams(data);
          //   staminaBar();
          //   healthBar();
          //   kickAss(data["playerAction"], data["opponentAction"])
          // });
          // return false;
        });
});

function sendThings(player, id){
    actionList[player] = id;

    if(actionList["player"] !== 'xd' && actionList["opponent"] !== 'xd'){
        $.getJSON('/fight_hotseat_do', {
            action: actionList["player"],
            actionOpponent: actionList["opponent"]
          }, function(data) {
            // $('button.actionHs').attr("disabled", false);
            // $('button.actionHsO').attr("disabled", true);
            updateParams(data);
            staminaBar();
            healthBar();
            kickAss(data["playerAction"], data["opponentAction"])
            actionList = {}
          });
          return false;
    }
}