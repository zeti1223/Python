#!/usr/bin/env python3
import sys
import subprocess
import re
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QProgressBar
from PyQt6.QtCore import QTimer, Qt

UPOWER_PATH = "/org/freedesktop/UPower/devices/battery_BAT0"

def get_upower_info():
    result = subprocess.run(
        ["upower", "-i", UPOWER_PATH],
        capture_output=True, text=True
    )
    return result.stdout.splitlines()

def parse_key(lines, key):
    for line in lines:
        if key in line:
            return line.split(":", 1)[1].strip()
    return None

def to_float(value):
    if value is None:
        return None
    number = re.findall(r"[0-9.]+", value)
    return float(number[0]) if number else None

def get_battery_info():
    lines = get_upower_info()
    state = parse_key(lines, "state")
    energy_rate = to_float(parse_key(lines, "energy-rate"))
    energy_full = to_float(parse_key(lines, "energy-full"))
    energy_now  = to_float(parse_key(lines, "energy"))

    percent = None
    if energy_full and energy_now:
        percent = energy_now / energy_full * 100

    time_to_full = parse_key(lines, "time to full")
    time_to_empty = parse_key(lines, "time to empty")

    return {
        "state": state,
        "watt": energy_rate,
        "percent": percent,
        "time_to_full": time_to_full,
        "time_to_empty": time_to_empty
    }

class BatteryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Battery Monitor")
        self.setGeometry(300, 300, 300, 150)

        self.layout = QVBoxLayout()
        self.state_label = QLabel("Állapot: ...")
        self.watt_label = QLabel("Töltési watt: ...")
        self.time_label = QLabel("Hátralévő idő: ...")
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.state_label)
        self.layout.addWidget(self.progress)
        self.layout.addWidget(self.watt_label)
        self.layout.addWidget(self.time_label)
        self.setLayout(self.layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_info)
        self.timer.start(1000)
        self.update_info()

    def update_info(self):
        info = get_battery_info()
        self.state_label.setText(f"Állapot: {info['state']}")
        self.progress.setValue(int(info['percent'] or 0))
        self.watt_label.setText(f"Töltési watt: {info['watt'] or 'nincs adat'} W")
        if info['state'] == "charging":
            self.time_label.setText(f"Hátralévő töltési idő: {info['time_to_full'] or 'n/a'}")
        elif info['state'] == "discharging":
            self.time_label.setText(f"Hátralévő merülési idő: {info['time_to_empty'] or 'n/a'}")
        else:
            self.time_label.setText("Hátralévő idő: n/a")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BatteryWindow()
    window.show()
    sys.exit(app.exec())
