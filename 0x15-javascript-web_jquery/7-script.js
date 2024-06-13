'use strict';

/**
 * Constants
 * Declare constants at the top of the file
 */
const API_URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

/**
 * Event Listeners
 * Add event listeners if your app interacts with the DOM
 */
$(document).ready(function () {
  $.getJSON(API_URL, function (data) {
    $('DIV#character').text(data.name);
  });
});
