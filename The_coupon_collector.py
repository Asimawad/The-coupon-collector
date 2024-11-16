import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import concurrent.futures
from tqdm import tqdm

def Empirical_solution(n, no_of_trials):
    coupons = set(range(1, n + 1))
    def single_trial(_):  # Added a dummy argument
        experiment = np.random.randint(1, n + 1, size=n * 10)
        collected = set()
        for idx, value in enumerate(experiment):
            collected.add(value)
            if collected == coupons:
                return idx + 1
        return len(experiment)

    # Use parallel processing for multiple trials
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(single_trial, range(no_of_trials)))

    def calc_probs(no_of_samples,counter):
        keys = np.array(list(counter.keys()))
        values = np.array(list(counter.values()))
        summ = np.sum((keys * values)/no_of_samples)
        return summ
    counter = Counter(results)
    boxes_needed = calc_probs(1000,counter)

    return boxes_needed


def expected_boxes_formula(n):
    # Harmonic number calculation: Sum of 1/k for k = 1 to n
    return n * sum(1 / k for k in range(1, n + 1))

def run_comparison(investigation):
    Empirical_results = [] ;    formula_results = []
    for inv in tqdm(investigation):
        boxes_needed = Empirical_solution(inv, 1000)
        Empirical_results.append(round(boxes_needed,2))
        formula_results.append(round(expected_boxes_formula(inv),2))
    return Empirical_results,formula_results

def plot(investigation , Empirical_results,formula_results):
    plt.plot(investigation , Empirical_results, label='Empirical Results Curve', color='blue')
    plt.plot(investigation, formula_results, label='Formula Curve', color='red')
    plt.xlabel('Number of Unique Coupons (n)');    plt.ylabel('Average Boxes Required')
    plt.legend()
    plt.savefig('compare.pdf')
    plt.show()


def curve_fitting(investigation,results):
    n_values = np.array(investigation)  
    box_counts = np.array(results)  

    coeffs = np.polyfit(n_values, box_counts, 2)
    poly_func = np.poly1d(coeffs)

    # Plotting the fitted curve
    plt.scatter(n_values, box_counts, label='Data Points')
    plt.plot(n_values, poly_func(n_values), label='Fitted Curve', color='red')
    plt.xlabel('Number of Unique Coupons (n)')
    plt.ylabel('Average Boxes Required')
    plt.legend()
    plt.savefig("curve.pdf")
    plt.show()

    # Display the function
    print(f"Fitted function: f(n) = {coeffs[0]:.4f}*n^2 + {coeffs[1]:.4f}*n + {coeffs[2]:.4f}")

if __name__ == "__main__":

    investigation = list(range(500)) 
    #  get the expected no. of boxes for several n trials
    Empirical_results,formula_results  =  run_comparison(investigation)
    #  plot the results
    plot(investigation , Empirical_results,formula_results)

    
    # Example usage: Single N example, assume n = 50
    n = 50                                              # No of distict copouns we have to collect
    Empirical_Result = Empirical_solution(n, 1000)
    print(f"Expected number of boxes to collect all {n} coupons 'Empirically': {Empirical_Result:.2f}")
    Formula_Result = expected_boxes_formula(n)
    print(f"Expected number of boxes to collect all {n} coupons 'Using Formula': {Formula_Result:.2f}")

    # Fit a Quadratic function to the data and try to compare, and get a function representing the data, hopefully ssomething similar to the formula' nln(n) + alpha '
    curve_fitting(investigation,Empirical_results)
