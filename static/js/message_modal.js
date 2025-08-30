/* jshint esversion: 6 */
/**
 Shows the Bootstrap modal with ID "messageModal" 
 as soon as the page finishes loading.
 */
document.addEventListener('DOMContentLoaded', function() {
    var messageModal = new bootstrap.Modal(document.getElementById('messageModal'));
    messageModal.show();
});
