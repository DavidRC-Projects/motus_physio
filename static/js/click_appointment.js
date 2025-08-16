document.addEventListener('DOMContentLoaded', function() {
    // Add click to all calendar days
    const days = document.querySelectorAll('.calendar-date');
    
    days.forEach(function(day) {
        day.addEventListener('click', function() {
            // redirect to booking page
            window.location.href = '/booking/';
        });
        
        day.style.cursor = 'pointer';
    });
});