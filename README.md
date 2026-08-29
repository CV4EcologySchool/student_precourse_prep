# CV4Ecology student guide

This is a lightweight six-session preparation sequence for the January CV4Ecology workshop. It focuses on practical Python, understanding ecological data, Git, and the basic idea of remote computing. Computer-vision modeling remains in the course itself.

This README and the numbered session folders are for students.

## Sessions

| Session | Timing | Focus | Main student result |
|---|---|---|---|
| 1 | September | Cohort kickoff and setup | Meet the group; complete the setup check afterward |
| 2 | October | Python, files, and media | Find and display supplied media with Python |
| 3 | Early November | Exploratory analysis of your data | Inspect your own metadata and bring one useful plot and data question |
| 4 | Late November | Media, labels, and dataset objects | Visualize your own labels on several samples and build a small dataset class |
| 5 | Early December | Git and remote computing | Make one Git-tracked change; understand an SSH login |
| 6 | Mid/late December | Individual data-subset planning | Agree with instructors on a manageable, representative working subset and next steps |

Core work outside a meeting should take no more than 30–45 minutes. Optional sections are genuinely optional.

## Setup

Start with [`01_kickoff_and_setup/README.md`](01_kickoff_and_setup/README.md).

The exercises use Python 3.12 and these packages:

- NumPy
- Pandas
- Matplotlib
- Pillow
- IPython kernel (to run the notebooks)

### 1. Install uv

uv manages Python and the packages for these exercises, so you do not need to create an environment with `venv` or install packages with `pip`.

On macOS or Linux, open a terminal and run:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows, open PowerShell and run:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Restart the terminal after installation, then confirm that uv is available:

```bash
uv --version
```

If these commands are blocked on a managed computer, see the [official uv installation options](https://docs.astral.sh/uv/getting-started/installation/) or ask an instructor.

### 2. Create an environment

Open a terminal in this `prep` directory and run:

```bash
uv sync
```

This creates a local `.venv`, installs Python 3.12 if needed, and installs the locked dependencies. Check the setup with:

```bash
uv run python 01_kickoff_and_setup/check_setup.py
```

Use `uv run python ...` for the other Python scripts. Activating the environment is optional because `uv run` uses it automatically.

### 3. Choose the notebook kernel in VS Code

After running `uv sync`:

1. In VS Code, use **File: Open Folder** to open the `prep` folder that contains `pyproject.toml`. Open this folder directly, not its parent folder.
2. Install the recommended **Python** and **Jupyter** extensions if VS Code prompts you. This repository is configured to use its existing `.venv` automatically.
3. Open an `.ipynb` notebook. If `.venv (Python 3.12)` is already shown in the upper-right corner, start running cells.
4. If VS Code shows **Select Kernel**, choose **Select Another Kernel...**, then **Python Environments**, then `.venv (Python 3.12)`.

Do **not** choose **Create Environment**. `uv sync` has already created the environment and installed its packages.

To confirm that the correct kernel is running, execute this in a notebook cell:

```python
import sys
import matplotlib

print(sys.executable)
print(matplotlib.__version__)
```

The first printed line should contain `prep/.venv` on macOS/Linux or `prep\.venv` on Windows. The second line should show the installed Matplotlib version. If `.venv` is not listed, run `uv sync` again, then use **Developer: Reload Window** from the VS Code Command Palette and reopen the kernel picker.

## License

Source code and notebook code cells are available under the [MIT
License](LICENSE). Original written educational materials, notebook narrative,
and landmark annotation CSV files are available under [CC BY
4.0](LICENSE-CONTENT.md). The landmark annotations are copyright Tel Aviv
University; the written educational materials and notebook narrative are
copyright Massachusetts Institute of Technology and California Institute of
Technology.

The J.E. Randall fish photographs are third-party materials provided with the
kind permission of the Bishop Museum for research and educational use. They
are not covered by either repository license. See
[`ATTRIBUTION.md`](ATTRIBUTION.md) for details.
