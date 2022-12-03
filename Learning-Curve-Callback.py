import pandas as pd
import matplotlib.pyplot as plt
import os

class LearningCurve(keras.callbacks.Callback):
  def __init__(self, metrics_to_plot, directory):
    self.metrics_to_plot = metrics_to_plot
    self.directory = directory
    if not os.path.exists(directory):
      os.mkdir(directory)


  def on_train_begin(self, logs):
    self.metric_logs = []
  
  def on_epoch_end(self, epoch, logs):
    self.metric_logs.append(logs)

  def on_train_end(self, logs):
    metrics_df = pd.DataFrame(self.metric_logs)
    for metric in self.metrics_to_plot:
      fig, ax = plt.subplots(figsize=(20, 6))
      fig.suptitle(metric.title(), fontsize=18)
      metrics_df[[metric, f'val_{metric}']].plot(style='o-', ax=ax)
      plt.savefig(os.path.join(self.directory, metric))
      plt.show()

    self.metric_logs = []

class BatchWiseLearningCurve(keras.callbacks.Callback):
  def __init__(self, metrics_to_plot, directory):
    self.metrics_to_plot = metrics_to_plot
    self.directory = directory
    if not os.path.exists(directory):
      os.mkdir(directory)

  def on_train_begin(self, logs):
    self.metric_logs = []
  
  def on_batch_end(self, batch, logs):
    self.metric_logs.append(logs)

  def on_epoch_end(self, epoch, logs):
    metrics_df = pd.DataFrame(self.metric_logs)
    for metric in self.metrics_to_plot:
      fig, ax = plt.subplots(figsize=(20, 6))
      fig.suptitle(f"BatchWise {metric.title()} for epoch {epoch+1}", fontsize=18)
      metrics_df[metric].plot(ax=ax)
      plt.savefig(os.path.join(self.directory, f"batchwise_{metric}_epoch_{epoch+1}"))
      plt.show()
    self.metric_logs = []