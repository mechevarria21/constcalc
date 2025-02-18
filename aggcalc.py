def calculate_tons(length, width, depth, material, compaction_state):
    """
    Calculate the weight of processed aggregate in tons.

    :param length: float, length in feet
    :param width: float, width in feet
    :param depth: float, depth in inches
    :param material: str, material type
    :param compaction_state: str, compaction state ('loose', 'compacted_95')
    :return: float, weight in tons
    """
    # Convert cubic feet to cubic yards (1 cubic yard = 27 cubic feet)
    volume_cubic_yards = (length * width * (depth / 12)) / 27
    
    # Get material density
    material_density = material_densities.get(material, {}).get(compaction_state)
    
    if material_density is None:
        print(f"Compaction state '{compaction_state}' is not available for {material}.")
        return None

    # Convert volume to tons
    return volume_cubic_yards * material_density

# Material densities in tons per cubic yard (extracted from the image)
material_densities = {
    "crushed_stone": {"loose": 1.30, "compacted_95": 1.42},
    "processed_stone": {"loose": 1.50, "compacted_95": 1.95},
    "screenings": {"loose": 1.40, "compacted_95": 1.60},
    "surge_stone": {"loose": 1.35, "compacted_95": 1.65},
    "riprap": {"loose": 1.35, "compacted_95": None},
    "bank_run_gravel": {"loose": 1.38, "compacted_95": 1.65},
    "screened_sand": {"loose": 1.58, "compacted_95": 1.75}
}

# User inputs
length = float(input("Enter length in feet: "))
width = float(input("Enter width in feet: "))
depth = float(input("Enter depth in inches: "))
material = input("Enter material type (e.g., crushed_stone, processed_stone, screenings, etc.): ").strip().lower()
compaction_state = input("Enter compaction state (loose, compacted_95): ").strip().lower()

# Calculate and display the result
total_tons = calculate_tons(length, width, depth, material, compaction_state)

if total_tons is not None:
    print(f"Total weight for {compaction_state} {material}: {total_tons:.2f} tons")