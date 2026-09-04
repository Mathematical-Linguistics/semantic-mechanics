#!/usr/bin/env python3
"""
lifecycle.py
A computational mechanics model tracking the economic lifecycle of semantic tokens:
Minting -> In-Group Liquidity -> Mainstream Arbitrage -> Inflation/Debasement -> Inversion/Reclamation.
"""

import math

class SemanticToken:
    def __init__(self, term: str, origin_domain: str, initial_capital: float = 1.0):
        self.term = term
        self.origin_domain = origin_domain
        self.capital = initial_capital       # In-group symbolic value
        self.institutional_adoption = 0.0    # Commercial / corporate / academic capture [0, 1]
        self.entropy = 1.0                   # Semantic sharpness (lower = denser meaning)
        self.inverted = False
        self.inverted_term = None

    def step(self, commercial_pressure: float):
        """Advances the token dynamics by one epoch."""
        if not self.inverted:
            # Mainstream adoption grows under commercial pressure
            self.institutional_adoption = min(1.0, self.institutional_adoption + commercial_pressure * 0.15)
            # In-group capital decays as mainstream adoption increases (loss of signaling utility)
            self.capital = max(0.05, self.capital * (1.0 - 0.22 * self.institutional_adoption))
            # Semantic entropy rises (meaning becomes diluted / generic)
            self.entropy += 0.3 * self.institutional_adoption

            # When capital drops below threshold and adoption is saturated, inversion triggers
            if self.capital < 0.25 and self.institutional_adoption > 0.70:
                self.invert()
        else:
            # Reclaimed token accumulates fresh subcultural equity
            self.capital = min(2.5, self.capital * 1.25)
            self.entropy = max(0.8, self.entropy * 0.90)

    def invert(self):
        """Flips polarity to reclaim semantic agency."""
        self.inverted = True
        self.inverted_term = f"reclaimed({self.term})"
        self.institutional_adoption = 0.05
        self.capital = 1.8
        self.entropy = 0.9

def simulate_token_dynamics(token_name: str, domain: str, epochs: int = 8):
    token = SemanticToken(token_name, domain)
    history = []
    
    print(f"=== Simulating Semantic Mechanics for: '{token_name}' ({domain}) ===")
    print(f"{'Epoch':<6} {'State':<18} {'Capital':<10} {'Adoption':<10} {'Entropy':<10} {'Action'}")
    print("-" * 65)

    for ep in range(1, epochs + 1):
        state_label = token.inverted_term if token.inverted else token.term
        action = "Reclaimed (Inversion Triggered!)" if (token.inverted and ep > 1 and not history[-1]['inverted']) else "Circulating"
        
        print(f"{ep:<6} {state_label:<18} {token.capital:<10.2f} {token.institutional_adoption:<10.2f} {token.entropy:<10.2f} {action}")
        
        history.append({
            'epoch': ep,
            'term': state_label,
            'capital': token.capital,
            'adoption': token.institutional_adoption,
            'entropy': token.entropy,
            'inverted': token.inverted
        })
        
        token.step(commercial_pressure=0.85)

    print("-" * 65 + "\n")
    return history

if __name__ == "__main__":
    simulate_token_dynamics("sick/ill", "Vernacular (AAVE/Hip-Hop)")
    simulate_token_dynamics("fluxions", "Calculus Representation Wars (1690-1730)")
