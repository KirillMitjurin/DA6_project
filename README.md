# F8_project
## Blackjack Simulation and Strategy Testing

## Overview

This project is a comprehensive simulation of blackjack games, utilizing machine learning models to simulate optimal decisions based on pre-defined strategies and rules. The project integrates logic-based decision-making with model predictions to evaluate outcomes of blackjack hands. The simulation is flexible, handling scenarios like soft hands, splits, doubles, and reshuffles.

### Key Features
- Simulates blackjack games with realistic rules (reshuffling, card drawing, etc).
- Implements logic-based decisions for taking cards, splitting, and doubling.
- Machine learning models (Random Forest) are trained on Kaggle data for predictions.
- Tracks wins, losses, ties over multiple simulations.
- Supports both logical and model-driven decision-making for comparison.

---

## Dataset

The data used to train the models is sourced from Kaggle (https://www.kaggle.com/datasets/mojocolors/900000-hands-of-blackjack-results). It contains features related to blackjack gameplay, including:
- Player cards, dealer cards, and sums.
- Game outcomes like win/loss, busts, and pushes.

The dataset has been modified to extract key features. Some of them:
- `ply2cardsum`: Sum of the player's initial two cards.
- `dealcard1`: Dealer's visible card.
- `soft_hand`: Indicator for a "soft" hand (presence of an Ace valued as 11).

---

## Code Functionality

### Blackjack Simulation

The simulation runs multiple games of blackjack, keeping track of:
- Player's decisions (stand, take card, split, double).
- Dealer's decisions based on standard blackjack rules.
- Game outcomes and balance changes.

---

### Decision Logic

#### Logic-Based Decisions
- **Take a Card**: Based on `ply2cardsum`, `dealcard1`, and `soft_hand`.
- **Split**: Decides to split pairs (e.g., 8s or Aces) based on dealer card.
- **Double**: Combines doubling logic with take-card decisions for optimization.

#### Machine Learning Predictions
- Trained models predict optimal actions (`take_card`, `split`, `double`):
  - Random Forest Classifier used for `take_card`, `split`, and `double`.
  - Trained on Kaggle dataset to predict decisions for any hand.

---

## Models

### Training
The machine learning models are trained using the following features:
- Player cards (`card1`, `card2`).
- Player's initial two-card sum (`ply2cardsum`).
- Dealer's visible card (`dealcard1`).
- Whether the hand is soft (`soft_hand`).

### Predictions
- **`take_card`**: Predicts whether the player should take a card and when to double.
- **`split`**: Determines if splitting pairs is advantageous.

---

## Usage Instructions

### Prerequisites
- Python 3.x
- Required libraries: pandas, numpy, scikit-learn, seaborn, matplotlib.

### Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/KirillMitjurin/IDS6_project.git
   cd IDS6_project
