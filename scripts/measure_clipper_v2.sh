#!/bin/bash
# Clipper Power Measurement v2 - Improved
# Run: sudo ./scripts/measure_clipper_v2.sh

set -e
cd /Users/rahul/offlyn-token-savings-audit
mkdir -p measurements

TIMESTAMP=$(date +%Y%m%d_%H%M%S)

echo "=============================================="
echo "  CLIPPER POWER MEASUREMENT v2"
echo "=============================================="
echo ""
echo "IMPORTANT INSTRUCTIONS:"
echo ""
echo "1. Have Clipper app open and ready"
echo "2. Have a meeting recording/audio ready to process"
echo "   (Or join a test call you can record)"
echo "3. When prompted, START RECORDING in Clipper immediately"
echo "4. Let it transcribe for the full measurement duration"
echo ""
echo "Press ENTER when ready to begin..."
read

# Phase 1: True baseline (Clipper open but NOT recording/processing)
echo ""
echo "=== PHASE 1: BASELINE (30 sec) ==="
echo "DO NOT record or process anything in Clipper yet."
echo "Just let it sit idle."
echo ""
sleep 3
powermetrics --samplers cpu_power -i 1000 -n 30 -o measurements/baseline_v2_${TIMESTAMP}.log
BASELINE=$(grep "Combined Power" measurements/baseline_v2_${TIMESTAMP}.log | awk -F': ' '{gsub(/ mW/,"",$2); sum+=$2; count++} END {printf "%.0f", sum/count}')
echo ""
echo "✓ Baseline captured: ${BASELINE} mW"

# Phase 2: Active inference
echo ""
echo "=== PHASE 2: CLIPPER INFERENCE (90 sec) ==="
echo ""
echo ">>> START RECORDING IN CLIPPER NOW! <<<"
echo ">>> Speak or play audio for transcription <<<"
echo ""
echo "Press ENTER the moment you start recording..."
read
echo "Measuring... keep Clipper transcribing..."
powermetrics --samplers cpu_power -i 1000 -n 90 -o measurements/active_v2_${TIMESTAMP}.log
ACTIVE=$(grep "Combined Power" measurements/active_v2_${TIMESTAMP}.log | awk -F': ' '{gsub(/ mW/,"",$2); sum+=$2; count++} END {printf "%.0f", sum/count}')
echo ""
echo "✓ Active captured: ${ACTIVE} mW"

# Phase 3: Post-processing (when meeting ends and Clipper generates summary)
echo ""
echo "=== PHASE 3: SUMMARIZATION (60 sec) ==="
echo ""
echo ">>> STOP the recording in Clipper now <<<"
echo ">>> Let it generate the summary and action items <<<"
echo ""
echo "Press ENTER when you stop the recording..."
read
echo "Measuring summarization/LLM inference..."
powermetrics --samplers cpu_power -i 1000 -n 60 -o measurements/summarize_v2_${TIMESTAMP}.log
SUMMARIZE=$(grep "Combined Power" measurements/summarize_v2_${TIMESTAMP}.log | awk -F': ' '{gsub(/ mW/,"",$2); sum+=$2; count++} END {printf "%.0f", sum/count}')
echo ""
echo "✓ Summarization captured: ${SUMMARIZE} mW"

# Calculate results
echo ""
echo "=============================================="
echo "  MEASUREMENT RESULTS"
echo "=============================================="
echo ""
echo "Baseline (idle):           ${BASELINE} mW"
echo "Transcription (Whisper):   ${ACTIVE} mW"
echo "Summarization (LLM):       ${SUMMARIZE} mW"
echo ""

TRANS_INCR=$((ACTIVE - BASELINE))
SUMM_INCR=$((SUMMARIZE - BASELINE))
TRANS_W=$(echo "scale=2; $TRANS_INCR / 1000" | bc)
SUMM_W=$(echo "scale=2; $SUMM_INCR / 1000" | bc)

echo "Incremental Transcription: ${TRANS_INCR} mW (${TRANS_W} W)"
echo "Incremental Summarization: ${SUMM_INCR} mW (${SUMM_W} W)"
echo ""

# Peak analysis
TRANS_PEAK=$(grep "Combined Power" measurements/active_v2_${TIMESTAMP}.log | awk -F': ' '{gsub(/ mW/,"",$2); if($2>max) max=$2} END {print max}')
SUMM_PEAK=$(grep "Combined Power" measurements/summarize_v2_${TIMESTAMP}.log | awk -F': ' '{gsub(/ mW/,"",$2); if($2>max) max=$2} END {print max}')

echo "Peak during transcription: ${TRANS_PEAK} mW"
echo "Peak during summarization: ${SUMM_PEAK} mW"
echo ""

# Save summary
cat > measurements/summary_v2_${TIMESTAMP}.txt << SUMMARY
Clipper Power Measurement Summary
=================================
Timestamp: $(date)
Device: $(sysctl -n machdep.cpu.brand_string 2>/dev/null || echo "Apple Silicon")

POWER READINGS:
- Baseline (idle):         ${BASELINE} mW
- Transcription (avg):     ${ACTIVE} mW
- Summarization (avg):     ${SUMMARIZE} mW
- Transcription peak:      ${TRANS_PEAK} mW
- Summarization peak:      ${SUMM_PEAK} mW

INCREMENTAL POWER:
- Transcription: ${TRANS_INCR} mW (${TRANS_W} W)
- Summarization: ${SUMM_INCR} mW (${SUMM_W} W)

FOR SCI CALCULATION:
Use the higher incremental value for conservative estimate.
Grid intensity: 350 gCO2eq/kWh (IEA 2023)
SUMMARY

echo "Results saved to: measurements/summary_v2_${TIMESTAMP}.txt"
echo ""
echo "Log files:"
echo "  - measurements/baseline_v2_${TIMESTAMP}.log"
echo "  - measurements/active_v2_${TIMESTAMP}.log"  
echo "  - measurements/summarize_v2_${TIMESTAMP}.log"
