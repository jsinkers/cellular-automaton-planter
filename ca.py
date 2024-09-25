import numpy as np
import matplotlib.pyplot as plt

def binary_rule(rule_num):
    """
    Converts a rule number (0-255) into its binary representation.
    """
    return np.array([int(bit) for bit in f'{rule_num:08b}'], dtype=int)

def apply_rule(triplet, rule_bin):
    """
    Applies the rule based on a triplet of neighbors (left, center, right).
    """
    index = 7 - (triplet[0] * 4 + triplet[1] * 2 + triplet[2] * 1)
    return rule_bin[index]

def generate_ca(width, height, rule_num):
    """
    Generates a 2D grid of the cellular automaton based on a given rule number.
    """
    grid = np.zeros((height, width), dtype=int)
    # Initial condition: alternating 0s and 1s
    #grid[0, :] = np.arange(width) % 2
    #grid[0, width // 2] = 1  # Start with a single active cell in the center
    # random initial condition
    grid[0, :] = np.random.randint(0, 2, width)

    rule_bin = binary_rule(rule_num)

    for t in range(1, height):
        for i in range(width):
            left = grid[t - 1, (i - 1) % width]
            center = grid[t - 1, i]
            right = grid[t - 1, (i + 1) % width]
            grid[t, i] = apply_rule([left, center, right], rule_bin)

    return grid

def export_to_openscad(ca_output, filename="ca_planter.scad"):
    """
    Exports the CA output into an OpenSCAD script file that includes the CA data.
    """
    with open(filename, 'w') as f:
        # Write the CA data into the file
        f.write("ca_grid = [\n")
        for row in ca_output:
            f.write("  [" + ",".join(map(str, row)) + "],\n")
        f.write("];\n\n")

        # Write the OpenSCAD code that reads from the CA data
        f.write("""
module cylindrical_planter() {
    height = len(ca_grid);  // The height of the cylinder based on the CA grid
    radius = 40;            // Adjust as needed for your design
    thickness = 2;          // Wall thickness
    num_slices = len(ca_grid[0]);  // Number of slices (circumferential segments)

    for (h = [0 : height-1]) {
        for (s = [0 : num_slices-1]) {
            angle = s * 360 / num_slices;
            z_pos = h;
            if (ca_grid[h][s] == 1) {
                // Extrude outward for each active cell
                translate([radius * cos(angle), radius * sin(angle), z_pos])
                    cylinder(r=thickness, h=1, center=false);
            }
        }
    }
}

cylindrical_planter();
        """)

# Example settings
width = 40  # Number of cells around the cylinder's circumference
height = 60  # Number of time steps (vertical height of the planter)
rule_num = 110  # Rule number (Rule 110)

# Example settings
width = 400  # Number of cells around the cylinder's circumference
height = 60  # Number of time steps (vertical height of the planter)
rule_num = 30  # The rule number to apply (e.g., Rule 110)

ca_output = generate_ca(width, height, rule_num)

# Visualize the pattern
plt.imshow(ca_output, cmap="binary")
plt.title(f'Cellular Automaton - Rule {rule_num}')
plt.show()

export_to_openscad(ca_output, f"ca_output_w{width}xh{height}_rule_{rule_num}.scad")
