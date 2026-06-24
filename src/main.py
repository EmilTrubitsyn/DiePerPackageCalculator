import math

_DPP_REGISTRY = {
    0: "DDP",
    1: "DDP",
    2: "QDP",
    3: "ODP",
    4: "ODP",  # for now 4 is ODP until we get something with HDP
}

_MODULE_TYPE_REGISTRY = {
    "CAMM2": 4,
    "COMPONENT": 1,
}


def _log2(die_density: float, capacity: float, die_per_module: int) -> int:
    x = capacity * 8 / (die_density * die_per_module)
    return int(math.log2(x))


def get_dpp(ddr_type: str, capacity: float, die_density: float) -> str:
    die_per_module = _MODULE_TYPE_REGISTRY.get(ddr_type.upper())
    if die_per_module is None:
        raise ValueError(f"Unsupported DDR type: {ddr_type}")

    dpp_value = _log2(die_density, capacity, die_per_module)
    dpp = _DPP_REGISTRY.get(dpp_value)
    if dpp is None:
        raise ValueError(f"Unsupported DPP value: {dpp_value}")
    return dpp


def main() -> None:
    dpp_value = get_dpp("blaa", 24, 16)
    print(dpp_value)


if __name__ == "__main__":
    main()
