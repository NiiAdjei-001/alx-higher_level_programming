'use strict';

/**
 * Event Listeners
 * Add event listeners if your app interacts with the DOM
 */
$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    try {
      const item = $('UL.my_list LI').get(-1);
      item.remove();
    } catch (err) {
      console.error('List Empty: Can not remove from an empty list');
    }
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
