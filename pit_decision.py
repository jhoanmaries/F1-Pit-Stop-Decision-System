import numpy as np

def estimate_degradation(lap_times):
    lap_seconds = lap_times.dt.total_seconds()
    slope = np.polyfit(range(len(lap_seconds)), lap_seconds, 1)[0]
    return slope

def decide_pit(tire_age, degradation, gap_behind, pit_loss=22):
    if tire_age > 20 and degradation > 0.05:
        return "BOX BOX"
    
    if gap_behind < pit_loss:
        return "STAY OUT"
    
    return "STAY OUT"