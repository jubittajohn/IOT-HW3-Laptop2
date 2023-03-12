import os
import datetime

class StateLogger:
    def __init__(self, log_dir, log_name):
        self.log_dir = log_dir
        self.log_name = log_name
        self.log_path = os.path.join(self.log_dir, self.log_name)
        self.log_file = open(self.log_path, 'w')
        self.log_file.write("Timestamp\t,Topic\t,Messages")

    def log_data(self, data):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log_file.write(f"\n{timestamp}\t,{data.topic}\t,{data.payload}")

    def close(self):
        self.log_file.close()
        
    def __del__(self):
        self.close()