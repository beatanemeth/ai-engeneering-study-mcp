# Jupyter Notebook Setup

> If you intend to use the data preparation services, follow the steps below to configure your local environment.

---

## Getting Started 🚀

### 1. Set Up Python Virtual Environment

Ensure you have initialized your virtual environment as described in the **root `README.md`**.

---

### 2. Install Dependencies

With the **virtual environment active**, install the necessary data processing and notebook packages:

```bash
pip install pandas jupyter ipykernel
```

### 3. Register the Jupyter Kernel

A kernel is a configuration file that tells Jupyter which Python executable to use.
Registering a project-specific kernel ensures your notebooks use the dependencies installed in your virtual environment rather than the system Python.

Run the following command:

```bash
python3 -m ipykernel install --user \
  --name=ai-engineering-study-mcp \
  --display-name "Python (AI Engineering)"
```

Understanding the Flags:

| Flag             | Name        | Purpose                                   | Recommendation                                         |
| ---------------- | ----------- | ----------------------------------------- | ------------------------------------------------------ |
| `--name`         | System Name | The unique ID used by the filesystem      | lowercase-with-hyphens; must be unique on your machine |
| `--display-name` | Visual Name | The name shown in the Jupyter UI dropdown | Descriptive name (e.g. `Python (AI Engineering) 🤖`)   |

#### Managing Your Kernels

- **List Active Kernels**

To see all kernels currently recognized by Jupyter and their locations:

```bash
jupyter kernelspec list
```

- **Inspect the "Internal Blueprint"**

To verify that the kernel is pointing to the correct virtual environment path, inspect the `kernel.json` file:

```bash
# Replace the path with the output from the list command above
cat ~/.local/share/jupyter/kernels/ai-engineering-study-mcp/kernel.json
```

- **Remove a Kernel**

If you no longer need the kernel (e.g. the project is finished), uninstall it using the System Name:

```bash
jupyter kernelspec uninstall ai-engineering-study-mcp
```

## Using Jupyter ▶️

### 1. **Launch Jupyter**

```Bash
jupyter notebook
```

### 2. **Select the Kernel**

Once the Notebook opens:

- Click the kernel name in the top-right corner, or
- Navigate to Kernel → Change Kernel
- Then select: `Python (AI Engineering)`

## Shutting Down 🛑

When you are finished working, follow these steps to cleanly close your session:

### 1. Stop the Jupyter Server

Instead of using terminal shortcuts, it is often more reliable to shut down directly from the browser:

- **Save** your work in any open Notebooks.
- Go to the main Jupyter dashboard (the file list tab).
- **File > Shut Down**

### 2. Deactivate the Virtual Environment

Once the server has stopped, return to your terminal and run:

```bash
deactivate
```

---

---

## Jupyter Cleanup & Git Hygiene 🧹

> This project uses `nbstripout` to keep notebook outputs out of version control.

- [kynan/nbstripout](https://github.com/kynan/nbstripout)
- [pre-commit/pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)

Follow these steps in your project terminal with your `.venv` active:

### 1. Configure the Notebook "Filter"

This handles the automatic stripping of cell outputs (prints, graphs, etc.) whenever you `git add`.

```Bash
pip install nbstripout
nbstripout --install
```

### 2. Create the Configuration File

Create a file named `.pre-commit-config.yaml` in your root directory.

### 3. Initialize the Manager

This installs the "hooks" into your local `.git` folder so they run automatically on every commit.

```Bash
pip install pre-commit
pre-commit install
```

### 4. The Final Verification (Optional)

Run this to check your existing files for issues before your next commit. If a notebook has outputs, this command will clean them for you right now.

```Bash
pre-commit run --all-files
```
