/** This function will show the email verification modal after the page loads.
*This is used as a reminder to verify their email.
*/
document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('verifyModal')) {
        var verifyModal = new bootstrap.Modal(document.getElementById('verifyModal'));
        verifyModal.show();
    }
});