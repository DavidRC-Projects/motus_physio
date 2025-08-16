document.addEventListener('DOMContentLoaded', function() {
    // Add click to all calendar days
    const days = document.querySelectorAll('.calendar-date');
    
    days.forEach(function(day) {
        day.addEventListener('click', function() {
            if (this.classList.contains('booked')) {
                alert('This day is already booked. Please select a different day.');
                return;
            }
            
            // redirect to booking page
            window.location.href = '/booking/';
        });
        
        day.style.cursor = 'pointer';
    });
});