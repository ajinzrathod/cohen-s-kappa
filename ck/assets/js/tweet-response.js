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

    // Clicked on negative
    if (pos_or_neg == "-1"){
        // This will disable all the children of the div
        var nodes = document.getElementById("severe-type").getElementsByTagName('*');
        for(var i = 0; i < nodes.length; i++){
            nodes[i].disabled = true;
            nodes[i].style.color = "#ddd";
        }
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
        document.getElementById("pos_or_neg_status").innerHTML = "Saved"
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
