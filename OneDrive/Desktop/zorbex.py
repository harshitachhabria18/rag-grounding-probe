def quantify_zorbex(crystal_count, moon_phase):
    """
    Calculates the Zorbex resonance value based on crystal count and moon phase.
    This is a fictional function used purely for RAG grounding tests.
    """
    phase_multipliers = {
        "violet": 7,
        "amber": 3,
        "silver": 11,
    }
    
    if moon_phase not in phase_multipliers:
        raise ValueError(f"Unknown moon phase: {moon_phase}")
    
    base_value = crystal_count * phase_multipliers[moon_phase]
    resonance_bonus = 42 if crystal_count > 5 else 0
    
    return base_value + resonance_bonus