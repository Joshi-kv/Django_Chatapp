let loc = window.location
let wsStart = 'ws://'
let id = JSON.parse(document.getElementById('json-username').textContent)
let senderId = JSON.parse(document.getElementById('json-message-username').textContent)

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
    // messageForm.submit((e)=>{
    //     e.preventDefault()
    //     let msg = messageInput.val()
    //     let data = {
    //         'message':msg
    //     }

    //     //converting json object to json string
    //     data = JSON.stringify(data)
    //     //sending message to backend
    //     socket.send(data)
    //     messageForm[0].reset()
    // })
}

socket.onmessage = async (e)=>{
    console.log('On message',e)
    let data = JSON.parse(e.data)
    let message = data['message']
    let messageDiv = document.createElement('div')
    messageDiv.classList.add('chat-box-sent')
    messageDiv.innerText = message
    chatBody.append(messageDiv)

}

socket.onerror = async (e)=>{
    console.log('On error',e)
}

socket.onclose = async (e)=>{
    console.log('On close',e)
}