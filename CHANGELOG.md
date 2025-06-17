
## [v0.0.1] - 2025-06-17
### Changes
- Set up initial project structure: Created the basic layout with lovelace_os, tests, docs, and configuration files
- Integrated OpenAI API: Implemented ai_core.py for querying GPT-4o and processing user inputs
- Implemented ethical decision-making logic: Added philosophical_core.py with basic ethical frameworks (utilitarianism, deontology)
- Created Flask web app: Set up web/app.py with /ask endpoint to handle user queries and return AI and ethical decisions
- Configured setup.cfg: Added metadata, dependencies, and entry points for the project
- Added release.sh script: Automated versioning and release process, including GitHub tag creation and release uploads
- Created pyproject.toml: Defined build system with setuptools and wheel for modern packaging
- Updated requirements.txt: Added necessary dependencies such as openai, flask, and pytest for testing
- Implemented initial tests: Added unit tests for ai_core.py and philosophical_core.py in test_ai_core.py and test_philosophical_core.py
Initial commit

