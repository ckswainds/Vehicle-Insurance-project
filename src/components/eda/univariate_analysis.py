from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import seaborn as sns


class UnivariateStrategy(ABC):

    @abstractmethod
    def plot(self, df, column):
        pass


class HistogramStrategy(UnivariateStrategy):
    def plot(self, df, column):
        sns.histplot(df[column])
        plt.title(f"Histogram of {column}")
        plt.show()


class CountplotStrategy(UnivariateStrategy):
    def plot(self, df, column):
        sns.countplot(df, column)
        plt.title(f"Countplot of {column}")
        plt.show()


class UnivariateAnalyzer:
    def __init__(self, strategy: UnivariateStrategy):
        self.strategy = strategy

    def analyze(self, df, column):
        self.strategy.plot(df, column)
