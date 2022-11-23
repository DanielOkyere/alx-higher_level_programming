/**
 * Query https://swapi-api.hbtn.io/api/people/5/?format=json
 */
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$.get(url, (data)=>{
    $('#character').text(data.name);
});