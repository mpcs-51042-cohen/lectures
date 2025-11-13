import time

def debugging(f): # decorator
  def wrapper(*args, **kwargs):
    start_time = time.time()
    if (...):
      pass
    else:
      f(*args, **kwargs)
    ending_time = time.time()
    print(f"That took {(ending_time - start_time)} seconds.")
  return wrapper

@debugging
@logging
@timer
def perform_computation(complexity=1):
  print("Performing computation...")
  time.sleep(complexity)  

@timer
def sort_a_big_list(dataset):
  print("Sorting...")
  time.sleep(len(dataset))
  
def demo():
  time.sleep(1)
  

perform_computation(2)
sort_a_big_list([1,2,3])
  
  
