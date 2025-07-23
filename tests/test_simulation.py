import unittest
import numpy as np
from bank_simulation.simulation import BankSimulation, Customer

class TestBankSimulation(unittest.TestCase):
    def setUp(self):
        self.simulation = BankSimulation(10)  # Use smaller number for tests
    
    def test_generate_interarrival_time(self):
        times = [self.simulation.generate_interarrival_time() for _ in range(1000)]
        self.assertTrue(all(1 <= t <= 8 for t in times))
        self.assertAlmostEqual(np.mean(times), 4.5, delta=0.5)
    
    def test_generate_service_time(self):
        times = [self.simulation.generate_service_time() for _ in range(1000)]
        self.assertTrue(all(1 <= t <= 6 for t in times))
        self.assertAlmostEqual(np.mean(times), 3.5, delta=0.5)
    
    def test_customer_generation(self):
        self.assertEqual(len(self.simulation.customers), 10)
        for i, customer in enumerate(self.simulation.customers):
            self.assertEqual(customer.customer_id, i+1)
            if i > 0:
                self.assertGreaterEqual(customer.arrival_time, 
                                      self.simulation.customers[i-1].arrival_time)
    
    def test_simulation_run(self):
        self.simulation.run_simulation()
        customers = self.simulation.get_customers()
        
        # Check all customers have departure times
        self.assertTrue(all(c.departure_time > 0 for c in customers))
        
        # Check service starts after arrival
        for c in customers:
            self.assertGreaterEqual(c.service_start_time, c.arrival_time)
            self.assertGreaterEqual(c.departure_time, c.service_start_time + c.service_time)
        
        # Check FIFO order is maintained
        for i in range(1, len(customers)):
            if customers[i].service_start_time < customers[i-1].departure_time:
                self.assertGreaterEqual(customers[i].arrival_time, 
                                       customers[i-1].arrival_time)

if __name__ == '__main__':
    unittest.main()