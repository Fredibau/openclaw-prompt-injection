# Contributing to OpenClaw Prompt Injection Benchmark

We welcome contributions of new prompt injection attack cases! This benchmark is a community effort to document vulnerabilities in agentic systems.

## How to Contribute a New Attack

1. **Fork the Repository**: Create your own copy of the repo.
2. **Create a Case Directory**: Choose the correct source category under `attacks/` (e.g., `SRC-FILE`, `SRC-WEB`). If the category folder doesn't exist yet, feel free to create it!
3. **Add the Payload**: Place the malicious file (HTML, TXT, etc.) in your folder.
4. **Create `meta.yaml`**: Follow the schema in [ATTACK_SPEC.md](/ATTACK_SPEC.md). Make sure to include:
   - A unique ID.
   - The tested models.
   - The **trigger prompt** (use `[FILEPATH]` or `[URL]` as placeholders).
5. **Add a README.md**: (Optional but recommended) Explain how the attack works and how to reproduce it.
6. **Submit a Pull Request**: Once merged, the leaderboard will update automatically.

## Submission Rules

- **No Real Secrets**: Never include real API keys or credentials.
- **Reproducibility**: Ensure the attack is reproducible against the models you list.
- **Ethical Use**: This benchmark is for defensive research. Do not use these attacks against systems you do not own.

Thank you for helping make AI agents more secure!

