from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import seaborn as sns


class BivariateStrategy(ABC):
    @abstractmethod
    def plot(self, df, x, y):
        pass


class ScatterStrategy(BivariateStrategy):
    def plot(self, df, x, y):
        sns.scatterplot(data=df, x=x, y=y)
        plt.title(f"{x} vs {y}")
        plt.show()


class BoxplotStrategy(BivariateStrategy):
    def plot(self, df, x, y):
        sns.boxplot(data=df, x=x, y=y)
        plt.title(f"{x} vs {y}")
        plt.show()


class BivariateAnalyzer:
    def __init__(self, strategy: BivariateStrategy):
        self.strategy = strategy

    def analyze(self, df, x, y):
        self.strategy.plot(df, x, y)
