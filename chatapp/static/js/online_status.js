
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
        let onlineCaption = document.getElementById(`${data.username}-caption`)

        if(data.online_status == true){
            onlineImage.classList.remove('offline')
            onlineCaption.classList.remove('offline-caption')
            onlineImage.classList.add('online')
            onlineCaption.classList.add('online-caption')

        }else{
            onlineImage.classList.remove('online')
            onlineCaption.classList.remove('online-caption')
            onlineImage.classList.add('offline')
            onlineCaption.classList.add('offline-caption')
        }
       
    }

}

onlineStatus.onclose = function (e) {
    console.log('online connection lost ',e);
}