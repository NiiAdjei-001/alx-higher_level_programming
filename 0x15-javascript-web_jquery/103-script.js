'use strict';

/**
 * Constants
 * Declare constants at the top of the file
 */
const ALT_URL = 'https://hellosalut.stefanbohacek.dev/';
const API_URL = 'https://www.fourtonfish.com/hellosalut/hello/';

/**
 * Event Listeners
 * Add event listeners if your app interacts with the DOM
 */
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const txt = $('INPUT#language_code:text').val();
    $.ajax({
      url: `${ALT_URL}?lang=${txt}`,
      type: 'GET',
      dataType: 'json',
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    })
  });

  $('INPUT#language_code').on('keydown', function (event) {
    if (event.key === 'Enter') {
      const txt = $('INPUT#language_code:text').val();
      $.ajax({
        url: `${ALT_URL}?lang=${txt}`,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
          $('DIV#hello').text(data.hello);
        }
      });
    };
  });
});
