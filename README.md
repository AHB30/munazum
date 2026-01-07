Munazum

Munazum is a Python-based CLI tool designed to safely and intelligently organise cluttered directories—such as the Downloads folder—into a clean, structured hierarchy.

It combines rule-based file classification with assistive ML suggestions, while prioritising user control, transparency, and zero-risk previews.

Munazum is intentionally conservative: it never modifies your filesystem unless you explicitly allow it.

✨ Key Features

📂 Intelligent categorisation of files (documents, archives, executables, videos, code, etc.)

🧠 Assistive ML suggestions (confidence-based, non-destructive)

🛡️ --dry-run mode for zero-risk previews

🔍 --verbose mode for full execution transparency

📦 Modern Python packaging (pyproject.toml, editable installs)

⚙️ Works on real-world messy folders (e.g. Downloads)

📁 Output Structure

When executed (without --dry-run), Munazum organises files into an Organized/ folder inside the target directory:

Organized/
├─ documents/
├─ archives/
├─ executables/
├─ videos/
├─ code/
└─ others/


Original files are copied, not deleted or moved.

🚀 Installation

Clone the repository:

git clone https://github.com/your-username/munazum.git
cd munazum


Install Munazum in editable mode:

pip install -e .


This allows you to run Munazum from any directory while continuing development.

▶️ Usage
1️⃣ Basic run (recommended first)

From any directory you want to organise:

python -m munazum run .


This will:

create an Organized/ folder

copy files into categorised subfolders

2️⃣ Dry-run mode (safe preview)

No files or folders will be created.

python -m munazum run . --dry-run


Output example:

DRY RUN — no files will be copied
Done.
ML suggestions (assistive only):


Use this to validate behaviour before real execution.

3️⃣ Verbose dry-run (recommended for first real test)

Shows every planned operation without touching the filesystem:

python -m munazum run . --dry-run --verbose


Example output:

INFO: Target folder: C:\Users\USER\Downloads
INFO: Output folder: C:\Users\USER\Downloads\Organized
INFO: Planned operations: 57

INFO: DRY-RUN: Copying file.pdf → Organized/documents/file.pdf
INFO: DRY-RUN: Copying setup.exe → Organized/executables/setup.exe


This mode is ideal for:

understanding decisions

building trust

debugging classification rules

🧠 Design Philosophy

Munazum is built on three principles:

Safety first
Nothing happens without explicit intent. --dry-run guarantees zero side effects.

Transparency over magic
Decisions are visible, logged, and explainable. ML assists—it does not override.

Real-world readiness
Designed and tested against chaotic directories, not artificial examples.

🛠️ Development Notes

Python ≥ 3.10 recommended

Packaged using pyproject.toml

Editable install supported

Flat-layout project with explicit package declaration

📌 Status

Munazum is actively developed and tested on real user data.
Future improvements may include:

confirmation prompts

ignore rules (e.g. installers, temp files)

preview-only structure creation

configurable categories

   Author

Abdullah Bahamish
Computer Science student with interests in AI, systems design, and workflow optimisation.

📄 License

MIT License (or specify your preferred license).