import logging
import psutil
import time
import os
import datetime

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)


timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
perf_log_path = os.path.join(log_dir, f"performance_{timestamp}.log")

perf_logger = logging.getLogger("performance")

if perf_logger.hasHandlers():
    perf_logger.handlers.clear()

perf_handler = logging.FileHandler(perf_log_path, mode='w')
perf_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
perf_logger.setLevel(logging.DEBUG)
perf_logger.addHandler(perf_handler)


def get_ram_usage_mb():
    process = psutil.Process(os.getpid())
    mem_bytes = process.memory_info().rss
    return mem_bytes / (1024 ** 2)  


def performance(frame: int, total_frames: int, frame_start: float):
    frame_time = time.perf_counter() - frame_start
    ram_usage = get_ram_usage_mb()
    if frame % 100 == 0:
        perf_logger.info(f"Frame {frame}/{total_frames} took {frame_time:.4f} s | RAM used: {ram_usage:.1f} MB")

    mem = psutil.virtual_memory()

    if mem.percent > 80:
        perf_logger.warning(f"High RAM usage: {mem.percent:.1f}%")


def simulation_start():
    perf_logger.info("Starting simulation...")


def simulation_end(start_time : float, frameCount : float):
    total_time = time.perf_counter() - start_time
    ram_usage = get_ram_usage_mb()
    perf_logger.info(f"Simulation complete. Total time: {total_time:.2f} seconds| Total frames simulated: {frameCount} | Final RAM: {ram_usage:.1f} MB")
