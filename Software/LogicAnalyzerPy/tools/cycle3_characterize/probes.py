"""Named inert/hostile probe inventory.  It imports no fixtures or outputs."""

PROBES = frozenset(
    {
        "valid",
        "hang",
        "ignore_term",
        "partial",
        "extra",
        "nonfinite",
        "stderr",
        "stdout_noise",
        "malformed",
        "stdout_flood",
        "stderr_flood",
        "diagnostic_flood",
        "text_cap",
        "binary_cap",
        "large_result",
        "deep",
        "items",
        "nested_items",
        "unknown",
        "base64",
        "limits",
        "recursion_over",
        "raise_address_space",
        "address_space_over",
        "bytecode",
        "address_space_over",
    }
)
