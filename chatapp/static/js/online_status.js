
let onlineLocation = window.location
let onlineWsStart = 'ws://'
// let id = JSON.parse(document.getElementById('json-username').textContent)
// let sender = JSON.parse(document.getElementById('json-message-username').textContent)

if (onlineLocation.protocol === 'https') {
    let onlineWsStart = 'wss://'
}

let onlineEndpoint = onlineWsStart + onlineLocation.host + '/online/' 

let onlineSocket = new WebSocket(onlineEndpoint)

onlineSocket.onopen = function (e) {
    console.log('online connection ',e);
}

onlineSocket.onclose = function (e) {
    console.log('online connection lost ',e);
}