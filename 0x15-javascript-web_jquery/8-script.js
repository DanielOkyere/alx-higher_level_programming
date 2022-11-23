/**
 * Reads and lists titles for all movies
 */
 const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

 $.get(url, (data)=>{
    const titles = data.results.map((el)=>  $('#list_movies')
    .append('<li>' + el.title + '<li>').remove(" "))
 });