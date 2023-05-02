let notificationLocation = window.location
let notificationStart = 'ws://'
let currentUser = JSON.parse(document.getElementById('json-message-username').textContent)

if (notificationLocation.protocol === 'https'){
    notificationStart = 'wss://'
}

let notificationEndpoint = notificationStart + notificationLocation.host + '/notification/'

notificationSocket = new WebSocket(notificationEndpoint)

notificationSocket.onopen = function(e){
    console.log('Notification connection',e);

}

notificationSocket.onmessage = function(e){
    data = JSON.parse(e.data)
    console.log(data);

    if(data.sender !== currentUser){
        let bellIcon = document.getElementById(`${data.sender}-bell`)
        let count = document.getElementById(`${data.sender}-count`)

        if(data.seen == false){
            bellIcon.classList.add('fa-shake')
            count.innerHTML=`${data.notification_count}`
        }else{
            bellIcon.classList.remove('fa-shake')
            count.style.display='none'
        }
    }


    
}

notificationSocket.onclose = function(e){
    console.log('Notification disconnected',e)
}