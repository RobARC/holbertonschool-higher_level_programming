/* JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
    The name must be displayed in the HTML tag DIV#character
    You can’t use document.querySelector to select the HTML tag
    You must use the JQuery API */

const $ = window.$;
$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  $.get(url, function (data) {
    const name = data.name;
    $('DIV#character').text(name);
  });
});