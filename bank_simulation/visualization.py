import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Create a directory for plots if it doesn't exist
PLOTS_DIR = 'plots'
os.makedirs(PLOTS_DIR, exist_ok=True)

def save_plot(figure, filename):
    """Helper function to save plots"""
    plot_path = os.path.join(PLOTS_DIR, filename)
    figure.savefig(plot_path)
    plt.close(figure)
    print(f"Saved plot to {plot_path}")

def plot_waiting_times(df: pd.DataFrame):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='customer_id', y='waiting_time')
    plt.title('Waiting Time for Each Customer')
    plt.xlabel('Customer ID')
    plt.ylabel('Waiting Time (minutes)')
    plt.grid(True)
    save_plot(plt.gcf(), 'waiting_times.png')

def plot_system_times(df: pd.DataFrame):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='customer_id', y='system_time')
    plt.title('Total Time in System for Each Customer')
    plt.xlabel('Customer ID')
    plt.ylabel('System Time (minutes)')
    plt.grid(True)
    save_plot(plt.gcf(), 'system_times.png')

# def plot_service_vs_waiting(df: pd.DataFrame):
#     plt.figure(figsize=(10, 6))
#     sns.scatterplot(data=df, x='service_time', y='waiting_time')
#     plt.title('Service Time vs Waiting Time')
#     plt.xlabel('Service Time (minutes)')
#     plt.ylabel('Waiting Time (minutes)')
#     plt.grid(True)
#     save_plot(plt.gcf(), 'service_vs_waiting.png')

def plot_histogram_waiting_times(df: pd.DataFrame):
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='waiting_time', bins=30, kde=True)
    plt.title('Distribution of Waiting Times')
    plt.xlabel('Waiting Time (minutes)')
    plt.ylabel('Frequency')
    plt.grid(True)
    save_plot(plt.gcf(), 'waiting_times_histogram.png')

def plot_queue_length_over_time(df: pd.DataFrame):
    # Create time points for plotting
    time_points = sorted(df['arrival_time'].tolist() + df['departure_time'].tolist())
    queue_lengths = []
    current_queue = 0
    
    for time in time_points:
        arrivals = sum(df['arrival_time'] == time)
        departures = sum(df['departure_time'] == time)
        current_queue += arrivals - departures
        queue_lengths.append(current_queue)
    
    plt.figure(figsize=(12, 6))
    plt.step(time_points, queue_lengths, where='post')
    plt.title('Queue Length Over Time')
    plt.xlabel('Time (minutes)')
    plt.ylabel('Queue Length')
    plt.grid(True)
    save_plot(plt.gcf(), 'queue_length_over_time.png')