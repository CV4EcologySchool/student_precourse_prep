# Session 1: cohort kickoff and setup

The meeting itself is mainly for introductions, program context, and learning who is in the group. The technical exercise is a short follow-up.

## Casual introduction

Be ready to share 2 slides introducing you and your project: focus on the ecological question you work on and what you look to accomplish at the workshop. 
It's also a good idea to include some data samples!

This is an informal intro to a friendly small crowd.

## After the meeting: technical check

1. Install uv, VS Code, and the VS Code Python and Jupyter extensions if needed.
2. Open the entire `prep` folder in VS Code.
3. Create the environment with `uv sync`, as described in the top-level `README.md`.
4. Run the setup check from the `prep` directory:

   ```bash
   uv run python 01_kickoff_and_setup/check_setup.py
   ```

5. Open `demo_python_cells.py` and make the three small changes marked `TODO`.
6. Run it from VS Code and from the terminal:

   ```bash
   uv run python 01_kickoff_and_setup/demo_python_cells.py
   ```

If you run into issues, message your instructor with the details!

## Optional: set up a coding agent

A coding agent can inspect files in a project, explain errors, suggest changes,
and run commands. The exact setup depends on the tool, so these steps are
deliberately generic:

1. Choose a coding agent (e.g., Codex or Claude Code). Use its
   official installation instructions to install the app, command-line tool, or
   VS Code extension and sign in if required.
2. Open the `prep` folder as the agent's workspace. Do not give it access to a
   broader folder than it needs.
3. Start with a read-only request, such as:

   > Read `01_kickoff_and_setup/README.md` and tell me what I need to complete.
   > Do not edit any files or run commands.

4. Check that its answer matches this page. Then ask it to explain one `TODO` in
   `demo_python_cells.py` without completing the exercise for you.

Treat the agent as a collaborator, not an authority. Read proposed commands and
file changes before approving them, run the setup check yourself, and make sure
you can explain the code you submit. Never paste passwords, API keys, unpublished
research data, or other sensitive information into a coding agent. 

## Extra reading

The official [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial) explains the three pieces that often cause confusion: VS Code is the editor, the Python extension connects the editor to Python, and the Python interpreter runs the code. Use it for setup help; completing the whole tutorial is not required.
