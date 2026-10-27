# Technical Architecture

## Demonstration pipeline

```text
Synthetic rice expression CSV
          |
          v
  Input validation
          |
          v
 Fold-change calculation
 (Drought / Control)
          |
          +------> Salt / Control context metric
          |
          v
 Transparent screening heuristic
          |
          v
 Ranked candidate table
          |
          v
 Researcher review / future validation
```

## Intended future architecture

```text
Curated plant genomics + transcriptomics
                 |
                 v
       Gene / pathway analysis
                 |
                 v
Validated plant-specific metabolic model
                 |
                 v
 Candidate edit hypotheses (external CRISPR tools)
                 |
                 v
Validated crop model + local soil/weather data
                 |
                 v
Scenario comparison and visual dashboard
                 |
                 v
Researcher prioritisation -> laboratory / field validation
```

## Current implementation versus roadmap

**Implemented in this repository:** CSV loading, input checks, expression fold-change calculations, a transparent heuristic ranking, and a command-line output.

**Earlier exploratory notebook components:** PyTorch Geometric graph construction, COBRApy analysis using its generic textbook benchmark model, illustrative mapping to crop parameters, and a simplified yield calculation. These are exploratory demonstrations and are not integrated into a validated rice-specific prediction pipeline.

**Not implemented/validated:** real-time IoT ingestion, 3D visualisation, a rice-specific metabolic model, APSIM/DSSAT execution, validated CRISPR guide/off-target analysis, or experimentally calibrated gene-to-phenotype predictions.

## Validation plan

1. Replace synthetic values with cited, quality-controlled datasets.
2. Validate gene IDs and annotations for the selected rice cultivar.
3. Select and document a plant-specific metabolic model.
4. Calibrate crop-model parameters with published or measured field data.
5. Evaluate predictions on held-out conditions and report uncertainty.
6. Validate promising hypotheses experimentally.
