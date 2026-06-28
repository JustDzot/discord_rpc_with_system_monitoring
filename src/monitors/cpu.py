import psutil

class CpuMonitoring():
    def __init__(self):
        pass
    
    def get_data(self):
        cpu_percent = psutil.cpu_percent(interval=0.5)
        cpu_freq = psutil.cpu_freq(percpu=False)
        
        cpu_freq_current = cpu_freq.current if cpu_freq else 0
        cpu_freq_max = cpu_freq.max if cpu_freq else 0
        
        return {
            'cpu_percent': f'🖥️ CPU {round(cpu_percent, 1)} %',
            'cpu_freq_current': f'🖥️ CPU {round(cpu_freq_current, 1)} Mhz',
            'cpu_freq_max': f'🖥️ CPU Max {round(cpu_freq_max, 1)} Mhz'
        }