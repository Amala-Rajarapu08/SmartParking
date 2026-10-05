const API_URL = "http://127.0.0.1:8000";

async function loadParkingStatus() {
    try {
        const response = await fetch(
            `${API_URL}/api/parking/status`
        );

        const data = await response.json();

        document.getElementById("totalSlots").textContent =
            data.total_slots;

        document.getElementById("occupiedSlots").textContent =
            data.occupied_slots;

        document.getElementById("availableSlots").textContent =
            data.available_slots;

        displaySlots(data.slots);

    } catch (error) {
        showMessage("Backend is not running.", true);
        console.error(error);
    }
}


function displaySlots(slots) {

    const container = document.getElementById("parkingSlots");

    container.innerHTML = "";

    for (const [slotNumber, vehicle] of Object.entries(slots)) {

        const slot = document.createElement("div");

        slot.className = vehicle
            ? "slot occupied"
            : "slot available";

        slot.innerHTML = `
            <div>Slot ${slotNumber}</div>
            <br>
            <div>
                ${vehicle ? "🚗 " + vehicle : "🟢 Available"}
            </div>
        `;

        container.appendChild(slot);
    }
}


async function parkVehicle() {

    const vehicleInput =
        document.getElementById("vehicleNumber");

    const vehicleNumber =
        vehicleInput.value.trim();

    if (!vehicleNumber) {
        showMessage("Please enter vehicle number.", true);
        return;
    }

    try {

        const response = await fetch(
            `${API_URL}/api/parking/park`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    vehicle_number: vehicleNumber
                })
            }
        );

        const data = await response.json();

        if (!response.ok) {
            showMessage(data.detail, true);
            return;
        }

        showMessage(
            `Vehicle ${vehicleNumber} parked in Slot ${data.slot}`
        );

        vehicleInput.value = "";

        loadParkingStatus();

    } catch (error) {

        showMessage(
            "Unable to connect to backend.",
            true
        );

        console.error(error);
    }
}


async function removeVehicle() {

    const slotInput =
        document.getElementById("removeSlot");

    const slotNumber =
        slotInput.value;

    if (!slotNumber) {
        showMessage("Please enter slot number.", true);
        return;
    }

    try {

        const response = await fetch(
            `${API_URL}/api/parking/remove/${slotNumber}`,
            {
                method: "DELETE"
            }
        );

        const data = await response.json();

        if (!response.ok) {
            showMessage(data.detail, true);
            return;
        }

        showMessage(
            `Vehicle removed. Parking fee: ₹${data.fee}`
        );

        slotInput.value = "";

        loadParkingStatus();

    } catch (error) {

        showMessage(
            "Unable to connect to backend.",
            true
        );

        console.error(error);
    }
}


function showMessage(message, error = false) {

    const messageBox =
        document.getElementById("message");

    messageBox.textContent = message;

    messageBox.style.color =
        error ? "red" : "green";
}


loadParkingStatus();