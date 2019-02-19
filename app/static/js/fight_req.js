function updateParams(data){
    $("#playerHP").text(data["playerHP"]);
    $("#playerSTA").text(data["playerSTA"]);
    $("#opponentHP").text(data["opponentHP"]);
    $("#opponentSTA").text(data["opponentSTA"]);
}

$(function() {
        $('button.action').bind('click', function(event) {
          $.getJSON('/fight_do', {
            action: event.target.id
          }, function(data) {
            updateParams(data);
            staminaBar();
            healthBar();
            kickAss(data["playerAction"], data["opponentAction"])
          });
          return false;
        });
});
