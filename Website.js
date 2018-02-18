document.getElementById("asdf").onclick = function() {
        $.getJSON('/url/to/ajax/view/', {foo: 'bar'}, function(data, jqXHR){
            var audio = new Audio('test.wav');
            audio.play();
        });
    }