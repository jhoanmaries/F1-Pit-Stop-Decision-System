import fastf1
from strategy.pit_decision import estimate_degradation, decide_pit

fastf1.Cache.enable_cache("data")

session = fastf1.get_session(2023, "MONZA", "R")
session.load()

laps = session.laps.pick_driver("SAI")

degradation = estimate_degradation(laps["LapTime"])
tire_age = laps["TyreLife"].iloc[-1]

# EXAMPLE ---- NEED TO CHANGE TO USER INPUT
gap_behind = 25

decision = decide_pit(tire_age, degradation, gap_behind)

print("Driver: Carlos Sainz")
print("Tire Age:", tire_age)
print("Degradation:", round(degradation, 4))
print("Gap Behind:", gap_behind)
print("Decision:", decision)