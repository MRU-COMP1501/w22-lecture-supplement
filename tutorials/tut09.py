from mockmarket import MockMarket

def mean(data):
    """
    Return the mean value of the list data.
    """
    return sum(data) / len(data)

def crossover(prev_trend, trend):
    """
    Checks for crossover. Returns +1 if the trend is changing to positive,
    returns -1 if the trend is changing to negative, otherwise returns 0.
    """
    if prev_trend == trend:
        return 0
    
    if prev_trend: # positive switching to negative
        return -1
    else:
        return +1

def buy_sell_shares(short_win, long_win):
    """
    Buy and sell shares of GME according to crossover rules:
    - If short-term mean > long-term mean, trend is positive.
    - If trend is currently positive, sell if trend changes.
    - If trend is currently negative, buy if trend changes.

    Args:
        short_win (int): Number of days to calculate short-term mean
        long_win (int): Number of days to calculate long-term mean
    
    Returns: 
        total_per_share (float): Amount of money made (or lost) per share
            by using this strategy over the entire time period
    """
    
    market = MockMarket()

    # initialize the market "today" value to the longest time frame so we
    # can calculate back long_win days
    market.today = long_win

    # initialize the prev_trend and accumulator
    prev_trend = False
    total_per_share = 0

    # initialize a flag so we don't sell before buying
    bought = False

    # Loop as long as the market has data
    while market.has_data(long_win):
        # get the two windows of data
        prev_long = market.get_prev_close(long_win)
        prev_short = market.get_prev_close(short_win)

        # update the trend value
        trend = mean(prev_short) > mean(prev_long)
        
        # check if there's a crossover
        if crossover(prev_trend, trend) > 0:
            # signal to buy
            total_per_share -= market.get_today_price()
            print(f'Buying on day {market.today} at ${market.get_today_price()}')
            bought = True
        elif crossover(prev_trend, trend) < 0 and bought:
            # signal to sell
            total_per_share += market.get_today_price()
            print(f'Selling on day {market.today} at ${market.get_today_price()}')
        
        # update previous trend with current trend
        prev_trend = trend
        
        # update the loop variable by advancing the day in the market
        market.advance_day()
    
    return total_per_share

def main():
    """
    Prompt the user for a short window and a long window.
    Then, calculate how much money per share they would have made
    over the past two years buying/selling GME.
    """
    short_win = int(input('Enter a short window: '))
    long_win = int(input('Enter a long window: '))
    total = buy_sell_shares(short_win, long_win)
    print(f'You made a total of ${total:.2f}')

if __name__ == '__main__':
    main()