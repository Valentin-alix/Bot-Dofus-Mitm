import matplotlib
import pandas as pd

matplotlib.use("Qt5Agg")


from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class ChartContent(FigureCanvasQTAgg):
    def __init__(self, width=5, height=5, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(ChartContent, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)

    def show(self, df_info: pd.DataFrame):
        self.axes.cla()
        self.axes.set_xlabel("Date de création")
        self.axes.set_ylabel("Prix par 1, 10 et 100")

        self.axes.plot(df_info["creation_date"], df_info["hundred"], label="100")
        self.axes.plot(df_info["creation_date"], df_info["ten"], label="10")
        self.axes.plot(df_info["creation_date"], df_info["one"], label="1")

        self.axes.legend()
        self.draw()
