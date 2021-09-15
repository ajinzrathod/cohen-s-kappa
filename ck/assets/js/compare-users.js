console.log("2. Jai Swaminarayan...")

let search_text_u1 = document.getElementById("user1")
let search_text_u2 = document.getElementById("user2")

search_text_u2.addEventListener('keyup', (event) => {
    var key = event.key;
    var code = event.code;
    console.log(`Key pressed ${key} \r\n Key code value: ${code}`);
    search_text_u2_keyup(key);
}, false);

search_text_u1.addEventListener('keyup', (event) => {
    var key = event.key;
    var code = event.code;
    console.log(`Key pressed ${key} \r\n Key code value: ${code}`);
    search_text_u1_keyup(key);
}, false);

document.getElementById("table-u1").addEventListener('blur', (event) => {
    document.getElementById("status_user1").style.display = "none"
});

document.getElementById("table-u1").addEventListener('focus', (event) => {
    document.getElementById("status_user1").style.display = ""
});

document.getElementById("table-u2").addEventListener('blur', (event) => {
    document.getElementById("status_user2").style.display = "none"
});

document.getElementById("table-u1").addEventListener('focus', (event) => {
    document.getElementById("status_user1").style.display = ""
});

function showUsersUsingXHR(txtIDtoRead, divIDtoDisplay, selected_user_status){
    console.log(">>>>>" + selected_user_status)
    // document.getElementById(divIDtoDisplay).innerHTML = "Searching...."
    user_to_search = document.getElementById(txtIDtoRead).value

    var xhr = new XMLHttpRequest()

    // Function on state change
    xhr.onreadystatechange = function () {
        console.log(xhr.readyState)
        console.log(xhr.responseText)

        // Handling <empty string> in JSON parse, else it will throw error in console
        if (xhr.responseText == null || xhr.responseText == ""){ }
        else{
            var xhrResponseJson = JSON.parse(xhr.responseText)
            var xhrResponseText = JSON.stringify(xhrResponseJson, null, 4)
            // document.getElementById(divIDtoDisplay).innerHTML = xhrResponseText
            if (xhr.readyState === 1)
                document.getElementById(divIDtoDisplay).innerHTML = "Searching."
            if (xhr.readyState === 2)
                document.getElementById(divIDtoDisplay).innerHTML = "Searching.."
            if (xhr.readyState === 3)
                document.getElementById(divIDtoDisplay).innerHTML = "Searching..."
        }

        // if status: 200
        if (xhr.readyState === 4 && xhr.status === 200) {
            var keyCount  = Object.keys(xhrResponseJson).length;
            console.log(keyCount)
            var textToRender = ""

            for(var i = 0; i < keyCount; i++){
                var userDetails = '\
                <tr class="clickable-row" onclick="selectUser( \
                this.id, \'' + selected_user_status +'\', \'' + divIDtoDisplay + '\') \
                " id="' + xhrResponseJson[i]['username'] + '"> \
                    <td class="cell"> \
                    <b>' + xhrResponseJson[i]['username'] + '</b> \
                    <span class="note">' + xhrResponseJson[i]['first_name'] + ' ' + xhrResponseJson[i]['last_name'] + '</span> \
                    </td> \
                </tr>'
                textToRender += userDetails
            }
            if(keyCount == 0){
                textToRender += '\
                <tr> \
                    <td class="cell"><span><b>No users found</b></span></td> \
                </tr>';
            }

            document.getElementById(divIDtoDisplay).innerHTML = textToRender
        }
    };
    //
    if (user_to_search){
        document.getElementById(divIDtoDisplay).style.display = ""
        var url = "/api/search-user/" + user_to_search + "/"
        xhr.open("POST", url, true)
        xhr.setRequestHeader("Content-Type", "application/json")
        xhr.setRequestHeader("X-CSRFToken", csrftoken)
        var data = JSON.stringify({});
        xhr.send(data);
    } 
    else {
        textToRender = ""
        document.getElementById(divIDtoDisplay).style.display = "none"
        document.getElementById(divIDtoDisplay).innerHTML = textToRender
    }
}

function search_text_u1_keyup(key){
    if(key === "Escape") {
        document.getElementById("status_user1").style.display = "none"
    }
    else{
        showUsersUsingXHR("user1", "status_user1", "selected_user1_status")
    }
}

function search_text_u2_keyup(key){
    if(key === "Escape") {
        document.getElementById("status_user2").style.display = "none"
    }
    else{
        showUsersUsingXHR("user2", "status_user2", "selected_user2_status")
    }
}


function selectUser(curr_row_id, selected_user_status, divIDtoDisplay){
    console.log(curr_row_id)
    console.log(selected_user_status)
    console.log(divIDtoDisplay)
    document.getElementById(selected_user_status).innerHTML = curr_row_id;
    document.getElementById(divIDtoDisplay).style.display = "none"
    console.log("User selected")

    enableCompareButton()
}

function enableCompareButton() {
    u1_name = document.getElementById("selected_user1_status").innerHTML
    u2_name = document.getElementById("selected_user2_status").innerHTML

    if (u1_name !== "-No user selected-" && u2_name !== "-No user selected-"){
        console.log("Enable Button")
        document.getElementById("compare-btn").disabled = false;
    }
    else{
        document.getElementById("compare-btn").disabled = true;
    }
}

document.getElementById("compare-btn").disabled = true;

let compare_button = document.getElementById("compare-btn")
compare_button.addEventListener('click', compare_button_click)

function compare_button_click(){
    document.getElementById("compare_status").innerHTML = "Please Wait.. This can take a while"
    var username1 = document.getElementById("selected_user1_status").innerHTML
    var username2 = document.getElementById("selected_user2_status").innerHTML

    console.log(username1)
    console.log(username2)

    var xhr = new XMLHttpRequest()

    // Function on state change
    xhr.onreadystatechange = function () {
        console.log(xhr.readyState)
        console.log(xhr.responseText)

        // Handling <empty string> in JSON parse, else it will throw error in console
        if (xhr.responseText == null || xhr.responseText == ""){ }
        else{
            var xhrResponseJson = JSON.parse(xhr.responseText)
            var xhrResponseText = JSON.stringify(xhrResponseJson, null, 4)
            document.getElementById("compare_status").innerHTML = xhrResponseText
        }

        // if status: 200
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById("tweet_id").innerHTML = curr_tweet_id
        }
    };

    var url = "/api/compare/" + username1 + "/" + username2 + "/" 
    xhr.open("GET", url, true)
    xhr.setRequestHeader("Content-Type", "application/json")
    xhr.setRequestHeader("X-CSRFToken", csrftoken)
    var data = JSON.stringify({});
    xhr.send(data);
}
