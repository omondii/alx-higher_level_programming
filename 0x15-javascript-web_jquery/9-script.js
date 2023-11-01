$(document).ready(function(){
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data){
        let great = data.hello;
        $('#hello').text(great);
    });
});