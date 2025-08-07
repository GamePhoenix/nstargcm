import logging
import psutil
import time
import os
import datetime
from classes import SystemComponent

class Logger:
    def __init__(self, simPath):
        logDir = os.path.join(simPath, "logs")
        os.makedirs(logDir, exist_ok=True)

        self.perf_log_path = os.path.join(logDir, "performance.log")
        self.debug_log_path = os.path.join(logDir, "debug.log")

        self.perf_logger = logging.getLogger("performance")
        self.debug_logger = logging.getLogger("debug")

        for logger in (self.perf_logger, self.debug_logger):
            if logger.hasHandlers():
                logger.handlers.clear()

        self.perf_handler = logging.FileHandler(self.perf_log_path, mode='w')
        self.perf_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

        self.perf_logger.setLevel(logging.DEBUG)
        self.perf_logger.addHandler(self.perf_handler)

        debug_handler = logging.FileHandler(self.debug_log_path, mode='w')
        debug_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

        self.debug_logger.setLevel(logging.DEBUG)
        self.debug_logger.addHandler(debug_handler)

    def get_ram_usage_mb(self):
        process = psutil.Process(os.getpid())
        mem_bytes = process.memory_info().rss
        return mem_bytes / (1024 ** 2)  


    def performance(self, frame: int, total_frames: int, frame_start: float):
        frame_time = time.perf_counter() - frame_start
        ram_usage = self.get_ram_usage_mb()
        if frame % 100 == 0:
            self.perf_logger.info(f"Frame {frame}/{total_frames} took {frame_time:.4f} s | RAM used: {ram_usage:.1f} MB")

        mem = psutil.virtual_memory()

        if mem.percent > 80:
            self.perf_logger.warning(f"High RAM usage: {mem.percent:.1f}%")


    def simulation_start(self):
        self.perf_logger.info("Starting simulation...")


    def simulation_end(self, start_time : float, frameCount : float):
        total_time = time.perf_counter() - start_time
        ram_usage = self.get_ram_usage_mb()
        self.perf_logger.info(f"Simulation complete. Total time: {total_time:.2f} seconds| Total frames simulated: {frameCount} | Final RAM: {ram_usage:.1f} MB")

    def debugVariable(self, name : str, var):
        self.debug_logger.info(f"{name} : {var}")

    def debugPosVel(self, sc : SystemComponent):
        self.debug_logger.info(f"The current parameters of {sc.compA.name} are: position: {sc.compA.pos}, and velocity : {sc.compA.vel}")
        self.debug_logger.info(f"The current parameters of {sc.compB.name} are: position: {sc.compB.pos}, and velocity : {sc.compB.vel}")

    def write(self, string : str):
        self.debug_logger.info(string)