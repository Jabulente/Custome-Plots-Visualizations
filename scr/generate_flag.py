
import numpy as np
import matplotlib.pyplot as plt

def get_flag_dimensions():
    return 3, 2  # width, height (2:3 ratio)

def calculate_diagonal_params(width, height):
    k = np.sqrt(13)
    slope = height / width
    outer_offset = k / 6
    inner_offset = k / 12
    return slope, outer_offset, inner_offset

def generate_lines(x, slope, outer_offset, inner_offset):
    main = slope * x
    upper_outer = main + outer_offset
    upper_inner = main + inner_offset
    lower_inner = main - inner_offset
    lower_outer = main - outer_offset
    return upper_outer, upper_inner, lower_inner, lower_outer

def plot_flag(x, upper_outer, upper_inner, lower_inner, lower_outer, width, height):
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_aspect('equal')

    # Fill flag regions
    ax.fill_between(x, upper_outer, height, color='#1EB53A', interpolate=True)    # Green
    ax.fill_between(x, upper_outer, upper_inner, color='#FCD116', interpolate=True)  # Top Yellow
    ax.fill_between(x, upper_inner, lower_inner, color='black', interpolate=True)    # Black
    ax.fill_between(x, lower_inner, lower_outer, color='#FCD116', interpolate=True)  # Bottom Yellow
    ax.fill_between(x, lower_outer, 0, color='#00A3DD', interpolate=True)           # Blue

    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.axis('off')
    plt.tight_layout()
   #plt.savefig('tanzania_flag.png', dpi=300, bbox_inches='tight')
    plt.show()

def draw_tanzania_flag():
    width, height = get_flag_dimensions()
    slope, outer_offset, inner_offset = calculate_diagonal_params(width, height)
    x = np.linspace(0, width, 1000)
    upper_outer, upper_inner, lower_inner, lower_outer = generate_lines(x, slope, outer_offset, inner_offset)
    plot_flag(x, upper_outer, upper_inner, lower_inner, lower_outer, width, height)

# Call the main function
draw_tanzania_flag()
