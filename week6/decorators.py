import time

def perform_computation(complexity=1):
  print("Performing computation...")
  time.sleep(complexity)  
  
def sort_a_big_list(dataset):
  print("Sorting...")
  time.sleep(len(dataset))
  

perform_computation(2)
sort_a_big_list([1,2,3])
  
  
