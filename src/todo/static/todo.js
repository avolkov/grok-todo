function toggleAddControls(controls_id) {
    controls = document.getElementById(controls_id);
    if (controls.style.display=='none') {
        controls.style.display='block';
    } else {
        controls.style.display='none';
    }
}

function hideControls() {
    buttons = document.getElementsByClassName('update_button');
    for (i=0;i<buttons.length;i++) { buttons[i].style.display='none'; }
    controls = document.getElementsByClassName('controls');
    for (i=0;i<controls.length;i++) { controls[i].style.display='none'; }
    moveDoneToBottom();
}

function checkItem(url) {
    req = false;
    if(window.XMLHttpRequest && !(window.ActiveXObject)) {
        try {
            req = new XMLHttpRequest();
        } catch(e) {
            req = false;
        }
    } else if(window.ActiveXObject) {
        try {
            req = new ActiveXObject("Msxml2.XMLHTTP");
        } catch(e) {
            try {
                req = new ActiveXObject("Microsoft.XMLHTTP");
            } catch(e) {
                req = false;
            }
        }
    }
    if(req) {
        req.onreadystatechange = processReqChange;
        req.open("GET", url, true);
        req.send("");
    }
}

function processReqChange() {
    if (req.readyState == 4) {
        if (req.status == 200) {
            div = document.getElementById(req.responseText);
            if (div.className=='pending') {
                div.className='done';
            } else {
                div.className='pending';
            }
            moveDoneToBottom();
        } else {
            alert("There was a problem setting the checkbox state:\n" +
                req.statusText);
        }
    }
}

function getPreviousItem(item) {
    var item  = item.previousSibling;
    while (item.nodeType!=1) {
        item=item.previousSibling;
    }
    return item
}

function moveDoneToBottom(){
    pending=document.getElementsByClassName('pending');
    for (i=0;i<pending.length;i++) {
        var item=getPreviousItem(pending[i]);
        while (item.className=='done') { 
            var clone1=pending[i].cloneNode(true);
            var clone2=item.cloneNode(true);
            var replaced1=pending[i].parentNode.replaceChild(clone2, pending[i]);
            var replaced2=item.parentNode.replaceChild(clone1, item);
            item=getPreviousItem(clone1);
        }
    }
}
