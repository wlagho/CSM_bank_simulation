# Bank Service Counter Simulation

A discrete-event simulation of a single-server bank queue system with FIFO (First-In-First-Out) service.

## Overview

This project simulates customer arrivals and service times at a bank counter with:

- Random inter-arrival times (1-8 minutes)
- Random service times (1-6 minutes)
- Performance metrics calculation (wait times, queue lengths, etc.)
- Visualization of key patterns

## Key Metrics Calculated

| Metric                  | Example Value from Simulation |
|-------------------------|-------------------------------|
| Average Waiting Time    | 1.89 minutes                 |
| Max Waiting Time        | 15.20 minutes                |
| Server Utilization      | 78%                          |
| Average Queue Length    | 0.01 customers               |

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/bank_simulation.git
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Simulation

To run the simulation, execute the main script:

 ```bash
    python main.py
```

This will:
    - Simulate 500 customers
    - Save results to `data/simulation_results.csv`
    - Generate visualizations in the `plots/` directory:
        - `waiting_times.png`
        - `queue_length_over_time.png`

## Project Structure

```bash
        bank_simulation/
        ├── data/                   # Simulation output data
        ├── plots/                  # Generated visualizations
        ├── bank_simulation/        # Core code
        │   ├── simulation.py       # Main simulation logic
        │   ├── metrics.py          # Performance calculations
        │   └── visualization.py    # Plot generation
        ├── tests/                  # Unit tests
        └── main.py                 # Entry point
```

## Understanding the Outputs

### Service Time vs Waiting Time

        ![Service vs Waiting Time](https://plots/service_vs_waiting.png)

        - **X-axis:** Service time (how long the transaction takes)
        - **Y-axis:** Waiting time (time spent in queue)
        - **Key Insight:** Waiting time depends on queue congestion, not just service time.

        ### Queue Length Over Time

        ![Queue Length Over Time](https://plots/queue_length_over_time.png)

        - Shows how customer backlog varies during the simulation.

        ## 🧪 Testing

        Run unit tests with:

        ```bash
        python -m unittest tests/test_simulation.py
        ```

        ## ⚙️ Customization

        Modify parameters in `simulation.py`:

        ```python
        # Change simulation parameters
        simulation = BankSimulation(
            num_customers=1000,        # Simulate more/fewer customers
            interarrival_range=(1,10), # Wider arrival window
            service_range=(1,8)        # Longer possible service times
        )
        ```

        ## 🤝 Contributing

        Pull requests are welcome! For major changes, please open an issue first.

        ## 📄 License

        MIT