/* jshint esversion: 6 */
/*
 Handles the appointment calendar:
 - Creates a Bootstrap modal.
 - Makes each calendar day clickable.
 - If a day is marked as "booked", shows a warning modal.
 - Otherwise, redirects the user to the booking page.
*/
document.addEventListener('DOMContentLoaded', function() {
    const modalHTML = `
    <div class="modal fade" id="appointmentModal" tabindex="-1" aria-labelledby="appointmentModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="appointmentModalLabel">Appointment Information</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body" id="appointmentModalBody">
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-primary" data-bs-dismiss="modal">OK</button>
                </div>
            </div>
        </div>
    </div>
`;

if (!document.getElementById('appointmentModal')) {
    document.body.insertAdjacentHTML('beforeend', modalHTML);
}

const days = document.querySelectorAll('.calendar-date');

days.forEach(function(day) {
    day.addEventListener('click', function() {
        if (this.classList.contains('booked')) {
            const modalBody = document.getElementById('appointmentModalBody');
            modalBody.innerHTML = '<p class="text-warning"><i class="fas fa-exclamation-triangle me-2"></i>This day is already booked. Please select a different day.</p>';
            
            const modal = new bootstrap.Modal(document.getElementById('appointmentModal'));
            modal.show();
            return;
        }
            
            // redirect to booking page
            window.location.href = '/booking/';
        });
        
        day.style.cursor = 'pointer';
    });
});