
Salvage AI Classifier

AI system for identifying usable EV components from junkyard imagery.

What it does

Detects EV-related hardware in scrapyard images

Classifies component type

Estimates condition and reuse potential


Output Classes

BATTERY_PACK

BATTERY_MODULE

ELECTRIC_MOTOR

INVERTER

WIRING_HARNESS

SCRAP


Philosophy

We assume nothing is labeled. Everything must be inferred from visual + structural patterns.

Run

python demo.py 
