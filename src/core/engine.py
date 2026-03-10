from src.monitors import DataCollector
from pypresence import Presence
import time
import sys
import os
import json


class RPCengine:
    def __init__(self, config_path=None):
        self.monitoring = DataCollector()
        self.config_path = config_path
        self.client_id = None
        self.update_interval = 15
        self.running = False
        self.start_time = time.time()
        
        if config_path and os.path.exists(config_path):
            self.load_config(config_path)
        
        self.RPC = Presence(self.client_id)
    
    def load_config(self, config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            self.client_id = config.get('client_id', self.client_id)
            self.update_interval = config.get('update_interval', self.update_interval)
    
    def build_presence_from_data(self, config_path=None):
        path = config_path or self.config_path
        
  
        monitoring_vars = {
            'monitoring_1': 'cpu_percent',
            'monitoring_2': 'memory_percent',
            'monitoring_3': 'memory_used',
            'monitoring_4': 'swap_percent'
        }
        
        if path and os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                for key in monitoring_vars:
                    if key in config:
                        monitoring_vars[key] = config[key]
        
        data = self.monitoring.get_all_data()
        details = f"{data.get(monitoring_vars['monitoring_1'], 0)} | {data.get(monitoring_vars['monitoring_2'], 0)}"
        state = f"{data.get(monitoring_vars['monitoring_3'], 0)} | {data.get(monitoring_vars['monitoring_4'], 0)}"
        
        return details, state
    
    def connect(self):
        try:
            self.RPC.connect()
            print('Connected to Discord')
            return True
        except Exception as e:
            print(f'Check your Client ID code in settings.json \n Connection error: {e}')
            return False
    
    def update_presence(self):
        try:
            details, state = self.build_presence_from_data()
            
            self.RPC.update(
                details=details,
                state=state,
                large_image="pc_icon",
                large_text="System Monitor",
                start = self.start_time

            )
            
            print(f"Status updated: {details} | {state}")
            
        except Exception as e:
            print(f"Update error: {e}")
    
    def run(self):
        if not self.connect():
            return
        
        self.running = True
        print(f"Monitoring started (interval: {self.update_interval} seconds")
        
        try:
            while self.running:
                self.update_presence()
                time.sleep(self.update_interval)
        except KeyboardInterrupt:
            print("\nStop")
        finally:
            self.stop()
    
    def stop(self):
        self.running = False
        if self.RPC:
            self.RPC.close()
        print("Disconnected from Discord")