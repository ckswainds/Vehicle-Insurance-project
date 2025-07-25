from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class MultivariateStrategy(ABC):
    @abstractmethod
    def plot(self, df: pd.DataFrame):
        pass


class CorrelationMatrixStrategy(MultivariateStrategy):
    def plot(self, df):
        corr_mtx = df.corr()
        sns.heatmap(corr_mtx, annot=True, cbar=True)
        plt.show()


class MultivariateAnalyzer:
    def __init__(self, strategy: MultivariateStrategy):
        self.strategy = strategy

    def analyze(self, df):
        self.strategy.plot(df)
