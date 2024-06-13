'use strict';

/**
 * Event Listeners
 * Add event listeners if your app interacts with the DOM
 */
$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    $('header').toggleClass('red');
    $('header').toggleClass('green');
  });
});
