# Loopy

Learning to shape software from scratch, by hand, one project at a time.

## What

A handcrafted event loop written in Python.

## Why

To understand how things work by implementing them myself :)

Through this project, I want to explore:

- Why cooperative multitasking can be more efficient than OS-managed thread scheduling.
- Why event loops are well suited for I/O-bound tasks but generally less effective for CPU-bound tasks.
- How the kernel provides the mechanisms that enable asynchronous I/O.

## Dependencies & Usage

- Python `3.12` (see `.python-version`), managed with [uv](https://docs.astral.sh/uv/).
- No runtime dependencies; the only dev dependency is `pytest`.
- Optional: a Nix flake is provided. Enter the dev shell with `nix develop` (or automatically via `direnv`).

```sh
uv sync                    # create .venv and install dev dependencies
uv run pytest              # run the test suite
uv run main.py             # run the event loop demo
```

## Disclaimer About AI Usage

- Most of the code in this repository is written AI-free (handcrafted). I use LLMs as instructors to guide me toward the prerequisites and concepts I need to understand.
- All implementation decisions and code are my own. The LLMs I used were explicitly instructed not to provide any code implementations or even define interfaces or APIs for the project.
- LLMs helped me identify relevant design questions that would influence the implementation and the project's features.
- They also pointed me toward similar projects, which I had to read and study to gather inspiration.
- On rare occasions, I used LLMs to help in a debugging session when I got stuck.
