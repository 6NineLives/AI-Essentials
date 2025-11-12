# Code of Conduct

Version: 1.0

This project exists to build learning resources about AI and machine learning. We value open, constructive, and respectful participation from everyone — maintainers, contributors, and users.

## Our standards

We expect participants to:

- Be considerate and respectful in all communications.
- Use welcoming and inclusive language.
- Assume good faith: give others the benefit of the doubt and ask clarifying questions politely.
- Provide constructive feedback and focus on improving the work, not attacking people.

### Repository-specific technical expectations

In addition to general behavior, technical contributions in this repository should follow these engineering conduct principles:

- Reproducibility and clarity
	- Keep examples runnable out-of-the-box using the provided `requirements.txt` and `package.json` where applicable.
	- Prefer small, self-contained examples; document any non-obvious steps and environment needs.
	- Avoid committing large binaries or datasets. Use links to public datasets or tiny samples for demos; consider Git LFS if truly needed.
	- For notebooks, keep runtime deterministic when reasonable and minimize large cell outputs.

- Data privacy and secrets
	- Never commit secrets (API keys, tokens, credentials) or proprietary data. Use environment variables (e.g., `.env`) and add sensitive files to `.gitignore`.
	- Only use datasets you have the right to share; remove PII unless you have explicit consent and a valid reason aligned with this project.

- Licensing and attribution
	- Respect this repository’s license. Attribute any third-party code, datasets, diagrams, or text you include.
	- Do not submit plagiarized content. Summarize and cite sources where applicable.

- Benchmarks and claims
	- Be honest and transparent about performance claims. Include dataset name/version, subset size, hardware, key settings, and seeds when relevant.
	- Avoid cherry-picking results; prefer repeatable measurements.

- Security and responsible disclosure
	- Do not publicly post exploit details. Report suspected vulnerabilities privately (see Reporting and enforcement below) and give maintainers time to respond.
	- Do not introduce malicious code or dependencies.

- Model/API usage and responsible AI
	- Follow model/provider terms (e.g., OpenAI, HuggingFace, Anthropic, Azure). Do not bypass usage restrictions.
	- Avoid generating or distributing harmful content. Use guardrails and clearly label limitations and risks.
	- Be mindful of bias, safety, and misuse risks; document known limitations of examples.

## Unacceptable behavior

The following are examples of unacceptable behavior and will not be tolerated:

- Harassment, intimidation, or discrimination of any kind (including on the basis of race, gender, sexual orientation, disability, religion, age, nationality, or other protected characteristics).
- Insults, shaming, or abusive language directed at project members or contributors.
- Threats of violence or encouragement of self-harm.
- Publishing private or identifying information (doxing).
- Repeatedly posting off-topic, disruptive, or hostile content after being asked to stop.

## Reporting and enforcement

If you experience or witness unacceptable behavior, please report it to the project maintainers. On GitHub:

- Open a short issue titled `Code of Conduct Report (request private contact)` without sensitive details: https://github.com/6NineLives/AI-Essentials/issues/new
- Or open a Discussion requesting a private contact channel: https://github.com/6NineLives/AI-Essentials/discussions
- For potential security vulnerabilities, use the repository's Security tab to submit a private report if available (see `SECURITY.md`).

When a report is received, maintainers will review it and respond in a timely manner. Responses may include:

- A private conversation with the reporter and the person(s) involved to gather more information.
- Temporary or permanent removal of offending content.
- Temporary or permanent ban from the project or its communication channels.

Decisions will be made at the maintainers' discretion, guided by the goal of keeping the community safe and welcoming. We aim to acknowledge reports within 72 hours and keep reporters informed of progress where possible.

## Scope

This Code of Conduct applies to all project spaces — issues, pull requests, project discussions, community forums, chat rooms, and events related to this project.

## A note to maintainers and contributors

Maintainers should strive to enforce the code of conduct consistently, transparently, and fairly. If you are a maintainer, consider:

- Adding a real contact email and a `SECURITY.md` for vulnerability reporting.
- Cross-linking relevant sections from `CONTRIBUTING.md` (style guides, run steps, example structure).
- Setting up `.gitignore` and, if needed, Git LFS for large assets.

## Attribution

This Code of Conduct is adapted for this repository and follows common open-source community standards. If you'd like a different template (for example, the Contributor Covenant), tell me and I can swap it in and add attribution.

---

Thank you for helping keep this project welcoming and productive for everyone.