# Construction Calculator Suite

A collection of web-based calculators for construction material calculations. This application provides easy-to-use tools for calculating material quantities for asphalt paving, concrete flatwork, and monolithic curbs.

## Project Structure

```
.
├── index.html              # Main landing page
├── path/                   # Asphalt calculator
│   └── index.html         # Asphalt tonnage calculator page
├── flatwork/              # Concrete flatwork calculator
│   └── index.html         # Concrete flatwork calculator page
├── monocurb/              # Monolithic curb calculator
│   └── index.html         # Monolithic curb calculator page
├── Example.py             # Python implementation of asphalt calculations
└── monocurb.py           # Python implementation of curb calculations
```

## Calculators

### 1. Asphalt Calculator
- **File**: `path/index.html`
- **Purpose**: Calculates asphalt tonnage for paving projects
- **Inputs**:
  - Area (square feet)
  - Depth (inches)
  - Factor (default: 39.15)
- **Formula**: `tonnage = (area_sf / factor) * (depth_in / 4)`
- **Reference Implementation**: `Example.py`

### 2. Concrete Flatwork Calculator
- **File**: `flatwork/index.html`
- **Purpose**: Calculates concrete volume for flat surfaces
- **Inputs**:
  - Length (feet)
  - Width (feet)
  - Thickness (inches)
  - Spillage Factor (default: 1.05)
- **Formula**: `cubic_yards = (length * width * (thickness/12) / 27) * spillage`

### 3. Monolithic Curb Calculator
- **File**: `monocurb/index.html`
- **Purpose**: Calculates concrete volume for monolithic curbs
- **Constants**: Fixed curb width of 14 inches
- **Inputs**:
  - Curb Height (inches)
  - Slab Height (inches)
  - Curb Length (feet)
  - Spillage Factor (default: 1.1)
- **Formula**: See `monocurb.py` for detailed calculation
- **Reference Implementation**: `monocurb.py`

## Technical Details

### Frontend
- **Framework**: None (vanilla JavaScript)
- **CSS**: Tailwind CSS (via CDN)
- **Responsive**: Yes, mobile-friendly design
- **Browser Support**: Modern browsers (Chrome, Firefox, Safari, Edge)

### Calculations
- All calculations are performed client-side in JavaScript
- Python files (`Example.py`, `monocurb.py`) serve as reference implementations
- Each calculator includes spillage/waste factors for real-world accuracy
- Results are rounded to 2 decimal places

### UI Features
- Clean, consistent design across all calculators
- Real-time calculation updates
- Input validation
- Mobile-responsive layout
- Clear result display

## Usage Notes

1. All calculators update results in real-time as values are entered
2. Default spillage factors are pre-set but can be adjusted:
   - Flatwork: 1.05 (5% extra)
   - Monolithic Curb: 1.1 (10% extra)
   - Asphalt: Factor of 39.15 for standard conversion
3. Measurements should be entered in:
   - Lengths/Widths: Feet
   - Heights/Depths: Inches
   - Areas: Square Feet

## Development Notes

- The application is entirely frontend-based with no backend dependencies
- Calculations are mirrored in both JavaScript and Python for reference
- Tailwind CSS is loaded via CDN for easy maintenance
- Each calculator is self-contained in its own directory for modularity

## Future Improvements

Potential areas for enhancement:
1. Add input validation with error messages
2. Include unit conversion options
3. Add ability to save/export calculations
4. Implement print-friendly results
5. Add additional construction calculators as needed 