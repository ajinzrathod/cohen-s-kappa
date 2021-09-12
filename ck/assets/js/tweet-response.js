console.log("Jai Swaminarayan...")

/* Pos neg Click */
let positive_tweet = document.getElementById("positive-tweet")
let negative_tweet = document.getElementById("negative-tweet")

positive_tweet.addEventListener('click', pos_or_neg_click)
negative_tweet.addEventListener('click', pos_or_neg_click)

var nodes = document.getElementById("severe-type").getElementsByTagName('*');
for(var i = 0; i < nodes.length; i++){
    nodes[i].disabled = true;
    nodes[i].style.color = "#ddd";
}

function pos_or_neg_click(){
    document.getElementById("next_tweet_btn").disabled = true
    var pos_or_neg = document.querySelector('input[name="pos_or_neg"]:checked').value
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
            document.getElementById("pos_or_neg_status").innerHTML = xhrResponseText
        }

        // if status: 200
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById("pos_or_neg_status").innerHTML = "Saved"
            document.getElementById("next_tweet_btn").disabled = false
        }
    };

    // Clicked on negative
    if (pos_or_neg == "-1"){
        document.getElementById("pos_or_neg_status").innerHTML = "Saving...";

        // Disabling severe tweet choices
        disableSevereTweetElements()

        var url = "/api/mark-response/" + curr_tweet_id + "/-1/"
        xhr.open("POST", url, true)

        // To set Request Header, xhr must be opened. Thus below 2 lines are written after opening XHR
        xhr.setRequestHeader("Content-Type", "application/json")
        xhr.setRequestHeader("X-CSRFToken", csrftoken)
        var data = JSON.stringify({});

        // Send data using post
        xhr.send(data);
    }

    // Clicked on positive
    else{
        document.getElementById("pos_or_neg_status").innerHTML = "Saving...";
        // This will disable all the children of the div
        var nodes = document.getElementById("severe-type").getElementsByTagName('*');
        for(var node of nodes){
            node.disabled = false;
            node.style.color = '';
        }

        var url = "/api/mark-response/" + curr_tweet_id + "/1/"
        xhr.open("POST", url, true)

        // To set Request Header, xhr must be opened. Thus below 2 lines are written after opening XHR
        xhr.setRequestHeader("Content-Type", "application/json")
        xhr.setRequestHeader("X-CSRFToken", csrftoken)
        var data = JSON.stringify({});

        // Send data using post
        xhr.send(data);
    }
}
/* Pos neg Click Ends*/


/* severe click */
let radioOne = document.getElementById("radioOne")
let radioTwo = document.getElementById("radioTwo")
let radioThree = document.getElementById("radioThree")
let radioFour = document.getElementById("radioFour")

radioOne.addEventListener('click', severeClick)
radioTwo.addEventListener('click', severeClick)
radioThree.addEventListener('click', severeClick)
radioFour.addEventListener('click', severeClick)

function severeClick(){
    document.getElementById("next_tweet_btn").disabled = true
    document.getElementById("severe_status").innerHTML = "Saving...";
    var severe = document.querySelector('input[name="severe"]:checked').value
    console.log(severe)

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
            document.getElementById("severe_status").innerHTML = xhrResponseText
        }

        // if status: 200
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById("severe_status").innerHTML = "Saved"
            document.getElementById("next_tweet_btn").disabled = false
        }
    };

    var url = "/api/mark-priority/" + curr_tweet_id + "/" + severe + "/"
    xhr.open("POST", url, true)
    xhr.setRequestHeader("Content-Type", "application/json")
    xhr.setRequestHeader("X-CSRFToken", csrftoken)
    var data = JSON.stringify({});
    xhr.send(data);
}
/* severe click ends*/


/* skip_tweet */
let skip_tweet = document.getElementById("skip_tweet")
skip_tweet.addEventListener('click', skip_tweet_click)

function skip_tweet_click(){
    document.getElementById("skip_tweet_status").innerHTML = "Skipping..."
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
            document.getElementById("skip_tweet_status").innerHTML = xhrResponseText
        }

        // if status: 200
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById("skip_tweet_status").innerHTML = ""
            getNextTweet()
        }
    };

    var url = "/api/mark-response/" + curr_tweet_id + "/0/"
    xhr.open("POST", url, true)
    xhr.setRequestHeader("Content-Type", "application/json")
    xhr.setRequestHeader("X-CSRFToken", csrftoken)
    var data = JSON.stringify({});
    xhr.send(data);

}
/* skip_tweet ends */


/* never_ask_again */
let never_ask_again = document.getElementById("never_ask_again")
never_ask_again.addEventListener('click', never_ask_again_click)

