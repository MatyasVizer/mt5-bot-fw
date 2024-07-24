import utils
import strategies as strat

if __name__ == '__main__':
    cfg = utils.get_cfg()
    startup = utils.start_client(cfg)
    candles = utils.load_candles(cfg)
    df_ind = strat.spawn_indicators(candles, cfg)