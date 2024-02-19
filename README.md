# RobinhoodTrader
Executing stock trades through the Robinhood API.

This automated trading system is specifically designed for long-term investments, employing a basic Automatic Investment Plan (AIP). The primary goal is not to achieve rapid short-term gains but rather to target sustained returns over a period of at least 5 to 10 years, with a focus on retirement planning.

The fundamental strategy draws inspiration from Warren Buffett's guiding principles, treating his quotes as invaluable trading rules:

Rule No.1: "Never bet against America."
Rule No.2. "Be fearful when others are greedy, and be greedy when others are fearful."

Keeping it simple, the core operation involves setting a fixed monthly investment amount and distributing it across selected ETFs on a weekly basis. This aligns with Rule No.1, expressing confidence in the long-term growth of the U.S. economy. The underlying belief is that, over the next decade or more, the U.S. economy will continue to prosper.

For instance, if the monthly investment is $1000, the weekly allocation would be $250. The chosen ETFs (SPY/VOO, QQQ, BRKB) are assigned specific amounts (e.g., $90 on SPY/VOO, $80 on QQQ, and $80 on BRKB). Adjustments are made based on the current price—buying fewer shares if the price is higher and more shares if it is lower. This approach naturally averages the risks associated with purchasing at varying price levels. The strategy emphasizes a "Buy and Hold" philosophy, avoiding selling unless absolutely necessary.

The subsequent optimization step adheres to Rule No.2. The objective is to fine-tune operations by increasing investments during times of market fear and predicting a potential market bottom during bearish trends. Conversely, reducing investments is considered during the peak of bullish trends.

Two key indices inform the optimization process:

1. Market greed/fear index.
2. The S&P 500 Moving Averages (MA50 and MA200), leveraging trend analysis to ascertain whether the market is currently in a bearish or bullish phase.
