# Function to convert inches to feet
def inches_to_feet(inches):
    return inches / 12


height_in_const = 30
width_in_const = 52
length_in_const = 85
end_cap_length_in_const = 18
chamber_storage_volume_const = 2.83

# Convert dimensions from inches to feet
height_ft = inches_to_feet(height_in_const)
width_ft = inches_to_feet(width_in_const)
length_ft = inches_to_feet(length_in_const)
end_cap_length_ft = inches_to_feet(end_cap_length_in_const)



# Function to calculate single unit specifications
def single_unit_specifications(height_in, width_in, length_in, end_cap_length_in, chamber_storage_volume):


    # Calculate surface area and chamber storage volume
    surface_area = width_ft * length_ft
    chamber_storage_volume_ft3 = chamber_storage_volume  # Assuming the input is already in cubic feet

    return {
        'height_ft': height_ft,
        'width_ft': width_ft,
        'length_ft': length_ft,
        'end_cap_length_ft': end_cap_length_ft,
        'surface_area': surface_area,
        'chamber_storage_volume_ft3': chamber_storage_volume_ft3
    }

# Example usage of single_unit_specifications function
single_unit_specs = single_unit_specifications(height_in_const, width_in_const, length_in_const, end_cap_length_in_const, chamber_storage_volume_const)
print(single_unit_specs)

# Function to calculate system specifications
def system_specifications(long_units, short_units, stone_end_in, stone_between_in, stone_end_cap_in, stone_bottom_in, stone_top_in):
    # Convert stone dimensions from inches to feet
    stone_end_ft = inches_to_feet(stone_end_in)
    stone_between_ft = inches_to_feet(stone_between_in)
    stone_end_cap_ft = inches_to_feet(stone_end_cap_in)
    stone_bottom_ft = inches_to_feet(stone_bottom_in)
    stone_top_ft = inches_to_feet(stone_top_in)

    # Calculate system dimensions based on unit and stone specifications
    system_width = (long_units * width_ft) + ((long_units - 1) * stone_between_ft) + (2 * stone_end_ft)
    system_length = (short_units * length_ft) + (2 * end_cap_length_ft) + (2 * stone_end_ft)
    system_height = stone_bottom_ft + height_ft + stone_top_ft
    system_length = (short_units * stone_between_ft) + ((short_units + 1) * stone_end_ft)
    system_height = stone_bottom_ft + stone_top_ft + stone_end_ft

    return {
        'system_width_ft': system_width,
        'system_length_ft': system_length,
        'system_height_ft': system_height
    }

# Example usage of system_specifications function
system_specs = system_specifications(12, 6, 12, 9, 25.7, 12, 12)
print(system_specs)

# Function to calculate system area and volume
def system_calculations(system_width_ft, system_length_ft, system_height_ft):
    # Calculate area and volume
    area = system_width_ft * system_length_ft
    volume = area * system_height_ft

    return {
        'area_ft2': area,
        'volume_ft3': volume
    }

# Example usage of system_calculations function
system_calc = system_calculations(system_specs['system_width_ft'], system_specs['system_length_ft'], system_specs['system_height_ft'])
print(system_calc)

# Function to calculate stone volumes
def stone_calculations(system_volume_ft3, single_chamber_volume_ft3, number_of_chambers):
    # Calculate total chamber volume and leftover stone volume
    total_chamber_volume = single_chamber_volume_ft3 * number_of_chambers
    leftover_stone_volume = system_volume_ft3 - total_chamber_volume

    return {
        'total_chamber_volume_ft3': total_chamber_volume,
        'leftover_stone_volume_ft3': leftover_stone_volume
    }

# Example usage of stone_calculations function
stone_calc = stone_calculations(system_calc['volume_ft3'], single_unit_specs['chamber_storage_volume_ft3'], 50)
print(stone_calc)
