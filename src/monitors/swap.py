import psutil

class SwapMonitoring():
    def __init__(self):
        pass
    
    def get_data(self):
        swap = psutil.swap_memory()
        
        return {
            'swap_total': f'SWAP Total {round(swap.total / (1024 ** 3), 1)} GB',
            'swap_used': f'SWAP Used {round(swap.used / (1024 ** 3), 1)} GB',
            'swap_free': f'SWAP Free {round(swap.free / (1024 ** 3), 1)} GB',
            'swap_percent': f'SWAP {swap.percent} %',
            'swap_sin': f'SWAP Sin {round(swap.sin / (1024 ** 3), 1)} GB',
            'swap_sout': f'SWAP Sout {round(swap.sout / (1024 ** 3), 1)} GB'
        }