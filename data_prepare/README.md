# Jupyter Notebook Setup

> If you only want to use the **Jupyter Notebook** environment independently, follow the steps below.

---

## Getting Started 🚀

### 1. Set Up Python Virtual Environment

Ensure you have initialized your virtual environment as described in the **root `README.md`**.

---

### 2. Install Dependencies

With the virtual environment active, install all necessary packages in a single command.

```Bash
# Navigate to the Directory
cd data_prepare/

# Update pip
python -m pip install --upgrade pip

# Install the Packages
pip install -r requirements.txt
```

ℹ️ The `requirements.txt` file contains **all dependencies required** for this notebook environment:
`jupyter`, `pandas`, `ipykernel`, `nbstripout`.

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

With the virtual environment active:

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

Instead of relying on terminal shortcuts, it’s usually more reliable to shut down directly from the browser UI:

- **Save** your work in any open Notebooks.
- Go to the main Jupyter dashboard (the file list tab).
- **File > Shut Down**

### 2. Deactivate the Virtual Environment

Once the server has stopped, return to your terminal and run:

```bash
deactivate
```

Your command prompt will return to its default state, and the environment name (`.venv`) will disappear.

---

---

## Jupyter Cleanup 🧹

> This project uses `nbstripout` to keep notebook outputs out of version control.

- [kynan/nbstripout](https://github.com/kynan/nbstripout)

The `nbstripout` package is included in the `requirements.txt` file, and is installed with all other packages as described above.

The file named `.pre-commit-config.yaml` contains the necessary configurations.
