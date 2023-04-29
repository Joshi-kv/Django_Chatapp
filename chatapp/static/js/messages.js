let loc = window.location
let wsStart = 'ws://'
let id = JSON.parse(document.getElementById('json-username').textContent)
let sender = JSON.parse(document.getElementById('json-message-username').textContent)

if (loc.protocol === 'https') {
    let wsStart = 'wss://'
}

let endpoint = wsStart + loc.host + '/chat/' + id + '/'
console.log(endpoint);

let chatBody = document.getElementById('chat-body')



//creating object for websocket

let socket = new WebSocket(endpoint)

let messageInput = $('#message')
let messageForm = $('#message-form')


socket.onopen = async function(e){
    console.log('On open',e)
    messageForm.submit((e)=>{
        e.preventDefault()
        let message = messageInput.val()
        let data = {
            'message':message,
            'sender':sender
        }

        //converting json object to json string
        data = JSON.stringify(data)
        //sending message to backend
        socket.send(data)
        messageForm[0].reset()
        chatBody.scrollTop = chatBody.scrollHeight
    })
}

socket.onmessage = async (e)=>{
    console.log('On message',e)
    let data = JSON.parse(e.data)
    const message = data['message']
    
    //appending message received from backend

    if(data['sender'] == sender){
        chatBody.innerHTML += `
        
        <div class="chat-box-sent">
            ${message}
        </div>
        `
    }else{

        chatBody.innerHTML += `
        
        <div class="chat-box-received">
            ${message}
        </div>
        
        `
    }
    chatBody.scrollTop = chatBody.scrollHeight

}

socket.onerror = async (e)=>{
    console.log('On error',e)
}

socket.onclose = async (e)=>{
    console.log('On close',e)
}

window.onload = function() {
    chatBody.scrollTop = chatBody.scrollHeight
}