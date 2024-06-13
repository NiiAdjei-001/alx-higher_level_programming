'use strict';

/**
 * Event Listeners
 * Add event listeners if your app interacts with the DOM
 */
$(document).ready(function () {
  $('DIV#red_header').click(function () {
    $(this).addClass('red');
  });
});
