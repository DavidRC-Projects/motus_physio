/* jshint esversion: 6 */
/* global bootstrap */

/**
 Auto-show message modal functionality:
 - Automatically displays Bootstrap modal.
 - Shows notifications.
*/
document.addEventListener('DOMContentLoaded', function() {
    var messageModal = new bootstrap.Modal(document.getElementById('messageModal'));
    messageModal.show();
});
