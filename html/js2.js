function test(name) {
    var output = 'Hello ' + name + ' .. !';
    return function() {
        alert(output);
    };
}

var test_1 = test('Web');
var test_2 = test('JavaScript');

test_1();
test_2();