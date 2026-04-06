# F1-Pit-Stop-Decision-System
The F1 Pit Stop Decision System is a data-driven race strategy tool that analyzes real Formula 1 telemetry data to determine optimal pit stop decisions. By leveraging historical lap data and tire performance metrics, the system simulates how race engineers evaluate whether a driver should pit or stay out during a race.

**Objective**

To develop a simplified race strategy model that recommends pit stop decisions based on:
  - Tire age (TyreLife)
  - Lap time degradation
  - Gap to the car behind
This project demonstrates how real-world race strategy decisions can be modeled using data analysis and rule-based logic.

**How It Works:**

**1. Data Collection**
  - Uses the FastF1 library to retrieve real race telemetry
  - Loads session data from the 2023 Italian Grand Prix (Monza)
  - Extracts lap data for a selected driver (e.g., Carlos Sainz)
    
**2. Tire Degradation Estimation**
  - Converts lap times into seconds
  - Applies linear regression (via NumPy) to estimate performance drop over time
  - The slope of the regression represents tire degradation
     
**3. Strategy Decision Logic**
   The system evaluates:
     - High tire wear + high degradation → Recommend pit (“BOX BOX”)
     - Insufficient gap to car behind → Stay out (to avoid losing position)
       
**4. Output**
  The system prints:
    - Driver name
    - Tire age
    - Degradation rate
    - Gap to the car behind
    - Final pit decision
  
**Technologies Used**
    - Python
    - FastF1 (race data)
    - NumPy (numerical analysis)

**Features**
  - Real-world F1 telemetry integration
  - Tire degradation modeling using regression
  - Rule-based decision engine for pit strategy
  - Modular structure (data retrieval, analysis, decision logic)
