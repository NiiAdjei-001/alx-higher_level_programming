'use strict';

/**
 * Constants
 * Declare constants at the top of the file
 */
const API_URL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

/**
 * Event Listeners
 * Add event listeners if your app interacts with the DOM
 */
$(document).ready(function () {
  $.getJSON(API_URL, function (data) {
    $('DIV#hello').text(data.hello);
  });
});
