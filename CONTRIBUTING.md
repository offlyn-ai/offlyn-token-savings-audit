# Contributing to Offlyn AI Resource Avoidance Audit

We welcome contributions that improve the accuracy, coverage, and enterprise applicability of this audit framework.

## Ways to Contribute

### Assumptions and Data
- Improve default values in `assumptions/` with better sources or measurements
- Add real-world workload profiles for different meeting types and industries
- Contribute carbon intensity factors for additional cloud regions

### New Workflow Models
- Extend the framework to new AI workflow types (see `assumptions/workflows.yml` for planned areas)
- Add document Q&A, code review, or field operations models
- Propose new functional units for SCI-AI reporting

### Calculator Improvements
- Improve calculation accuracy with better models
- Add support for additional cloud providers or local hardware
- Optimize for new architecture patterns (e.g., speculative local + cloud verify)

### Enterprise Use Cases
- Share anonymized benchmark results from real deployments
- Propose new reporting dimensions relevant to your industry
- Suggest FinOps/GreenOps dashboard integration patterns

## How to Submit

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-improvement`)
3. Ensure all tests pass (`python -m pytest tests/`)
4. Update assumptions sources and methodology docs if changing calculations
5. Submit a pull request with a clear description of what and why

## Guidelines

- All assumptions must have documented sources or clearly state "estimated" with rationale
- Follow the claims policy in `analysis/claims_policy.md` — no greenwashing
- New calculations should include unit tests
- Maintain backward compatibility with existing assumption files
- Use the incremental energy model (not total device power) for carbon accounting

## Enterprise Contributions

If your organization wants to contribute proprietary workload data or request custom modeling:
- Contact: [hello@offlyn.ai](mailto:hello@offlyn.ai)
- We can work under NDA for sensitive data
- Anonymized insights may be incorporated into public defaults with permission

## Code of Conduct

Be respectful, precise, and evidence-based. This is a sustainability tool — accuracy and honesty matter more than optimistic numbers.

## License

By contributing, you agree that your contributions will be licensed under Apache License 2.0.
