# OpenClaw Prompt Injection Benchmark

A community-driven, "living" benchmark for documenting and researching prompt injection vulnerabilities in agentic systems like OpenClaw.

## What is this?

As AI agents become more autonomous—reading files, browsing the web, and managing their own long-term memory—they become susceptible to **Indirect Prompt Injection**. This occurs when an agent encounters malicious instructions hidden within the data it processes (like a webpage, a document, or a social media post).

This repository serves as a structured library of reproducible attack cases. Instead of static text datasets, we focus on **scenarios** that demonstrate how an agent can be tricked into violating its system instructions, leaking data, or performing unauthorized actions.

## Goals

- **Standardize Scenarios**: Provide a common format for sharing and reproducing complex injection attacks.
- **Map Attack Surfaces**: Categorize attacks by their entry point (Local Files, Web, Skills, Memory, etc.).
- **Track Model Resilience**: Document which models (e.g., GPT-4, Claude 3.5, GPT-OSS) are vulnerable to specific techniques.
- **Enable Defensive Research**: Help developers build better guardrails by providing a "Gauntlet" of known exploits to test against.

## Repository Structure

```text
openclaw-prompt-injection/
├── attacks/
│   └── SRC-FILE/               # Attacks via local files (HTML, TXT, PDF, etc.)
│   # New categories (SRC-WEB, SRC-SKILL, etc.) are added as cases are submitted.
├── scripts/
│   └── update_leaderboard.py    # Automated script to maintain the Hall of Fame
├── ATTACK_SPEC.md              # Detailed metadata schema for submissions
├── CONTRIBUTING.md             # How to add your own attack cases
├── LEADERBOARD.md              # The "Hall of Fame" of verified attacks
├── LICENSE                     # MIT License
└── SECURITY.md                 # Safety and responsible use policy
```

## Attack Categories (by Source)

We categorize attacks by the **entry point** to help researchers understand the threat model:

| Category | Source | Description | Example |
| :--- | :--- | :--- | :--- |
| **SRC-FILE** | **Local File** | Payloads in local files the agent is asked to read. | An `index.html` with hidden instructions in a white-on-white `div`. |
| **SRC-WEB** | **Web / URL** | Payloads fetched during `web_search` or browsing. | A blog post that tricks the agent into exfiltrating session data. |
| **SRC-SKILL** | **Skill / Tool** | Malicious instructions hidden in a tool's manifest or README. | A "Helper Skill" that requests unauthorized `sudo` access. |
| **SRC-SOUL** | **Memory (SOUL.md)** | Poisoned long-term memory that triggers in a future session. | A "sleeper" command saved in the agent's persistent memory. |
| **SRC-FEED** | **Social Feed** | Payloads encountered while autonomously monitoring feeds. | A post that tricks the agent into "liking" or "reposting" it. |

## How to Use This Benchmark

1.  **Explore**: Browse the `attacks/` directory to see real-world examples of how agents are being exploited.
2.  **Test**: Use the `trigger_prompt` and `payload` from a case to see if your own agent or model is vulnerable.
3.  **Contribute**: If you find a new way to inject instructions, follow the [CONTRIBUTING.md](CONTRIBUTING.md) guide to add it to the library.

## Verification & Leaderboard

This project features an automated **Hall of Fame** ([LEADERBOARD.md](LEADERBOARD.md)). When a new attack case is verified and merged into the repository, the leaderboard is automatically updated to credit the author and track the vulnerabilities.

## Safety First

This repository is for **defensive research only**. Please read our [SECURITY.md](SECURITY.md) before using or submitting payloads. Never test these attacks on systems you do not own.

---
*Licensed under the MIT License.*
