from bank_simulation.simulation import BankSimulation
from bank_simulation.metrics import create_results_dataframe, save_results_to_csv
from bank_simulation.visualization import (
    plot_waiting_times, 
    plot_system_times,
    plot_metrics_summary,
    # plot_service_vs_waiting,
    plot_histogram_waiting_times,
    plot_queue_length_over_time
)

def main():
    # Initialize and run simulation
    print("Starting bank simulation with 500 customers...")
    simulation = BankSimulation(500)
    simulation.run_simulation()
    
    # Calculate and display metrics
    metrics = simulation.calculate_metrics()
    print("\nSimulation Metrics:")
    for key, value in metrics.items():
        print(f"{key.replace('_', ' ').title()}: {value:.2f}")
    
    # Create and save results dataframe
    customers = simulation.get_customers()
    df = create_results_dataframe(customers)
    save_results_to_csv(df, 'data/simulation_results.csv')
    print("\nSimulation results saved to 'data/simulation_results.csv'")
    
    # Generate visualizations
    print("\nGenerating visualizations...")
    plot_waiting_times(df)
    plot_system_times(df)
    # plot_service_vs_waiting(df)
    plot_metrics_summary(metrics)
    plot_histogram_waiting_times(df)
    plot_queue_length_over_time(df)

if __name__ == "__main__":
    main()