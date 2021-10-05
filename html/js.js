/*
window.onloadd = function() {
    // 변수를 선언합니다.
    var header = document.createElement('h1');
    var textNode = document.createTextNode('Hello Dom')
        //노드를 연결합니다.
    header.appendChild(textNode);
    document.body.appendChild(header);

    var header1 = document.getElementById('header-1');
    var header2 = document.getElementById('header-2');

    header1.innerHTML = 'with getElementID()';
    header2.innerHTML = 'with getElementID()';
};

var header = document.createElement('h1');
var textNode = document.createTextNode('Hello Dom')
    //노드를 연결합니다.
header.appendChild(textNode);
document.body.appendChild(header);

document.body.write(header);

window.onload = function() {
    alert('Process - 0');
};
$(document).ready(funtion() {
    alert('First READY');
});
*/

function returnFuntion() {
    alert('문장 A');
    return;
    alert('문장 B');
}

returnFuntion();

function sortAcc(left, right) {
    return left - right;
}

var array = [52, 273, 103, 32];
array.sort(sortAcc);

alert(array);