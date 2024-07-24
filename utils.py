import json
import os
import MetaTrader5 as mt5
import indicator
import pandas
import mt5_lib
import strategies

def start_client(cfg):
    boot_terminal = start_terminal(cfg)
    if not boot_terminal:
        print(f"Failed to start Terminal, error code =", mt5.last_error())
    return boot_terminal


def load_candles(cfg):
    project_symbols = cfg["mt5"]["symbols"]
    all_candles = {}
    for s in project_symbols:
        init_symbol = mt5_lib.init_symbols(s)
        if init_symbol:
            candles = retrieve_candles(cfg, s)
            all_candles[s] = candles
    return all_candles


def retrieve_candles(cfg, s):
    candles = mt5_lib.get_candles(
        symbol=s,
        timeframe=cfg["mt5"]["timeframe"],
        amount=cfg["vars"]["candle_lookback"]
    )
    pandas.set_option('display.max_columns', None  )
    return candles

def get_cfg(path="cfg/cfg.json"):
    if os.path.exists(path):
        f = open(path, "r")
        parameters = json.load(f)
        f.close()
        return parameters
    else:
        raise ImportError("Failed to read configuration.")


def start_terminal(config):
    try:
        startup_status = mt5_lib.start_mt5(config)
    except Exception as e:
        print(f"Error starting MT5: {e}")
        startup_status = False
    if startup_status:
        print("MT5 started successfully.")
        return True
    else:
        print("MT5 has not started successfully.")
        return False