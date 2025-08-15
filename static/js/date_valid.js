// Date validation to prevent selecting past dates
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("input[type='date']").forEach(input => {
        input.min = new Date().toISOString().split("T")[0];
    });
});
