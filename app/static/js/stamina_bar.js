function staminaBar(){
  var sBar_p = $('.stamina-bar-pla'),
      sBar_o = $('.stamina-bar-opp'),
      sta_bar_pla = sBar_p.find('.sta-bar'),
      sta_hit_pla = sBar_p.find('.sta-hit'),
      sta_bar_opp = sBar_o.find('.sta-bar'),
      sta_hit_opp = sBar_o.find('.sta-hit');

    var total_pla = sBar_p.data('total'),
        value_pla = sBar_p.data('value'),
        total_opp = sBar_o.data('total'),
        value_opp = sBar_o.data('value');

    if (value_pla < 0 || value_opp < 0) {
      return;
    }

    var newValue_p = $("#playerSTA").text();
    var damage_p = value_pla - newValue_p;
    var newValue_o = $("#opponentSTA").text();
    var damage_o = value_opp - newValue_o;

    var barWidth_p = (newValue_p / total_pla) * 100;
    var hitWidth_p = (damage_p / value_pla) * 100 + "%";
    var barWidth_o = (newValue_o / total_opp) * 100;
    var hitWidth_o = (damage_o / value_opp) * 100 + "%";

    sta_hit_pla.css('width', hitWidth_p);
    sBar_p.data('value', newValue_p);
    sta_hit_opp.css('width', hitWidth_o);
    sBar_o.data('value', newValue_o);

    setTimeout(function(){
      sta_hit_pla.css({'width': '0'});
      sta_bar_pla.css('width', barWidth_p + "%");
      sta_hit_opp.css({'width': '0'});
      sta_bar_opp.css('width', barWidth_o + "%");
    }, 500);
};
