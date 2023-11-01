$(document).ready(function(){
    $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data){
        let chname = data.name;
        $('#character').text(chname);
    });
});