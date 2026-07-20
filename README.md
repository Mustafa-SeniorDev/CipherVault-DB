# ZK-Verifier Point-Validation Checker

## Summary

An open-source detection tool for a recurring vulnerability class in ZK-verifier implementations: missing on-curve and subgroup-membership validation for elliptic-curve points (e.g. BN254 G1/G2) accepted as proof inputs.

This tool grew out of independent research into zkVerify's `read_g2` function and Zeko Protocol's authorization logic — both cases where security-critical validation was silently missing without causing an obvious failure.

**Status:** Early development · Scaffold and detection logic in progress

## Motivation

Pairing-based commitment schemes (KZG and similar) are foundational to zk-Rollups, zk-coprocessors, and cross-chain ZK bridges. Their soundness depends on every input point being validated as on-curve and in the correct prime-order subgroup — a check that is easy to omit and rarely covered by standard unit tests. This tool lets any team building ZK-verifier pallets or libraries check their own code for this gap.

## Planned Scope

- [ ] Static analysis pass for Rust/Arkworks codebases: flag point-deserialization functions lacking `is_on_curve()` / subgroup-check calls
- [ ] Static analysis pass for Substrate pallets using similar deserialization patterns
- [ ] Dynamic test-vector generator: off-curve and non-subgroup BN254 points for use against live/testnet verifier instances
- [ ] CLI tool (`cargo run -- check <path>`) with human-readable findings output
- [ ] Documentation and worked examples, including the original zkVerify `read_g2` case

## Background Research

This tool is informed directly by two confirmed/ongoing findings:
- [zkVerify BN254 Point-Validation Research](https://github.com/Mustafa-SeniorDev/zkVerify-BN254-PointValidation-Research)
- [Zeko Protocol Fee-Payer Authorization Research](https://github.com/Mustafa-SeniorDev/Zeko-Protocol-FeePayer-Authorization-Research)

## License

MIT — freely usable and extensible by any team in the ZK ecosystem.

## Author

**Mustafa Ramadhani** — Independent security researcher, Dar es Salaam, Tanzania
Focus: ZK protocol security & smart contract auditing (Immunefi ecosystem)
📫 Mustafarama405@gmail.com · [LinkedIn](https://www.linkedin.com/in/mustafa-ramadhani-59394b354)
