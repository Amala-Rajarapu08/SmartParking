from main import ParkingSystem


def test_park_vehicle(capsys):
    parking = ParkingSystem()
    parking.park_vehicle("AP1234")

    assert parking.slots[1] == "AP1234"
    assert "Success" in capsys.readouterr().out


def test_duplicate_vehicle(capsys):
    parking = ParkingSystem()
    parking.park_vehicle("AP1234")
    parking.park_vehicle("AP1234")

    assert sum(v == "AP1234" for v in parking.slots.values()) == 1
    assert "already parked" in capsys.readouterr().out


def test_parking_full(capsys):
    parking = ParkingSystem()

    for i in range(5):
        parking.park_vehicle(f"AP{i}")

    parking.park_vehicle("AP9999")

    assert all(v is not None for v in parking.slots.values())
    assert "parking is full" in capsys.readouterr().out


def test_remove_vehicle(capsys):
    parking = ParkingSystem()
    parking.park_vehicle("AP1234")
    parking.remove_vehicle("AP1234")

    assert all(v != "AP1234" for v in parking.slots.values())
    assert "Parking fee: Rs. 20" in capsys.readouterr().out


def test_parking_summary(capsys):
    parking = ParkingSystem()
    parking.park_vehicle("AP1234")
    parking.summary()

    output = capsys.readouterr().out
    assert "Total slots: 5" in output
    assert "Occupied slots: 1" in output
    assert "Available slots: 4" in output


def test_view_slots(capsys):
    parking = ParkingSystem()
    parking.view_slots()

    output = capsys.readouterr().out
    assert "Slot 1: Available" in output
    assert "Slot 5: Available" in output


def test_empty_vehicle(capsys):
    parking = ParkingSystem()
    parking.park_vehicle("   ")

    assert all(v is None for v in parking.slots.values())
    assert "cannot be empty" in capsys.readouterr().out


def test_remove_unknown_vehicle(capsys):
    parking = ParkingSystem()
    parking.remove_vehicle("AP9999")

    assert "Vehicle not found" in capsys.readouterr().out


def test_menu_view_slots(capsys, monkeypatch):
    parking = ParkingSystem()
    inputs = iter(["1", "5"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    parking.run()

    output = capsys.readouterr().out
    assert "Slot 1: Available" in output
    assert "Thank you for using Smart Parking Management System!" in output


def test_menu_park_vehicle(capsys, monkeypatch):
    parking = ParkingSystem()
    inputs = iter(["2", "AP1234", "5"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    parking.run()

    assert parking.slots[1] == "AP1234"
    assert "Success" in capsys.readouterr().out


def test_menu_remove_vehicle(capsys, monkeypatch):
    parking = ParkingSystem()
    parking.park_vehicle("AP1234")
    capsys.readouterr()

    inputs = iter(["3", "AP1234", "5"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    parking.run()

    assert parking.slots[1] is None
    assert "Parking fee: Rs. 20" in capsys.readouterr().out


def test_menu_summary(capsys, monkeypatch):
    parking = ParkingSystem()
    inputs = iter(["4", "5"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    parking.run()

    assert "Total slots: 5" in capsys.readouterr().out


def test_menu_background_report(capsys, monkeypatch):
    parking = ParkingSystem()
    inputs = iter(["6", "5"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    parking.run()

    assert "Parking Summary" in capsys.readouterr().out


def test_menu_performance(capsys, monkeypatch):
    parking = ParkingSystem()
    inputs = iter(["7", "5"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    parking.run()

    output = capsys.readouterr().out
    assert "Performance Evaluation" in output
    assert "Time complexity: O(n)" in output


def test_menu_invalid_choice(capsys, monkeypatch):
    parking = ParkingSystem()
    inputs = iter(["9", "5"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    parking.run()

    assert "Invalid choice" in capsys.readouterr().out
