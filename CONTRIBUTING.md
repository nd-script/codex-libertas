# Contributing to Codex Libertas

Thank you for your interest in contributing to Codex Libertas! We're excited to have you on board. Please take a moment to review these guidelines before making your contribution.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Reporting Issues](#reporting-issues)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
   ```bash
   git clone https://github.com/your-username/codex-libertas.git
   cd codex-libertas
   ```
3. **Set up the development environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Development Workflow

1. Create a new branch for your feature/fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes following the coding standards
3. Write or update tests as needed
4. Ensure all tests pass
5. Update the documentation if necessary

## Pull Request Process

1. Push your changes to your fork
   ```bash
   git push origin feature/your-feature-name
   ```
2. Open a Pull Request (PR) against the `main` branch
3. Ensure your PR description clearly explains the problem and solution
4. Include relevant issue numbers if applicable
5. Wait for the CI/CD pipeline to complete
6. Address any code review feedback

## Coding Standards

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use type hints for all function signatures
- Write docstrings following Google style
- Keep functions small and focused
- Write meaningful commit messages

## Reporting Issues

When creating an issue, please include:
- A clear title and description
- Steps to reproduce the issue
- Expected vs actual behavior
- Environment details (Python version, OS, etc.)
- Any relevant logs or screenshots

## License

By contributing, you agree that your contributions will be licensed under the project's [Apache 2.0 License](LICENSE).

---

Thank you for contributing to Codex Libertas! Your help is greatly appreciated.
