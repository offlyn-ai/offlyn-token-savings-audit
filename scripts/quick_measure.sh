#!/bin/bash
# Quick Clipper Power Measurement
# Run: sudo ./scripts/quick_measure.sh

cd /Users/rahul/offlyn-token-savings-audit
mkdir -p measurements

echo "=== BASELINE MEASUREMENT (20 sec) ==="
echo "Keep Clipper IDLE during this phase..."
sleep 2
sudo powermetrics --samplers cpu_power -i 1000 -n 20 -o measurements/baseline.log
BASELINE=$(grep "Combined Power" measurements/baseline.log | awk '{sum+=$4; count++} END {printf "%.0f", sum/count}')
echo "Baseline: ${BASELINE} mW"

echo ""
echo "=== NOW START CLIPPER PROCESSING ==="
echo "Press ENTER then immediately process a meeting in Clipper"
read

echo "Measuring active power (60 sec)..."
sudo powermetrics --samplers cpu_power -i 1000 -n 60 -o measurements/active.log
ACTIVE=$(grep "Combined Power" measurements/active.log | awk '{sum+=$4; count++} END {printf "%.0f", sum/count}')
echo "Active: ${ACTIVE} mW"

INCREMENTAL=$((ACTIVE - BASELINE))
echo ""
echo "=== RESULTS ==="
echo "Baseline:    ${BASELINE} mW"
echo "Active:      ${ACTIVE} mW"  
echo "Incremental: ${INCREMENTAL} mW ($(echo "scale=2; $INCREMENTAL/1000" | bc) W)"
echo ""
echo "Results saved to measurements/"
