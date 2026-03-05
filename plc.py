"""
PLC Simulation Framework
-------------------------------------------
This script simulates a PLC scan cycle with:
- Digital and analog I/O
- Timers (TON / TOF)
- Counters (CTU)
- PID control loop
- State machine for industrial process control

This is meant for learning / simulation purposes and mimics
real PLC structure (scan -> logic -> outputs).
"""

import time
import math
from collections import defaultdict

# -------------------------
# PLC CORE
# -------------------------

class PLC:
    def __init__(self, scan_time=0.05):
        self.scan_time = scan_time
        self.inputs = defaultdict(bool)
        self.outputs = defaultdict(bool)
        self.memory = defaultdict(float)
        self.timers = {}
        self.counters = {}
        self.pid_loops = {}
        self.running = True

    def scan(self):
        while self.running:
            start = time.time()
            self.logic()
            elapsed = time.time() - start
            time.sleep(max(0, self.scan_time - elapsed))

    def logic(self):
        pass

# -------------------------
# TIMER
# -------------------------

class TON:
    def __init__(self, preset):
        self.preset = preset
        self.acc = 0
        self.done = False

    def update(self, enable, dt):
        if enable:
            self.acc += dt
            if self.acc >= self.preset:
                self.done = True
        else:
            self.acc = 0
            self.done = False
        return self.done

# -------------------------
# COUNTER
# -------------------------

class CTU:
    def __init__(self, preset):
        self.preset = preset
        self.acc = 0
        self.done = False

    def update(self, count):
        if count:
            self.acc += 1
        if self.acc >= self.preset:
            self.done = True
        return self.done

# -------------------------
# PID CONTROLLER
# -------------------------

class PID:
    def __init__(self, kp, ki, kd, setpoint=0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.integral = 0
        self.prev_error = 0

    def compute(self, pv, dt):
        error = self.setpoint - pv
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt if dt else 0
        self.prev_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative

# -------------------------
# INDUSTRIAL PROCESS SIM
# -------------------------

class MixingTankProcess(PLC):
    def __init__(self):
        super().__init__(scan_time=0.05)
        self.state = "IDLE"

        self.timers['fill'] = TON(3.0)
        self.timers['mix'] = TON(5.0)
        self.timers['drain'] = TON(3.0)

        self.pid_loops['temp'] = PID(2.0, 0.5, 0.1, setpoint=70)

        self.memory['temperature'] = 20.0
        self.memory['tank_level'] = 0.0

    def logic(self):
        dt = self.scan_time

        start_btn = self.inputs['START']
        stop_btn = self.inputs['STOP']

        if stop_btn:
            self.state = "IDLE"

        if self.state == "IDLE":
            self.outputs['FILL_VALVE'] = False
            self.outputs['MIX_MOTOR'] = False
            self.outputs['DRAIN_VALVE'] = False
            if start_btn:
                self.state = "FILL"

        elif self.state == "FILL":
            self.outputs['FILL_VALVE'] = True
            self.memory['tank_level'] += 5 * dt
            if self.timers['fill'].update(True, dt):
                self.state = "MIX"
                self.timers['fill'].acc = 0

        elif self.state == "MIX":
            self.outputs['FILL_VALVE'] = False
            self.outputs['MIX_MOTOR'] = True

            heater = self.pid_loops['temp'].compute(self.memory['temperature'], dt)
            self.memory['temperature'] += heater * dt * 0.1

            if self.timers['mix'].update(True, dt):
                self.state = "DRAIN"
                self.timers['mix'].acc = 0

        elif self.state == "DRAIN":
            self.outputs['MIX_MOTOR'] = False
            self.outputs['DRAIN_VALVE'] = True
            self.memory['tank_level'] -= 6 * dt
            if self.timers['drain'].update(True, dt):
                self.state = "IDLE"
                self.timers['drain'].acc = 0

        # Clamp
        self.memory['tank_level'] = max(0, min(100, self.memory['tank_level']))

# -------------------------
# SIMULATION LOOP
# -------------------------

if __name__ == '__main__':
    plc = MixingTankProcess()
    plc.inputs['START'] = True

    print("Starting PLC simulation...\n")

    for i in range(400):
        plc.logic()
        print(f"State: {plc.state:<6} | Level: {plc.memory['tank_level']:.1f}% | Temp: {plc.memory['temperature']:.1f}°C")
        time.sleep(plc.scan_time)

    print("\nSimulation complete.")
