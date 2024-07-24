import MetaTrader5 as mt5
import pandas as pd


def start_mt5(cfg):
    login = cfg["mt5"]["username"]
    login = int(login)
    password = cfg["mt5"]["password"]
    server = cfg["mt5"]["server"]
    path = cfg["mt5"]["mt5_pathway"]

    mt5_init = False

    if not mt5.initialize(path=path, login=login, server=server, password=password):
        print("initialize() failed, error code =", mt5.last_error())
        quit()
    print(mt5.terminal_info())

    authorized = mt5.login(login=login, server=server, password=password)
    if authorized:
        return True
    else:
        print("failed to connect at account #{}, error code: {}".format(login, mt5.last_error()))
        return False


def init_symbols(symbol):
    symbols = mt5.symbols_get()
    all_symbols = []
    for s in symbols:
        all_symbols.append(s.name)
    selected = mt5.symbol_select(symbol, True)
    if not selected:
        print(f"Failed to select {symbol}, error code =", mt5.last_error())
    return True


def get_candles(symbol, timeframe, amount):
    if amount > 50000:
        raise ValueError("Modify settings, to retrieve more than 50k candles.")
    current_timeframe = set_query_timeframe(timeframe)
    candles = mt5.copy_rates_from_pos(symbol, current_timeframe, 1, amount)
    dataframe = pd.DataFrame(candles)
    return dataframe


def set_query_timeframe(timeframe):
    if timeframe == "M1":
        return mt5.TIMEFRAME_M1
    elif timeframe == "M2":
        return mt5.TIMEFRAME_M2
    elif timeframe == "M3":
        return mt5.TIMEFRAME_M3
    elif timeframe == "M4":
        return mt5.TIMEFRAME_M4
    elif timeframe == "M5":
        return mt5.TIMEFRAME_M5
    elif timeframe == "M6":
        return mt5.TIMEFRAME_M6
    elif timeframe == "M10":
        return mt5.TIMEFRAME_M10
    elif timeframe == "M12":
        return mt5.TIMEFRAME_M12
    elif timeframe == "M15":
        return mt5.TIMEFRAME_M15
    elif timeframe == "M20":
        return mt5.TIMEFRAME_M20
    elif timeframe == "M30":
        return mt5.TIMEFRAME_M30
    elif timeframe == "H1":
        return mt5.TIMEFRAME_H1
    elif timeframe == "H2":
        return mt5.TIMEFRAME_H2
    elif timeframe == "H3":
        return mt5.TIMEFRAME_H3
    elif timeframe == "H4":
        return mt5.TIMEFRAME_H4
    elif timeframe == "H6":
        return mt5.TIMEFRAME_H6
    elif timeframe == "H8":
        return mt5.TIMEFRAME_H8
    elif timeframe == "H12":
        return mt5.TIMEFRAME_H12
    elif timeframe == "D1":
        return mt5.TIMEFRAME_D1
    elif timeframe == "W1":
        return mt5.TIMEFRAME_W1
    elif timeframe == "MN1":
        return mt5.TIMEFRAME_MN1
    else:
        print(f"Incorrect timeframe provided. {timeframe}")
        raise ValueError