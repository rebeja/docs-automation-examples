# Step 5: Best practices

When to use AI for READMEs, what to always write yourself, and how to keep documentation current.

## When AI adds the most value

**New projects with no documentation**: AI gets you from zero to a complete draft in minutes. Even an imperfect first draft is better than a blank file.

**Repos with good code quality**: Well-named functions, docstrings, and clear entry points give AI more signal, leading to better output.

**Standard project types**: CLI tools, libraries, and web apps follow predictable README patterns. AI has seen thousands of examples and generates accurate structure.

**Multilingual teams**: AI drafts in any language. Use `--sections description` with a target-language instruction in the prompt to generate descriptions in French, Japanese, or Spanish.

## What to always write yourself

**Real installation verification**: Generate the install commands, then run them in a clean environment. Fix anything that does not work. Publish only tested steps.

**Accurate code examples**: AI cannot run your code. Generated examples look plausible but may have wrong argument names, incorrect output, or missing imports. Test every example.

**Security and authentication notes**: If your project handles credentials, tokens, or sensitive data, write those warnings manually. AI may omit or understate security considerations.

**Known limitations and bugs**: AI has no knowledge of open issues or known edge cases. Add these manually.

**Environment-specific instructions**: Instructions for Windows, Docker, or unusual setups require human verification.

## Signs the AI output needs more work

Watch for these patterns in generated content:

| Pattern | What it means |
|---|---|
| "This project is designed to..." (no specifics) | AI had insufficient context — add more code or a stub README |
| `pip install my-project` for a local repo | AI assumed PyPI distribution — fix to `pip install -r requirements.txt` |
| Example function calls that don't match your code | AI hallucinated — verify against actual source |
| Generic contributing text | Fine to keep, but consider linking to a real `CONTRIBUTING.md` |

## Keeping the README current

A generated README goes stale as the project evolves. Two approaches:

**Manual updates**: Regenerate individual sections when significant changes ship. Use `--sections` to target only what changed.

**Document in your workflow**: Add README review to your PR checklist or release process. A five-minute review catches most drift.

**Treat generation as a starting point**: The best README is one the maintainer understands and keeps accurate — not one that reflects perfect AI output at a single point in time.

## README quality checklist

Before publishing any generated README:

- [ ] Project name and description are accurate
- [ ] All installation steps tested in a clean environment
- [ ] Code examples run without errors
- [ ] Expected output shown matches actual output
- [ ] Security/credential notes added where relevant
- [ ] License type is correct
- [ ] Links (if any) resolve correctly
- [ ] Tone matches the project and its audience

---

## Summary

You have learned how to:

- ✓ Analyze a code repository and understand what context AI needs
- ✓ Generate a complete README section by section
- ✓ Customize prompts to improve output for specific audiences
- ✓ Use a Jinja2 template to control README layout
- ✓ Identify what AI generates reliably vs. what requires human review

The README generator works best as a starting point, not a finished product. Combine AI's speed with your knowledge of the project for documentation that is both fast to produce and accurate to publish.
