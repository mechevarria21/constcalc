def inches_to_feet(inches):
    return inches / 12.0

# Constants - Single Unit Specifications (inches)
HEIGHT_INCHES = 45
WIDTH_INCHES = 77
LENGTH_INCHES = 90
END_CAP_LENGTH_INCHES = 25.7
SURFACE_AREA_SF = 48.125
CHAMBER_STORAGE_CF = 109.9

# Constants - System Specifications
QUANTITY_FACING_LONG_LENGTH = 10 # chamber columns
QUANTITY_FACING_SHORT_WIDTH = 10 # chamber rows

# Constants - Stone Specifications (inches)
STONE_LANE_ENDS_INCHES = 6
STONE_BETWEEN_LANES_INCHES = 6
STONE_END_CAPS_INCHES = 6
STONE_BOTTOM_INCHES = 6 
STONE_TOP_INCHES = 6

# Calculated values in feet
height_feet = inches_to_feet(HEIGHT_INCHES)
width_feet = inches_to_feet(WIDTH_INCHES)
length_feet = inches_to_feet(LENGTH_INCHES)
end_cap_length_feet = inches_to_feet(END_CAP_LENGTH_INCHES)

stone_lane_ends_feet = inches_to_feet(STONE_LANE_ENDS_INCHES)
stone_between_lanes_feet = inches_to_feet(STONE_BETWEEN_LANES_INCHES)
stone_end_caps_feet = inches_to_feet(STONE_END_CAPS_INCHES)
stone_bottom_feet = inches_to_feet(STONE_BOTTOM_INCHES)
stone_top_feet = inches_to_feet(STONE_TOP_INCHES)

# _________________________________________________________________________

# System Width Calculations
system_units_width = QUANTITY_FACING_SHORT_WIDTH * width_feet
system_stone_between_width = (QUANTITY_FACING_SHORT_WIDTH - 1) * stone_between_lanes_feet
system_stone_ends_width = 2 * stone_lane_ends_feet
total_system_width = system_units_width + system_stone_between_width + system_stone_ends_width

# System Length Calculations
system_units_length = QUANTITY_FACING_LONG_LENGTH * length_feet
system_end_caps_length = 2 * end_cap_length_feet
system_stone_ends_length = 2 * stone_end_caps_feet
total_system_length = system_units_length + system_end_caps_length + system_stone_ends_length

# System Height Calculations
total_system_height = height_feet + stone_top_feet + stone_bottom_feet

# Final System Calculations
system_area_sf = total_system_width * total_system_length
system_volume_cf = system_area_sf * total_system_height

# Stone Calculations
Total_Chamber_Volume_CF = CHAMBER_STORAGE_CF * (QUANTITY_FACING_LONG_LENGTH * QUANTITY_FACING_SHORT_WIDTH)
leftover_stone_volume_cf = system_volume_cf - Total_Chamber_Volume_CF
stone_depth_feet = (leftover_stone_volume_cf / system_area_sf)
stone_depth_yards = (system_area_sf * stone_depth_feet) / 27 
stone_loose_quantity = stone_depth_yards * 1.35
stone_compacted_quantity = stone_depth_yards * 2
total_stone_quantity = (stone_loose_quantity + stone_compacted_quantity) / 2

# Print System Width Calculations
print("\nSystem Width:")
print(f"Units:            {QUANTITY_FACING_SHORT_WIDTH} × {width_feet:.2f} ft = {system_units_width:.4f} ft")
print(f"Stone In Between: {QUANTITY_FACING_SHORT_WIDTH-1} × {stone_between_lanes_feet:.2f} ft = {system_stone_between_width:.4f} ft")
print(f"Stone Ends:       2 × {stone_lane_ends_feet:.2f} ft = {system_stone_ends_width:.4f} ft")
print(f"Total Width:      {total_system_width:.4f} ft")

# Print System Length Calculations
print("\nSystem Length:")
print(f"Units:            {QUANTITY_FACING_LONG_LENGTH} × {length_feet:.2f} ft = {system_units_length:.4f} ft")
print(f"End Caps:         2 × {end_cap_length_feet:.2f} ft = {system_end_caps_length:.4f} ft")
print(f"Stone Ends:       2 × {stone_end_caps_feet:.2f} ft = {system_stone_ends_length:.4f} ft")
print(f"Total Length:     {total_system_length:.4f} ft")

# Print System Height Calculations
print("\nSystem Height:")
print(f"Top Stone:        {stone_top_feet:.2f} ft")
print(f"Unit:             {height_feet:.2f} ft")
print(f"Bottom Stone:     {stone_bottom_feet:.2f} ft")
print(f"Total Height:     {total_system_height:.2f} ft")

# Print Final System Calculations
print("\nFinal System Dimensions:")
print(f"Width:            {total_system_width:.4f} ft")
print(f"Length:           {total_system_length:.4f} ft")
print(f"Height:           {total_system_height:.2f} ft")
print(f"Area:             {system_area_sf:.4f} sf")
print(f"Volume:           {system_volume_cf:.4f} cf")

# Print Stone Calculations
print("\nStone Calculations:")
print(f"Total Chamber Volume:     {Total_Chamber_Volume_CF:.4f} cf")
print(f"Leftover Stone Volume:    {leftover_stone_volume_cf:.4f} cf")
print(f"Stone Depth:             {stone_depth_feet:.4f} ft")
print(f"Stone Depth (yards):     {stone_depth_yards:.4f} yards³")
print(f"Stone Loose Quantity:    {stone_loose_quantity:.4f} tons")
print(f"Stone Compacted:         {stone_compacted_quantity:.4f} tons")
print(f"Total Stone Required:    {total_stone_quantity:.4f} tons")
