function updateParams(data){
    $("#playerHP").text(data["playerHP"]);
    $("#playerSTA").text(data["playerSTA"]);
    $("#opponentHP").text(data["opponentHP"]);
    $("#opponentSTA").text(data["opponentSTA"]);
}

$(function() {
        $('button.action').bind('click', function() {
          $.getJSON('/fight_do', {
            action: event.target.id
          }, function(data) {
            updateParams(data);
            staminaBar();
            healthBar();
          });
          return false;
        });
});
