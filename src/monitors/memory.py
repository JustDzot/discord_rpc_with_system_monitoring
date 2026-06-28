import psutil

class MemoryMonitoring():
    def __init__(self):
        pass
    
    def get_data(self):
        memory = psutil.virtual_memory()
        
        return {
            'memory_total': f'💾 RAM Total {round(memory.total / (1024 ** 3), 1)} GB',
            'memory_used': f'💾 RAM Used {round(memory.used / (1024 ** 3), 1)} GB',
            'memory_free': f'💾 RAM Free {round(memory.free / (1024 ** 3), 1)} GB',
            'memory_available': f'💾 RAM Available {round(memory.available / (1024 ** 3), 1)} GB',
            'memory_percent': f'💾 RAM {memory.percent} %'
        }