function never_ask_again_click(){
    document.getElementById("never_ask_again_status").innerHTML = "Saving..."
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
            document.getElementById("never_ask_again_status").innerHTML = xhrResponseText
        }

        // if status: 200
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById("never_ask_again_status").innerHTML = ""
            getNextTweet()
        }
    };

    var url = "/api/mark-response/" + curr_tweet_id + "/-2/"
    xhr.open("POST", url, true)
    xhr.setRequestHeader("Content-Type", "application/json")
    xhr.setRequestHeader("X-CSRFToken", csrftoken)
    var data = JSON.stringify({});
    xhr.send(data);

}

/* never_ask_again ends */


/* get next tweet */
function getNextTweet(){
    document.getElementById("tweet_id").innerHTML = "Getting Tweet id"
    document.getElementById("next_tweet").innerHTML = "Getting Next Tweet"
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
            document.getElementById("tweet_id").innerHTML = xhrResponseText
            document.getElementById("next_tweet").innerHTML = xhrResponseText
        }

        // if status: 200
        if (xhr.readyState === 4 && xhr.status === 200) {
            old_tweet = curr_tweet_id;
            curr_tweet_id = xhrResponseJson[0]['id']
            curr_tweet_text = xhrResponseJson[0]['tweet']

            if(old_tweet == curr_tweet_id){
                document.getElementById("pos_or_neg_status").innerHTML = "<span style='color: #ff0000 !important;'>This field cannot be empty</span>"
            }

            document.getElementById("tweet_id").innerHTML = curr_tweet_id
            document.getElementById("next_tweet").innerHTML = curr_tweet_text

            if(curr_tweet_id == 0){
                disablePositiveNegativeElements()
                disableButtons()
                console.log("Disabled pos and neg. Disabled Buttons")
            }
            else{
                // what if admin inserted new tweets just after all tweets are completed of user x
                // thus enable it again
                enablePositiveNegativeElements()
                enableButtons()
                document.getElementById("next_tweet_btn").disabled = true
                console.log("Enabled pos and neg. Enabled Buttons")
            }
            setSevereToModerate()
            disableSevereTweetElements()
            unselectPosNeg()
            setStatusTextToDefault()
        }
    };

    var url = "/api/get-next-tweet/"
    xhr.open("GET", url, true)
    xhr.setRequestHeader("Content-Type", "application/json")
    xhr.setRequestHeader("X-CSRFToken", csrftoken)
    var data = JSON.stringify({});
    xhr.send(data);
}
var curr_tweet_id, curr_tweet_text;
/* get next tweet ends */

function disableSevereTweetElements(){
    // This will disable all the children of the div
    var nodes = document.getElementById("severe-type").getElementsByTagName('*');
    for(var i = 0; i < nodes.length; i++){
        nodes[i].disabled = true;
        nodes[i].style.color = "#ddd";
    }
}

function disablePositiveNegativeElements(){
    // This will disable all the children of the div
    var nodes = document.getElementById("pos_or_neg_div").getElementsByTagName('*');
    for(var i = 0; i < nodes.length; i++){
        nodes[i].disabled = true;
        nodes[i].style.color = "#ddd";
    }
}

function enablePositiveNegativeElements(){
    // This will disable all the children of the div
    var nodes = document.getElementById("pos_or_neg_div").getElementsByTagName('*');
    for(var i = 0; i < nodes.length; i++){
        nodes[i].disabled = false;
        nodes[i].style.color = "";
    }
}

function disableButtons(){
    document.getElementById("skip_tweet").disabled = true;
    document.getElementById("never_ask_again").disabled = true;
    document.getElementById("next_tweet_btn").disabled = true;
}

function enableButtons(){
    document.getElementById("skip_tweet").disabled = false;
    document.getElementById("never_ask_again").disabled = false;
    document.getElementById("next_tweet_btn").disabled = false;
}

/* next_tweet_btn */
let next_tweet_btn = document.getElementById("next_tweet_btn")
next_tweet_btn.addEventListener('click', next_tweet_btn_click)

function next_tweet_btn_click() {
    getNextTweet()
}

/* next_tweet_btn ends */


function unselectPosNeg(){
    var ele = document.getElementsByName("pos_or_neg");
    for(var i = 0; i < ele.length; i++)
        ele[i].checked = false;
}

function setStatusTextToDefault(){
    document.getElementById("pos_or_neg_status").innerHTML = "Status"
    document.getElementById("severe_status").innerHTML = "Status"
}

function setSevereToModerate(){
    document.getElementById('radioTwo').checked = true;
    var severe = document.querySelector('input[name="severe"]:checked').value
    console.log(severe)
}
