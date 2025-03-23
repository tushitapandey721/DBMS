// Booking Functionality
document.getElementById("bookingForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let name = document.getElementById("name").value;
    let slot = document.getElementById("slotSelection").value;
    
    alert(name + " has booked " + slot + " successfully!");
    
    // Change slot color to red (booked)
    let buttons = document.querySelectorAll(".slot");
    buttons.forEach(btn => {
        if (btn.innerText === slot) {
            btn.classList.remove("available");
            btn.classList.add("booked");
        }
    });

    // Clear input fields
    document.getElementById("name").value = "";
});

// Admin Reset Functionality
document.getElementById("resetSlots").addEventListener("click", function() {
    let buttons = document.querySelectorAll(".slot");
    buttons.forEach(btn => {
        btn.classList.remove("booked");
        btn.classList.add("available");
    });

    alert("All slots have been reset.");
});

