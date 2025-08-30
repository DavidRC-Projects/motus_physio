/* jshint esversion: 6 */
/**
 Prevents past dates from being selected by setting
 today's date as the minimum for all date inputs.
 */
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("input[type='date']").forEach(input => {
        input.min = new Date().toISOString().split("T")[0];
    });
});
