// var actionList = {
//     "player": "xd",
//     "opponent": "xd"
// };
//
// $(document).ready(function() {
//             // Use a "/test" namespace.
//             // An application can open a connection on multiple namespaces, and
//             // Socket.IO will multiplex all those connections on a single
//             // physical channel. If you don't care about multiple channels, you
//             // can set the namespace to an empty string.
//             namespace = '/test';
//
//             // Connect to the Socket.IO server.
//             // The connection URL has the following format:
//             //     http[s]://<domain>:<port>[/<namespace>]
//             var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);
//
//             // Event handler for new connections.
//             // The callback function is invoked when a connection with the
//             // server is established.
//             socket.on('connect', function() {
//                 socket.emit('my_event', {data: 'I\'m connected!'});
//             });
//
//             // Event handler for server sent data.
//             // The callback function is invoked whenever the server emits data
//             // to the client. The data is then displayed in the "Received"
//             // section of the page.
//             socket.on('my_response', function(msg) {
//                 // alert("HAHAH");
//                 $('#log').append('<br>' + $('<div/>').text('Received #' + msg.count + ': ' + msg.data).html());
//             });
//
//             // Interval function that tests message latency by sending a "ping"
//             // message. The server then responds with a "pong" message and the
//             // round trip time is measured.
//             // var ping_pong_times = [];
//             // var start_time;
//             // window.setInterval(function() {
//             //     start_time = (new Date).getTime();
//             //     socket.emit('my_ping');
//             // }, 1000);
//
//             // Handler for the "pong" message. When the pong is received, the
//             // time from the ping is stored, and the average of the last 30
//             // samples is average and displayed.
//             // socket.on('my_pong', function() {
//             //     var latency = (new Date).getTime() - start_time;
//             //     ping_pong_times.push(latency);
//             //     ping_pong_times = ping_pong_times.slice(-30); // keep last 30 samples
//             //     var sum = 0;
//             //     for (var i = 0; i < ping_pong_times.length; i++)
//             //         sum += ping_pong_times[i];
//             //     $('#ping-pong').text(Math.round(10 * sum / ping_pong_times.length) / 10);
//             // });
//
//             // Handlers for the different forms in the page.
//             // These accept data from the user and send it to the server in a
//             // variety of ways
//             $('form#emit').submit(function(event) {
//                 socket.emit('my_event', {data: $('#emit_data').val()});
//                 return false;
//             });
//             $('form#broadcast').submit(function(event) {
//                 socket.emit('my_broadcast_event', {data: $('#broadcast_data').val()});
//                 return false;
//             });
//             $('form#join').submit(function(event) {
//                 socket.emit('join', {room: $('#join_room').val()});
//                 return false;
//             });
//             $('form#leave').submit(function(event) {
//                 socket.emit('leave', {room: $('#leave_room').val()});
//                 return false;
//             });
//             $('form#send_room').submit(function(event) {
//                 socket.emit('my_room_event', {room: $('#join_room').val(), data: $(this).val()});
//                 return false;
//             });
//             $('button[name=HS]').click(function(event) {
//                 socket.emit('my_room_event', {room: $('#join_room').val(), data: $(this).val()});
//                 return false;
//             });
//             $('form#close').submit(function(event) {
//                 socket.emit('close_room', {room: $('#close_room').val()});
//                 return false;
//             });
//             $('form#disconnect').submit(function(event) {
//                 socket.emit('disconnect_request');
//                 return false;
//             });
//         });
//
//
// var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);
//
//  function createGame() {
//       console.log('Creating game...');
//       socket.emit('create', {});
//  }
//
//     function sendIdleMsg() {
//         alert("lol");
//         socket.emit('my_room_event', {room: $('#join_room').val(), data: "czekam"});
//     }
//
//     function sendThingsWeb(player, id){
//     actionList[player] = id;
//
//     if(actionList["player"] !== 'xd' && actionList["opponent"] !== 'xd'){
//         $.getJSON('/fight_hotseat_do', {
//             action: actionList["player"],
//             actionOpponent: actionList["opponent"]
//           }, function(data) {
//             // $('button.actionHs').attr("disabled", false);
//             // $('button.actionHsO').attr("disabled", true);
//             updateParams(data);
//             staminaBar();
//             healthBar();
//             kickAss(data["playerAction"], data["opponentAction"])
//             actionList = {}
//           });
//           return false;
//     }
// }

 var socket = io.connect('http://' + document.domain + ':' + location.port);
    // verify our websocket connection is established
    socket.on('connect', function() {
        console.log('Websocket connected!');
    });
    // message handler for the 'join_room' channel
    socket.on('join_room', function(msg) {
        console.log(msg);
    });
    // createGame onclick - emit a message on the 'create' channel to
    // create a new game with default parameters
    function createGame() {
      var roomName = $('#create_room').val();
      alert(roomName)
      console.log('Creating game...');
      socket.emit('create', {name: $('#create_room').val(), size: 'normal', teams: 2, dictionary: 'Simple'});
    }

    function joinGame() {
      var roomName = $('#join_room').val();
      alert(roomName)
      console.log('Creating game...');
      socket.emit('join', {room: $('#join_room').val()});
    }