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
        }
    };

    // Clicked on negative
    if (pos_or_neg == "-1"){
        document.getElementById("pos_or_neg_status").innerHTML = "Saving...";
        // This will disable all the children of the div
        var nodes = document.getElementById("severe-type").getElementsByTagName('*');
        for(var i = 0; i < nodes.length; i++){
            nodes[i].disabled = true;
            nodes[i].style.color = "#ddd";
        }
        var url = "/api/mark-response/191/-1/"
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

        var url = "/api/mark-response/191/1/"
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
    document.getElementById("severe_status").innerHTML = "Saving...";
    var severe = document.querySelector('input[name="severe"]:checked').value
    console.log(severe)
    document.getElementById("severe_status").innerHTML = "Saved";
}
/* severe click ends*/
