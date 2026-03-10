from .cpu import CpuMonitoring
from .swap import SwapMonitoring
from .memory import MemoryMonitoring

class DataCollector:

    def __init__(self):
        self.cpu = CpuMonitoring()
        self.memory = MemoryMonitoring()
        self.swap = SwapMonitoring()

    def get_all_data(self):

        data = {}

        cpu_data = self.cpu.get_data()
        data.update(cpu_data)

        memory_data = self.memory.get_data()
        data.update(memory_data)

        swap_data = self.swap.get_data()
        data.update(swap_data)

        return data