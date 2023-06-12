import sys
sys.path.append('../Icarus-BT')
import Icarus as bt
import strategy as st


# Create an instance of Riley
riley = bt.Riley()
riley.set_cash(10000)
riley.add_data_csv('HistoricalData/F.csv')
riley.set_ticker('F')
riley.set_strategy(st.BollingerBands())
riley.set_stake_quantity(50)
# riley.set_stake_percentage(100)
# riley.set_stake_dollars(1000)
riley.add_metric(bt.metrics.SharpeRatio, 'sharpe')
riley.add_metric(bt.metrics.SortinoRatio, 'sortino')
riley.run()
# riley.plot(True)
# riley.plot_bar()