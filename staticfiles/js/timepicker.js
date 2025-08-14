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
