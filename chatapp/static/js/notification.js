let notificationLocation = window.location
let notificationStart = 'ws://'

if (notificationLocation.protocol === 'https'){
    notificationStart = 'wss://'
}

let notificationEndpoint = notificationStart + notificationLocation.host + '/notification/'

notificationSocket = new WebSocket(notificationEndpoint)

notificationSocket.onopen = function(e){
    console.log('Notification connection',e);

}

notificationSocket.onclose = function(e){
    console.log('Notification disconnected',e)
}