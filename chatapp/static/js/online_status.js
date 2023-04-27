
let onlineLocation = window.location
let onlineWsStart = 'ws://'

let loggedinUser = JSON.parse(document.getElementById('json-message-username').textContent)
let otherUsername = JSON.parse(document.getElementById('json-other-username').textContent)

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

window.addEventListener('beforeunload',function(e){
    onlineStatus.send(JSON.stringify({
        'username' : loggedinUser,
        'type' : 'offline'
    }))
})

onlineStatus.onmessage = function(e) {
    console.log(e);
    let data = JSON.parse(e.data)
    if(data.username !== loggedinUser){
        let onlineImage = document.getElementById(`${data.username}-image`)
        console.log(onlineImage)
    }

}

onlineStatus.onclose = function (e) {
    console.log('online connection lost ',e);
}