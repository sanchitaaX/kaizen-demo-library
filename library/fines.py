"""Late fees. The desk sets the fee rule on its settings screen, for example "days * 0.25"."""

DEFAULT_RULE = "days * 0.25"


def late_fee(days, rule=DEFAULT_RULE):
    """The fee for a book returned `days` late, worked out with the desk's fee rule."""
    if days <= 0:
        return 0.0
    return round(float(eval(rule, {}, {"days": days})), 2)
