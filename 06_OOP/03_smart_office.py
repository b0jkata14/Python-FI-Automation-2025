class Device:
    def __init__(self, name, room, power_watts):
        self.name = name
        self.room = room
        self.power_watts = power_watts
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def get_hourly_consumption(self):
        return self.power_watts if self.is_on else 0


class Light(Device):
    def __init__(self, name, room, power_watts, brightness=100):
        super().__init__(name, room, power_watts)
        self.brightness = 100
        self.set_brightness(brightness)

    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level

    def get_hourly_consumption(self):
        if self.is_on:
            return self.power_watts * (self.brightness / 100)

        return 0


class PC(Device):
    def __init__(self, name, room, power_watts, active_users=0):
        super().__init__(name, room, power_watts)
        self.active_users = max(0, active_users)

    def login_user(self):
        self.active_users += 1

    def logout_user(self):
        self.active_users = max(self.active_users - 1, 0)

    def get_hourly_consumption(self):
        if self.is_on:
            return self.power_watts * (1 + 0.1 * self.active_users)

        return 0


class Server(Device):
    def __init__(self, name, room, power_watts, load=50):
        super().__init__(name, room, power_watts)
        self.load = 50
        self.set_load(load)

    def set_load(self, percent):
        if 0 <= percent <= 100:
            self.load = percent

    def get_hourly_consumption(self):
        if self.is_on:
            return self.power_watts * (0.5 + self.load / 100)

        return self.power_watts * 0.1


def generate_report(devices, hours):
    room_energy = {}

    for device in devices:
        room_energy[device.room] = room_energy.get(device.room, 0) + (device.get_hourly_consumption() * hours)

    return sorted(room_energy.items(), key=lambda x: (-x[1], x[0]))