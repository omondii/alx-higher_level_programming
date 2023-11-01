$(document).ready(function(){
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data){
    let lists = data.results;
    let movies = $('#list_movies');

    $.each(lists, function(index, list){
        movies.append('<li>' + list.title + '</li>')
    });
    });
});