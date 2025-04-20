# FlytBase Drone Deconfliction System

This is a simulation-based system that checks if a planned drone flight will cause a conflict with other drones in the airspace. It works in 4 dimensions: x, y, z, and time.

---

## How it works

- Loads a primary drone path and paths of other drones from a JSON file.
- Interpolates each drone's position over time.
- Compares positions to check if any two drones are too close at the same time.
- Classifies the type of conflict (e.g., 4D, altitude-only, etc.).
- Shows the result as text and in a 3D plot.

---

## How to run

1. Install dependencies:

```bash
pip install matplotlib
