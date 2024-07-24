import numpy as np
import utils


def create(df, names):
    cfg = utils.get_cfg()
    for ind in names:
        globals()[ind](df, cfg)


def ma(dataframe, cfg):
    cfg = utils.get_cfg()
    ema_size = cfg["indicator_parameters"]["ma"]["size"]
    ema_name = "ma_" + str(ema_size)


def ema(dataframe, cfg):
    cfg = utils.get_cfg()
    ema_size = cfg["indicator_parameters"]["ema"]["size"]
    ema_name = "ema_" + str(ema_size)


def slow_stochastic(dataframe, cfg):
    length = cfg["indicator_parameters"]["slow_stochastic"]["length"]
    smooth_k = cfg["indicator_parameters"]["slow_stochastic"]["%K"]
    smooth_d = cfg["indicator_parameters"]["slow_stochastic"]["%D"]


