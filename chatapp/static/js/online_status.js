
let onlineLocation = window.location
let onlineWsStart = 'ws://'

let loggedinUser = JSON.parse(document.getElementById('json-message-username').textContent)

if (onlineLocation.protocol === 'https') {
    let onlineWsStart = 'wss://'
}

let onlineEndpoint = onlineWsStart + onlineLocation.host + '/online/' 

let onlineStatus = new WebSocket(onlineEndpoint)

onlineStatus.onopen = function (e) {
    console.log('online connection ',e);

    //sending logged user data to consumer
    onlineStatus.send(JSON.stringify({
        'username':loggedinUser,
        'type':'open'
    })) 
}

onlineStatus.onmessage = function(e) {
    console.log(e);
}

onlineStatus.onclose = function (e) {
    console.log('online connection lost ',e);
}