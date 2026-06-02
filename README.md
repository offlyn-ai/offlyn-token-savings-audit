# Case Study: Token Savings in Meeting Intelligence

## Summary

This case study compares two meeting-intelligence architectures:

1. A cloud-first AI notepad workflow
2. A Clipper-style local-first workflow

The goal is to measure how much cloud inference can be avoided when transcription, note enhancement, summaries, and meeting Q&A run locally first.

## Hypothesis

A local-first meeting intelligence workflow can reduce cloud token usage by 50–90% for eligible meetings while preserving quality for summaries, action items, and follow-up drafts.

## Why Clipper is a useful example

Clipper is designed as a local AI notetaker that captures audio from the Mac, transcribes locally, and processes meeting notes on device.

## What is compared

This benchmark does not claim access to proprietary internals of any third-party tool. The cloud-first baseline represents a common architecture where meeting transcripts and notes are processed primarily through cloud models.

## Metrics

- Cloud input tokens
- Cloud output tokens
- Cost per meeting
- Cost per employee per month
- Quality retention
- Privacy exposure
- Offline availability
- Local processing time

## Expected enterprise outcome

For teams with frequent meetings, local-first processing can reduce repeated cloud context, avoid unnecessary transcript uploads, and reserve cloud models for cases where they improve quality.
