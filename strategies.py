import indicator


def spawn_indicators(df, cfg):
    strategies = cfg["vars"]["selected_strategies"]
    for strat in strategies:
        print(strat)
        indicators = cfg["strategies"][strat]["indicators"]
        indicator.create(df, indicators)
        print(indicators)