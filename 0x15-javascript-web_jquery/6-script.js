'use strict';

/**
 * Event Listeners
 * Add event listeners if your app interacts with the DOM
 */
$(document).ready(function () {
  $('DIV#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
