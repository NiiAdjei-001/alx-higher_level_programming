'use strict';

/**
 * Event Listeners
 * Add event listeners if your app interacts with the DOM
 */
$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
});
