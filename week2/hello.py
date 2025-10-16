# type casting
# namespaces
import sys
COLORS = ("green", "blue")

def spin_roulette_wheel():
    picked_color = COLORS[0]
    number = 14
    print("Color is", picked_color, "and the number is", number)
    
def main(*args):
    spin_roulette_wheel()
    
if __name__ == "__main__":
    main(sys.argv)
    