let loc = window.location
let wsStart = 'ws://'

if (loc.protocol === 'https') {
    let wsStart = 'wss://'
}

let endpoint = wsStart + loc.host + loc.pathname

//creating object for websocket

let socket = new WebSocket(endpoint)


socket.onopen = async (e)=>{
    console.log('On open',e)
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