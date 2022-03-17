
def moving_average(data, win):
    """
    Computes the moving average of the data
    for a given window size.

    Args:
        data (list): a list of floats
        win (int): window size to average over
    """

    result = []
    for i in range(win, len(data) + 1):
        val = sum(data[i - win:i]) / win
        result.append(round(val, 2))

    # duplicate the first value so the lists are the same length
    return [result[0]] * (win - 1) + result


class MockMarket:
    """
    Class to provide a mock stock market for Tutorial 09
    """

    def __init__(self):
        """
        Initialize the default stock prices and the mock today value
        """

        self.init_gme()
        self.today = 0
    
    def has_data(self, win):
        """
        Boolean function to check if there is enough data for the given window.

        Args:
            win (int): Window size
        
        Returns:
            bool: True if the market has enough data, otherwise False
        """
        return self.today >= win and self.today < len(self.gme) - win

    def advance_day(self):
        """
        Increments the day counter
        """

        self.today += 1

    def get_today_price(self):
        """
        Returns the "current" price of GME
        """

        if not self.has_data(0):
            return None

        return self.gme[self.today]

    def get_prev_close(self, num):
        """
        Get the previous closing value for the last num days.

        Args:
            num (int): the number of days to get before today

        Returns:
            float: the closing price of GME for the given day
        """

        if not self.has_data(num):
            return None

        return self.gme[self.today - num : self.today + 1]

    def load_data(self, show=False):
        """Function used to fetch the GME data from Yahoo finance
        Loads the last 2 years of GME data and saves the closing price
        in a list. Optionally, prints the prices to copy into hard-coded list.

        Requires yfinance module installed via terminal command:
        pip install yfinance
        """

        import yfinance as yf

        ticker = yf.Ticker("GME")
        hist = ticker.history(period="2y")
        self.gme = list(hist["Close"])

        # optionally, print out the data to copy into hard-coded list
        if show:
            print("self.gme = [")
            for val in self.gme:
                print(f"    {val:.2f},")
            print("]")

    def plot_data(self):
        """
        Function to plot data and zoom in on an interesting region.
        Requres matplotlib module installed via terminal command:
        pip install matplotlib
        """
        import matplotlib.pyplot as plt

        plt.plot(self.gme)
        plt.plot(moving_average(self.gme, 5), linestyle="--")
        plt.plot(moving_average(self.gme, 10), linestyle="-.")
        plt.xlim([200, 260])
        plt.xlabel("Day")
        plt.ylabel("Price ($)")

        plt.legend(
            ["Closing stock price", "5-day moving average", "10-day moving average"]
        )

        plt.show()

    def init_gme(self):
        # GME closing share price from March 16, 2020 to March 16, 20222
        self.gme = [
            4.37,
            4.23,
            3.77,
            4.19,
            3.76,
            3.81,
            4.16,
            4.17,
            4.41,
            4.22,
            3.65,
            3.50,
            3.25,
            2.85,
            2.80,
            3.09,
            3.27,
            3.41,
            3.89,
            4.74,
            5.95,
            5.27,
            5.03,
            4.88,
            5.61,
            4.78,
            4.89,
            4.70,
            4.77,
            5.82,
            5.64,
            6.04,
            5.73,
            6.05,
            5.48,
            5.39,
            4.93,
            4.87,
            4.98,
            4.76,
            4.54,
            4.21,
            4.13,
            4.22,
            4.58,
            4.44,
            4.43,
            4.44,
            4.18,
            4.42,
            4.69,
            4.33,
            4.06,
            4.13,
            4.18,
            4.44,
            4.47,
            4.14,
            5.01,
            4.96,
            5.07,
            4.37,
            4.72,
            4.69,
            4.64,
            4.76,
            4.95,
            4.88,
            4.87,
            4.83,
            4.41,
            4.46,
            4.35,
            4.38,
            4.34,
            4.44,
            4.29,
            4.24,
            4.09,
            4.26,
            4.21,
            4.34,
            4.26,
            4.08,
            4.19,
            4.17,
            3.96,
            3.85,
            4.01,
            4.11,
            4.11,
            4.03,
            4.01,
            3.94,
            4.06,
            4.10,
            4.01,
            4.15,
            4.43,
            4.63,
            4.43,
            4.16,
            4.33,
            4.35,
            4.52,
            4.64,
            4.75,
            4.63,
            4.81,
            4.72,
            4.61,
            5.03,
            4.87,
            4.98,
            5.11,
            5.25,
            5.39,
            6.68,
            7.65,
            7.71,
            7.82,
            7.65,
            7.70,
            7.35,
            6.23,
            6.09,
            6.91,
            7.09,
            8.68,
            9.20,
            9.47,
            8.75,
            10.56,
            10.04,
            9.14,
            10.02,
            10.09,
            10.35,
            10.20,
            9.77,
            9.39,
            9.46,
            9.13,
            9.36,
            13.49,
            12.02,
            11.80,
            11.88,
            12.25,
            13.83,
            13.31,
            13.91,
            13.86,
            14.10,
            14.91,
            15.00,
            13.45,
            12.69,
            11.82,
            11.73,
            10.47,
            10.75,
            11.57,
            10.91,
            11.45,
            11.86,
            11.49,
            11.10,
            11.75,
            11.13,
            11.01,
            12.06,
            11.63,
            11.57,
            12.46,
            12.71,
            13.90,
            13.67,
            14.75,
            16.08,
            16.56,
            15.80,
            16.58,
            16.12,
            16.90,
            16.35,
            16.94,
            13.66,
            14.12,
            13.31,
            12.72,
            13.85,
            13.85,
            14.83,
            15.63,
            15.53,
            19.46,
            20.57,
            20.15,
            20.99,
            19.38,
            19.26,
            18.84,
            17.25,
            17.37,
            18.36,
            18.08,
            17.69,
            19.94,
            19.95,
            31.40,
            39.91,
            35.50,
            39.36,
            39.12,
            43.03,
            65.01,
            76.79,
            147.98,
            347.51,
            193.60,
            325.00,
            225.00,
            90.00,
            92.41,
            53.50,
            63.77,
            60.00,
            50.31,
            51.20,
            51.10,
            52.40,
            49.51,
            45.94,
            40.69,
            40.59,
            46.00,
            44.97,
            91.71,
            108.73,
            101.74,
            120.40,
            118.18,
            124.18,
            132.35,
            137.74,
            194.50,
            246.90,
            265.00,
            260.00,
            264.50,
            220.14,
            208.17,
            209.81,
            201.75,
            200.27,
            194.49,
            181.75,
            120.34,
            183.75,
            181.00,
            181.30,
            194.46,
            189.82,
            191.45,
            186.95,
            184.50,
            177.97,
            170.26,
            158.36,
            141.09,
            140.99,
            166.53,
            156.44,
            154.69,
            164.37,
            158.53,
            158.51,
            151.17,
            151.18,
            168.93,
            177.77,
            178.58,
            176.19,
            173.59,
            162.20,
            160.73,
            159.48,
            161.01,
            161.11,
            143.22,
            146.92,
            144.79,
            164.50,
            159.92,
            180.60,
            180.67,
            168.83,
            170.49,
            176.79,
            180.01,
            209.43,
            242.56,
            254.13,
            222.00,
            249.02,
            282.24,
            258.18,
            248.36,
            280.01,
            300.00,
            302.56,
            220.39,
            233.34,
            229.44,
            222.50,
            222.97,
            223.59,
            213.82,
            200.37,
            220.40,
            219.34,
            212.31,
            209.51,
            213.25,
            210.88,
            214.14,
            204.36,
            202.83,
            199.56,
            190.66,
            191.38,
            191.23,
            189.25,
            180.06,
            167.62,
            166.82,
            169.04,
            173.49,
            191.18,
            185.81,
            178.85,
            180.36,
            183.94,
            178.54,
            169.12,
            164.86,
            161.12,
            157.65,
            152.75,
            146.80,
            153.44,
            151.77,
            161.13,
            159.05,
            158.78,
            162.35,
            162.52,
            163.93,
            163.55,
            157.05,
            152.90,
            159.30,
            164.89,
            210.29,
            199.65,
            205.22,
            204.95,
            209.20,
            218.24,
            212.97,
            213.52,
            202.75,
            199.00,
            198.80,
            199.18,
            190.41,
            203.40,
            199.24,
            204.52,
            206.37,
            204.97,
            192.20,
            189.95,
            190.14,
            191.24,
            185.16,
            189.48,
            178.60,
            175.92,
            175.47,
            176.91,
            171.36,
            172.18,
            171.07,
            172.12,
            172.68,
            178.10,
            175.82,
            184.06,
            183.83,
            183.28,
            186.02,
            186.79,
            184.52,
            181.71,
            169.80,
            173.97,
            177.84,
            173.51,
            182.85,
            183.51,
            200.09,
            206.99,
            218.33,
            217.84,
            213.25,
            218.64,
            206.60,
            199.19,
            204.32,
            202.10,
            209.14,
            207.18,
            210.00,
            210.12,
            228.80,
            247.55,
            213.90,
            211.78,
            199.72,
            202.01,
            196.21,
            179.84,
            181.56,
            172.39,
            167.12,
            177.81,
            173.65,
            155.76,
            159.01,
            136.88,
            147.69,
            148.59,
            144.59,
            155.64,
            157.14,
            158.12,
            154.00,
            152.14,
            148.31,
            146.46,
            153.93,
            155.33,
            148.39,
            152.84,
            148.91,
            129.37,
            131.03,
            140.62,
            131.15,
            130.30,
            128.06,
            122.48,
            116.65,
            108.91,
            106.57,
            102.67,
            106.36,
            100.15,
            99.79,
            103.26,
            93.52,
            97.91,
            108.93,
            112.60,
            100.04,
            99.23,
            102.34,
            102.34,
            115.60,
            124.29,
            122.47,
            124.25,
            117.09,
            126.16,
            128.33,
            123.41,
            121.53,
            118.06,
            114.87,
            124.58,
            118.58,
            123.34,
            119.02,
            121.97,
            118.41,
            111.66,
            99.35,
            103.01,
            105.21,
            100.56,
            92.69,
            78.11,
            82.64,
            88.55,
        ]


def test_moving_average():
    market = MockMarket()

    # grab just the first 10 values of the data to test
    data = market.gme[:10]
    print(data)
    win = 3
    print(moving_average(data, win))

def main():
    market = MockMarket()
    market.plot_data()


if __name__ == "__main__":
    test_moving_average()
