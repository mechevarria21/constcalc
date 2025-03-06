def calculate_tonnage(area_sf, depth_in, factor):
    """
    Calculate the tonnage of material required based on area, depth, and conversion factor.

    Parameters:
    - area_sf (float): The total area in square feet.
    - depth_in (float): The depth of material in inches.
    - factor (float): The conversion factor (e.g., 39.15).

    Returns:
    - float: The required tonnage.
    """
    # Step 1: Calculate cubic yards (area divided by factor)
    cubic_yards = area_sf / factor
    
    # Step 2: Calculate the material conversion number based on depth
    conversion_number = depth_in / 4  # Depth divided by 4
    
    # Step 3: Calculate tonnage
    tonnage = cubic_yards * conversion_number
    
    return tonnage