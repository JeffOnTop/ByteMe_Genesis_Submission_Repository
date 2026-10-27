[README.md](https://github.com/user-attachments/files/34028798/README.md)
# Generative Bio-Digital Twin (Byte Me)

An early-stage computational proof of concept exploring how biological and environmental data could be combined to support climate-resilient crop research.

## What this repository currently demonstrates

- A small **synthetic** rice gene-expression dataset under control, drought and salt conditions.
- Basic drought-response screening using expression changes.
- A transparent, illustrative candidate-ranking calculation.
- A simple crop-response scenario calculation using user-defined assumptions.
- A modular starting point for later integration with validated plant models and real datasets.

> **Important:** This is a demonstration prototype, not a validated biological digital twin. The included data are synthetic. Scores are screening indicators, not evidence that a gene edit will improve drought tolerance or yield. The current demo does not perform real CRISPR guide validation, does not use a rice-specific metabolic model, and does not run APSIM/DSSAT.

## Run in Google Colab

1. Open `prototype.py` in this repository or download the repository ZIP.
2. In Colab, upload `prototype.py` and `data/rice_expression_demo.csv`, then run:

```python
!pip install -r requirements.txt
!python prototype.py --data data/rice_expression_demo.csv
```

Alternatively, clone the repository in a Colab cell:

```python
!git clone https://github.com/Mohini20088002/animated-diva.git
%cd animated-diva
!pip install -r requirements.txt
!python prototype.py --data data/rice_expression_demo.csv
```

## Run locally

```bash
python -m pip install -r requirements.txt
python prototype.py --data data/rice_expression_demo.csv
python -m unittest discover -s tests -v
```

Python 3.9+ is recommended.

## Input data format

CSV columns: `Gene_ID`, `Control`, `Drought`, `Salt`. Values in the included file are synthetic expression units created only for demonstrating the workflow.

## Workflow

1. Load expression data.
2. Calculate drought response as `(Drought - Control) / Control`.
3. Apply a simple drought-response screening threshold.
4. Rank candidates using the drought response and a transparent illustrative penalty for large salt-condition decreases.
5. Print a scenario table for further researcher review.

## Repository structure

- `prototype.py` — runnable demonstration pipeline.
- `data/rice_expression_demo.csv` — synthetic sample dataset.
- `tests/test_prototype.py` — basic automated tests.
- `docs/ARCHITECTURE.md` — system design and boundaries.
- `requirements.txt` — Python dependencies.
- `LICENSE` — MIT licence.

## Limitations and next steps

- Replace synthetic expression values with curated, cited experimental datasets.
- Validate gene identifiers and gene functions against authoritative rice databases.
- Use a rice-specific metabolic model before interpreting metabolic effects.
- Validate crop simulations using APSIM/DSSAT with appropriate cultivar, soil and weather parameters.
- Use established CRISPR design tools and off-target assessment; the current demo does not design or validate guides.
- Compare model outputs with laboratory and field observations before making biological claims.

## Team

**Byte Me** — Genesis Ideathon  
Problem area: Generative Bio-Digital Twin for climate-resilient crop research.
