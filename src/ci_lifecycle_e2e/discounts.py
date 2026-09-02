"""Volume discount tiers for the synthetic catalog."""

TIER_THRESHOLDS = ((100, 15), (50, 10), (20, 5))


def discount_percent(subtotal: int) -> int:
    for threshold, percent in TIER_THRESHOLDS:
        if subtotal >= threshold:
            return percent
    return 0


def total_cents(subtotal: int) -> int:
    return subtotal * (100 - discount_percent(subtotal))
