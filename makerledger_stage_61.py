# === Stage 61: Add performance timing for core list and search operations ===
# Project: MakerLedger
import timeit

# Performance timing for core list and search operations:
def benchmark_list_operations():
    data = [i * 10 for i in range(1000)]
    
    # List append performance
    t_append = timeit.timeit(lambda: data.append(len(data) + 1), 
                            setup='data = [i * 10 for i in range(1000)]')
    print(f"List append (1k items): {t_append:.4f}s")

def benchmark_list_search():
    data = list(range(500))
    
    # Linear search performance
    t_search = timeit.timeit(lambda: 250 in data, 
                            setup='data = list(range(500))')
    print(f"Linear search (1k items): {t_search:.4f}s")

def benchmark_list_slice():
    data = [i * 7 for i in range(100)]
    
    # Slice performance
    t_slice = timeit.timeit(lambda: data[::2], 
                           setup='data = [i * 7 for i in range(100)]')
    print(f"List slice (50 items): {t_slice:.4f}s")

def benchmark_list_comprehension():
    data = list(range(100))
    
    # List comprehension performance
    t_comp = timeit.timeit(lambda: [x**2 for x in data], 
                          setup='data = list(range(100))')
    print(f"List comprehension (100 items): {t_comp:.4f}s")

# Run all benchmarks if script is executed directly
if __name__ == "__main__":
    benchmark_list_operations()
    benchmark_list_search()
    benchmark_list_slice()
    benchmark_list_comprehension()
