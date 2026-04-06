import fastf1

fastf1.Cache.enable_cache("data")

session = fastf1.get_session(2023, "Monza", "R")
session.load()

laps = session.laps
laps = session.laps.pick_driver("SAI")

print(laps.head())
print(laps[["LapNumber", "LapTime", "Compound", "TyreLife", "Position"]])
