@echo off
echo Starting authserver...
start cmd /k python authserver.py

echo Starting worldserver...
start cmd /k python worldserver.py