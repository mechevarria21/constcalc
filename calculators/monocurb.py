def mono_curb_cy(curb_height, slab_height, curb_length, spillage):
    CURB_WIDTH = 14  # Constant curb width in inches
    
    # Calculate curb height difference
    curb_diff = curb_height - slab_height
    
    # Convert measurements to feet
    cheight = curb_diff / 12
    cwidth = CURB_WIDTH / 12
    
    # Calculate cubic feet volume
    cf = curb_length * cheight * cwidth
    
    # Convert cubic feet to cubic yards
    cy = cf / 27
    
    # Apply spillage factor
    result = cy * spillage
    
    return result