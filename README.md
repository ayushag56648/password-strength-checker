# Enterprise Password Security & Enforcement Tool

A command-line security utility designed to enforce enterprise-grade password policies. It combines entropy-based strength scoring with privacy-preserving data breach detection and demonstrates secure cryptographic storage.

## Features
* **Entropy-Based Scoring:** Replaces naive regex checks with the `zxcvbn` library to accurately estimate offline crack times and contextual predictability.
* **Privacy-Preserving Breach Detection:** Integrates with the HaveIBeenPwned API using a **k-Anonymity model**. Passwords are never transmitted; only the first 5 characters of a local SHA-1 hash are sent over the network.
* **Dynamic Policy Engine:** Uses a `policy.json` configuration file to enforce minimum strength scores and acceptable breach thresholds, simulating an IAM enforcement mechanism.
* **Secure Credential Storage:** Demonstrates proper cryptographic storage by generating salted hashes using `bcrypt`.

## Installation

1. Clone the repository and navigate into the directory.
2. Create and activate a clean virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate