import time
import serial 
import time 

class GyroHeadingCalculator:
    def init(self):
        # Initialize the heading to 0 degrees
        self.heading = 0.0
        self.last_time = time.time()

    def update_heading(self, gyrozrad_per_sec):
        current_time = time.time()
        time_elapsed = current_time - self.last_time
        rotation_deg = (gyro_z_rad_per_sec * time_elapsed) * (180.0 / 3.141592653589793)
        self.heading += rotation_deg
        self.heading %= 360  # Keep heading within [0, 360) degrees
        self.last_time = current_time
        return self.heading

# Example usage with simulated live data input
if __name__ == "__main__":
    print("Starting...")
    gyro_heading_calculator = GyroHeadingCalculator()
    arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1) 
    gyro_z_rad_per_sec = 0
    # This is where you would integrate your actual live data input.
    # For demonstration, we simulate live data with a loop.
    while True:
        # Simulate reading a new gyroscope Z-axis data point (in radians per second)
        # In a real application, replace this with actual data reading, e.g., from serial port
        if arduino.in_waiting > 0:
            data = arduino.readline().decode('utf-8').rstrip()
            data_parts = data_string.split(',')
            gyro_z_str = data_parts[-1]  # Extract the last variable as the gyroscope Z data
            gyro_z_rad_per_sec = float(gyro_z_str)  # Convert the gyro Z data to a float
        # Update heading based on new data
        new_heading = gyro_heading_calculator.update_heading(gyro_z_rad_per_sec)
        print(f"Updated Heading: {new_heading:.2f} degrees")

        # Simulate a delay between readings, remove or adjust in your actual use case
        time.sleep(1)

# Importing Libraries 
    arduino.close()




