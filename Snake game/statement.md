# Project Statement: Snake - Algorithm Arena

## Course Details
- **Course Code**: CSE1021
- **Course Title**: Problem Solving and Programming (Flipped Course)
- **Academic Program**: B.Tech, Vellore Institute of Technology (VIT Bhopal University)
- **Submission Target**: VITyarthi Evaluated Course Project

---

## 1. Problem Statement
First-year computer science students often encounter programming concepts—such as 2D coordinate systems, vector math, state machines, list processing, pseudo-random number generation, and in-place sorting—in isolation through disparate textbook examples. Without synthesizing these principles into a coherent, interactive software architecture, understanding how data structures govern dynamic runtime behavior remains abstract.

**Snake: Algorithm Arena** addresses this pedagogical gap by building a robust, modular, and fully deterministic grid-based simulation game. The system models the snake body as an ordered, mutable sequence of discrete 2D coordinates, evaluates spatial boundary and self-collision constraints, implements pseudo-random food placement with reproducible seed support, dynamically modulates game speed based on player progress, and ranks historic performances using an explicit, human-auditable **Insertion Sort** algorithm.

---

## 2. Project Scope

### In-Scope (Implemented & Demonstrable):
1. **Core Grid Simulation**: Discrete 20x20 grid coordinate system with cell mapping and vector-based direction changes.
2. **Deterministic Movement & Growth**: Head advancement, tail management, and body elongation upon food consumption.
3. **Dual-Mode Collision Engine**: Constant-time boundary checks O(1) and linear-time self-collision checks O(n) with tail-vacation awareness.
4. **Reproducible Food Generation**: Candidate free-cell set difference and pseudo-random placement with optional seed configuration.
5. **Dynamic Difficulty & Scoring**: Three baseline presets (Easy, Medium, Hard) with food point multipliers and threshold-based tick acceleration.
6. **Explicit Leaderboard Ranking**: Top-10 historical score management sorted via an explicit Insertion Sort algorithm.
7. **Robust Persistence Layer**: Defensive JSON serialization with automatic recovery against missing or malformed data files.
8. **Dual Execution Interfaces**: Hardware-accelerated 2D graphical display using Pygame-CE, alongside an interactive, dependency-free terminal ASCII mode.
9. **Headless Verification**: Full CLI self-test suite (--self-test) validating all functional requirements without GUI dependencies.

### Out-of-Scope:
- Multi-threaded network multiplayer or socket synchronization.
- External database server dependencies (e.g., PostgreSQL, MongoDB).
- Complex physics engines or continuous floating-point collision curves.

---

## 3. Target Users
1. **Student / Player**: Engages with the game to test reflexes, observe algorithmic game dynamics, and achieve high scores.
2. **Faculty Evaluator / Assessor**: Evaluates technical modularity, syllabus adherence, automated test execution, and code architecture from the command line.
3. **Student Developer / Maintainer**: Inspects clean, modular code units for educational reference, algorithm benchmarking, and future feature extension.

---

## 4. High-Level Features
- **Deterministic Seed Mode (--seed <INT>)**: Guarantees identical pseudo-random food sequences for repeatable testing.
- **Opposite Direction Rejection**: Mathematically filters 180-degree vector inversions to prevent accidental immediate suicide.
- **Headless CLI Diagnostics**: Single command self-test verifying 13 distinct functional and boundary requirements with structured output.
- **Persistent Hall of Fame**: Transparent in-memory sorting and JSON disk persistence with defensive error handling.
