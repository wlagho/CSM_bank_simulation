import numpy as np
from typing import List, Dict, Tuple

class Customer:
    def __init__(self, customer_id: int, arrival_time: float):
        self.customer_id = customer_id
        self.arrival_time = arrival_time
        self.service_start_time = 0.0
        self.service_time = 0.0
        self.departure_time = 0.0
    
    def __str__(self):
        return (f"Customer {self.customer_id}: Arrival={self.arrival_time:.2f}, "
                f"Service Start={self.service_start_time:.2f}, "
                f"Service Time={self.service_time:.2f}, "
                f"Departure={self.departure_time:.2f}")

class BankSimulation:
    def __init__(self, num_customers: int = 500):
        self.num_customers = num_customers
        self.customers: List[Customer] = []
        self.current_time = 0.0
        self.server_busy = False
        self.queue = []
        self.generate_customers()
    
    def generate_interarrival_time(self) -> float:
        return np.random.uniform(1, 8)
    
    def generate_service_time(self) -> float:
        return np.random.uniform(1, 6)
    
    def generate_customers(self):
        arrival_time = 0.0
        for i in range(self.num_customers):
            if i > 0:
                arrival_time += self.generate_interarrival_time()
            customer = Customer(i+1, arrival_time)
            customer.service_time = self.generate_service_time()
            self.customers.append(customer)
    
    def run_simulation(self):
        event_list = []
        
        # Initialize event list with all arrivals
        for customer in self.customers:
            event_list.append(('arrival', customer.arrival_time, customer))
        
        # Process events in chronological order
        while event_list:
            event_list.sort(key=lambda x: x[1])  # Sort by time
            event = event_list.pop(0)
            event_type, event_time, customer = event
            
            self.current_time = event_time
            
            if event_type == 'arrival':
                self.handle_arrival(customer, event_list)
            elif event_type == 'departure':
                self.handle_departure(customer, event_list)
    
    def handle_arrival(self, customer: Customer, event_list: List[Tuple]):
        if not self.server_busy:
            # Server is idle, start service immediately
            self.server_busy = True
            customer.service_start_time = self.current_time
            departure_time = self.current_time + customer.service_time
            event_list.append(('departure', departure_time, customer))
        else:
            # Server is busy, add to queue
            self.queue.append(customer)
    
    def handle_departure(self, customer: Customer, event_list: List[Tuple]):
        customer.departure_time = self.current_time
        
        if self.queue:
            # Serve next customer in queue
            next_customer = self.queue.pop(0)
            next_customer.service_start_time = self.current_time
            departure_time = self.current_time + next_customer.service_time
            event_list.append(('departure', departure_time, next_customer))
        else:
            # No customers in queue, server becomes idle
            self.server_busy = False
    
    def get_customers(self) -> List[Customer]:
        return self.customers
    
    def calculate_metrics(self) -> Dict[str, float]:
        waiting_times = [c.service_start_time - c.arrival_time for c in self.customers]
        system_times = [c.departure_time - c.arrival_time for c in self.customers]
        queue_lengths = []
        
        # Calculate queue length over time (simplified approach)
        time_points = sorted([c.arrival_time for c in self.customers] + 
                            [c.departure_time for c in self.customers])
        current_queue = 0
        max_queue = 0
        
        for time in time_points:
            arrivals = sum(1 for c in self.customers if c.arrival_time == time)
            departures = sum(1 for c in self.customers if c.departure_time == time)
            current_queue += arrivals - departures
            if current_queue > max_queue:
                max_queue = current_queue
        
        return {
            'average_waiting_time': np.mean(waiting_times),
            'max_waiting_time': np.max(waiting_times),
            'average_system_time': np.mean(system_times),
            'max_system_time': np.max(system_times),
            'server_utilization': sum(c.service_time for c in self.customers) / self.current_time,
            'average_queue_length': max_queue / len(time_points),
            'max_queue_length': max_queue
        }