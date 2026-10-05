from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.database import (
    initialize_database,
    get_all_slots,
    park_vehicle as db_park_vehicle,
    remove_vehicle as db_remove_vehicle,
)


app = FastAPI(title="Smart Parking Management System")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


TOTAL_SLOTS = 5


# Initialize SQLite database when backend starts
initialize_database()


# Request model
class Vehicle(BaseModel):
    vehicle_number: str


@app.get("/")
def home():
    return {"message": "Smart Parking Management System Backend is running!"}


@app.get("/api/health")
def health():
    return {"status": "success", "message": "Backend is healthy"}


@app.get("/api/parking/status")
def parking_status():

    parking_slots = get_all_slots()

    occupied = sum(1 for vehicle in parking_slots.values() if vehicle is not None)

    return {
        "total_slots": TOTAL_SLOTS,
        "occupied_slots": occupied,
        "available_slots": TOTAL_SLOTS - occupied,
        "slots": parking_slots,
    }


@app.get("/api/parking/available")
def available_slots():

    parking_slots = get_all_slots()

    available = [slot for slot, vehicle in parking_slots.items() if vehicle is None]

    return {"available_slots": available}


@app.post("/api/parking/park")
def park_vehicle(vehicle: Vehicle):

    vehicle_number = vehicle.vehicle_number.strip().upper()

    # Check empty vehicle number
    if not vehicle_number:
        raise HTTPException(status_code=400, detail="Vehicle number cannot be empty")

    parking_slots = get_all_slots()

    # Check duplicate vehicle
    if vehicle_number in parking_slots.values():

        raise HTTPException(
            status_code=400, detail=f"Vehicle {vehicle_number} is already parked"
        )

    # Find first available slot
    for slot, parked_vehicle in parking_slots.items():

        if parked_vehicle is None:

            db_park_vehicle(slot, vehicle_number)

            return {
                "message": "Vehicle parked successfully",
                "slot": slot,
                "vehicle_number": vehicle_number,
            }

    raise HTTPException(status_code=400, detail="No parking slots available")


@app.delete("/api/parking/remove/{slot}")
def remove_vehicle(slot: int):

    parking_slots = get_all_slots()

    # Check valid slot
    if slot not in parking_slots:

        raise HTTPException(status_code=404, detail="Invalid parking slot")

    # Check empty slot
    if parking_slots[slot] is None:

        raise HTTPException(status_code=404, detail="Slot is already empty")

    vehicle_number = parking_slots[slot]

    # Remove vehicle from database
    db_remove_vehicle(slot)

    return {
        "message": "Vehicle removed successfully",
        "slot": slot,
        "vehicle_number": vehicle_number,
        "fee": 20,
    }


@app.get("/api/parking/summary")
def parking_summary():

    parking_slots = get_all_slots()

    occupied = sum(1 for vehicle in parking_slots.values() if vehicle is not None)

    return {
        "total_slots": TOTAL_SLOTS,
        "occupied": occupied,
        "available": TOTAL_SLOTS - occupied,
        "parking_fee_per_hour": 20,
    }
