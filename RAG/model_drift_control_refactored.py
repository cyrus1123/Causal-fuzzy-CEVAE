
import datetime

class ModelDriftController:
    def __init__(self):
        self.last_update_time = datetime.datetime.now()

    def check_drift(self):
        current_time = datetime.datetime.now()
        drift_detected = (current_time - self.last_update_time).seconds > 3600
        if drift_detected:
            self.handle_drift()

    def handle_drift(self):
        self.last_update_time = datetime.datetime.now()
        print("Drift detected. Retraining the model.")
