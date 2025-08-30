/* jshint jquery: true */
/**
 * Initializes timepicker on inputs with "timepicker" using jQuery.
 * - 24-hour format, 30-min intervals, 09:00–21:00 range.
 * - Dropdown enabled, dynamic updates disabled.
 */
$(document).ready(function() {
  $('input.timepicker').timepicker({
    timeFormat: 'H:i',
    stepMinute: 30,
    minTime: '09:00',
    maxTime: '21:00',
    dropdown: true,
    dynamic: false
  });
});
