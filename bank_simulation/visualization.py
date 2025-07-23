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

def plot_metrics_summary(metrics: dict):
    """
    Plots key simulation metrics as a bar chart.
    
    Args:
        metrics: Dictionary from BankSimulation.calculate_metrics()
    """
    # Extract metrics for visualization
    labels = [
        'Avg Waiting Time', 
        'Max Waiting Time',
        'Avg System Time',
        'Server Utilization'
    ]
    values = [
        metrics['average_waiting_time'],
        metrics['max_waiting_time'],
        metrics['average_system_time'],
        metrics['server_utilization'] * 100  # Convert to percentage
    ]
    
    # Create figure
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, values, color=['#4C72B0', '#DD8452', '#55A868', '#C44E52'])
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}' if 'Time' in bar.get_label() else f'{height:.1f}%',
                ha='center', va='bottom')
    
    plt.title('Key Simulation Metrics Summary')
    plt.ylabel('Time (minutes) / Percentage')
    plt.ylim(0, max(values) * 1.2)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Save the plot
    save_plot(plt.gcf(), 'metrics_summary.png')