/*
console.log(window.location)
var wsStart = 'ws://'
var endpoint = wsStart + window.location.host + window.location.pathname
console.log(endpoint)
//var socket = new WebSocket(endpoint)
var socket = new ReconnectingWebSocket(endpoint)

//Preventing default form action
var formData = $("#form")

//Django renders form using this id (obtained from inspecting the element)
var msgIn = $("#id_input")

//For displaying the message that comes through from the data in the back-end
var chatHolder = $("#chat-items")

//Bring username in
var me = $("#myUsername").val()

//Websocket events; related to how consumer handles any event
//Client-side websocket received a message
socket.onmessage = function(e) {
    console.log("CHECK----------------")
    //console.log("message", e)
    //console.log(e.data)
    //Console log
    //console.log(e.data)
    //Appending chat messages
    //chatHolder.append("<tr>" + message + "</tr>")

    //Grabbing the message //---------------------------------
    var chatDataMsg = JSON.parse(e.data) //--------------------------------- Python equivalent of "loads"
    //chatHolder.append("<br>" + chatDataMsg.username + ": " + chatDataMsg.message)

    //chatHolder.append("<br>" + chatDataMsg.username + ": " + chatDataMsg.message)
    //<li>{{ input_message.author.username }}: {{ input_message.input }}</li>
    chatHolder.append("<li>" + chatDataMsg.username + ": " + chatDataMsg.message + "</li>")
    
}

//Message the client is sending
socket.onopen = function(e) {
    console.log("open", e)

    formData.submit(function(event){
        //Prevents form from being submitted by default
        event.preventDefault()

        //Send data to backend
        //socket.send("hello world")

        //Grab message data from form
        var msg = msgIn.val()
        //Send message text back
        //socket.send(msg)

        //Send the intial message - actual echoing
        ///////////////chatHolder.append("<br>" + me + ": " + msg)

        //var formDataSerialized = formData.serialize() //Not ideal, just use the message text
        //socket.send(formDataSerialized)

        //Send a dictionary back //---------------------------------
        var finalData = {
            'message':msg
        }
        socket.send(JSON.stringify(finalData)) //Turn into JSON data in order to send,
        //especially if it's a dictionary

        //Clear the form
        //
        //The line below also works, but you want to use the latter in
        //case you have other fields in your form
        //msgIn.val('')
        formData[0].reset()
    })
}

socket.onerror = function(e) {
    console.log("error", e)
}

socket.onclose = function(e) {
    console.log("close", e)
}
*/
