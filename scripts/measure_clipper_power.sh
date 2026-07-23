#!/bin/bash
# Clipper Power Measurement Script for SCI Calculation
# Run with: sudo ./scripts/measure_clipper_power.sh

set -e

OUTPUT_DIR="measurements"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

mkdir -p "$OUTPUT_DIR"

echo "=============================================="
echo "Clipper Power Measurement for SCI Calculation"
echo "=============================================="
echo ""
echo "Timestamp: $(date)"
echo "Output directory: $OUTPUT_DIR"
echo ""

# Step 1: Baseline measurement
echo "[Step 1/3] Measuring baseline power (30 seconds)..."
echo "Please ensure Clipper is NOT actively processing."
echo ""

powermetrics --samplers cpu_power,gpu_power -i 1000 -n 30 2>/dev/null | tee "$OUTPUT_DIR/baseline_${TIMESTAMP}.log" | grep -E "^(Combined Power|CPU Power|GPU Power)" &
BASELINE_PID=$!
wait $BASELINE_PID

BASELINE_POWER=$(grep "Combined Power" "$OUTPUT_DIR/baseline_${TIMESTAMP}.log" | awk '{sum+=$4; count++} END {if(count>0) printf "%.2f", sum/count; else print "N/A"}')
echo ""
echo "Baseline Power: ${BASELINE_POWER} mW"
echo ""

# Step 2: Active measurement prompt
echo "[Step 2/3] Ready for Clipper inference measurement."
echo ""
echo "Instructions:"
echo "  1. Have a test audio file ready (or use a live meeting)"
echo "  2. Press ENTER to start measurement"
echo "  3. Immediately start Clipper processing"
echo "  4. Measurement will run for 120 seconds"
echo ""
read -p "Press ENTER when ready to start Clipper measurement... "

echo ""
echo "Measuring Clipper active power (120 seconds)..."
echo "START CLIPPER PROCESSING NOW!"
echo ""

powermetrics --samplers cpu_power,gpu_power -i 1000 -n 120 2>/dev/null | tee "$OUTPUT_DIR/clipper_active_${TIMESTAMP}.log" | grep -E "^(Combined Power|CPU Power|GPU Power)" &
ACTIVE_PID=$!
wait $ACTIVE_PID

ACTIVE_POWER=$(grep "Combined Power" "$OUTPUT_DIR/clipper_active_${TIMESTAMP}.log" | awk '{sum+=$4; count++} END {if(count>0) printf "%.2f", sum/count; else print "N/A"}')
echo ""
echo "Clipper Active Power: ${ACTIVE_POWER} mW"
echo ""

# Step 3: Calculate incremental
echo "[Step 3/3] Calculating incremental power..."
echo ""

if [[ "$BASELINE_POWER" != "N/A" && "$ACTIVE_POWER" != "N/A" ]]; then
    INCREMENTAL=$(echo "$ACTIVE_POWER - $BASELINE_POWER" | bc)
    INCREMENTAL_WATTS=$(echo "scale=2; $INCREMENTAL / 1000" | bc)
    
    echo "=============================================="
    echo "MEASUREMENT RESULTS"
    echo "=============================================="
    echo "Baseline Power:     ${BASELINE_POWER} mW"
    echo "Active Power:       ${ACTIVE_POWER} mW"
    echo "Incremental Power:  ${INCREMENTAL} mW (${INCREMENTAL_WATTS} W)"
    echo ""
    echo "Results saved to: $OUTPUT_DIR/"
    echo ""
    
    # Save summary
    cat > "$OUTPUT_DIR/summary_${TIMESTAMP}.txt" << EOF
Clipper Power Measurement Summary
=================================
Timestamp: $(date)
Baseline Power: ${BASELINE_POWER} mW
Active Power: ${ACTIVE_POWER} mW
Incremental Power: ${INCREMENTAL} mW (${INCREMENTAL_WATTS} W)

For SCI calculation:
- Use incremental power: ${INCREMENTAL_WATTS} W
- Multiply by processing hours
- Apply grid intensity: 350 gCO2eq/kWh (IEA 2023)
EOF
    
    echo "Summary saved to: $OUTPUT_DIR/summary_${TIMESTAMP}.txt"
else
    echo "Error: Could not calculate power values"
fi
