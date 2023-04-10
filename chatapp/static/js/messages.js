let loc = window.location
let wsStart = 'ws://'

if (loc.protocol === 'https') {
    let wsStart = 'wss://'
}

let endpoint = wsStart + loc.host + loc.pathname

//creating object for websocket

let socket = new WebSocket(endpoint)

let messageInput = $('#message')
let messageForm = $('#message-form')

socket.onopen = async function(e){
    console.log('On open',e)
    messageForm.submit((e)=>{
        e.preventDefault()
        let msg = messageInput.val()
        let data = {
            'message':msg
        }
        data = JSON.stringify(data)
        //sending message to backend
        socket.send(data)
        messageForm[0].reset()
    })
}

socket.onmessage = async (e)=>{
    console.log('On message',e)
}

socket.onerror = async (e)=>{
    console.log('On error',e)
}

socket.onclose = async (e)=>{
    console.log('On close',e)
}