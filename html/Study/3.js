// 함수 오버로딩에 관한 두가지 예
function sendMessage(msg, obj) {
    if (arguments.length == 2)
        obj.document.write(msg);
    else
        document.write(msg);
}


function makeArray() {
    var arr = [];

    for (var i = 0; i < arguments.length; i++) {
        arr.push(arguments[i]);
    }
    return arr;
}

// 함수에 전달인자 개수 결정하기 위해 사용할 수 있는 방법 (약간의 트릭)
// 전달인자기 전달되지 않았을 때 그 전달인자의 값이 undefined 라는 사실을 이용
function displayError(msg) {
    if (typeof msg == 'undefined') {
        msg = "An error occured";
    }
    document.write(msg);
}

function typeo() {
    //typeof 사용
    var num = "1";
    var arr = "a,b,c";
    document.write(typeof num, ', ', typeof arr, )

    if (typeof num == "string")
        num = parseInt(num);
    if (typeof arr == "string")
        arr = arr.split(",");
    document.write('<br>-> ', typeof num, ', ', typeof arr)
}

function construct() {
    var num = "45";
    var str = ["a", 'b', 'c'];
    document.write(num.constructor, ' / ', str.constructor)

    if (num.constructor == String)
        num = parseInt(num);
    if (str.constructor == Array)
        str = str.join(',');
    document.write('<br>-> ', num.constructor, ' / ', str.constructor)
}