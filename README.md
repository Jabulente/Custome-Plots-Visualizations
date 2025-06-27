# Tanzania Flag Generator with Matplotlib

![Tanzania Flag](Resources/TZ.jpg)

## Project Overview
This Python project generates the national flag of Tanzania using the Matplotlib library with precise geometric calculations and official color specifications. The implementation accurately renders the flag's diagonal bands according to the official 2:3 aspect ratio and color scheme.

## Key Features
- **Geometric Precision**: Calculates diagonal band positions using trigonometric functions
- **Official Colors**: Uses exact hex codes from Tanzania's flag specifications
- **Dynamic Rendering**: Adapts to any resolution while maintaining correct proportions
- **Smooth Transitions**: Implements interpolation for clean band edges
- **Matplotlib Integration**: Leverages industry-standard visualization library

## Flag Specifications
| Aspect Ratio | Diagonal Band Width | Color Specifications |
|-------------|---------------------|----------------------|
| 2:3 | Black band = 1/6 of diagonal length<br>Yellow borders = 1/12 of diagonal length | **Green**: [`#1EB53A`](https://www.schemecolor.com/tanzania-flag-colors.php) <br> [![#1EB53A](https://img.shields.io/badge/Green-%231EB53A?style=for-the-badge&link=https://www.schemecolor.com/tanzania-flag-colors.php)](https://www.schemecolor.com/tanzania-flag-colors.php) <br><br> **Black**: [`#000000`](https://www.schemecolor.com/tanzania-flag-colors.php) <br> [![Black](https://img.shields.io/badge/Black-%23000000?style=for-the-badge&link=https://www.schemecolor.com/tanzania-flag-colors.php)](https://www.schemecolor.com/tanzania-flag-colors.php) <br><br> **Yellow**: [`#FCD116`](https://www.schemecolor.com/tanzania-flag-colors.php) <br> [![Yellow](https://img.shields.io/badge/Yellow-%23FCD116?style=for-the-badge&link=https://www.schemecolor.com/tanzania-flag-colors.php)](https://www.schemecolor.com/tanzania-flag-colors.php) <br><br> **Blue**: [`#00A3DD`](https://www.schemecolor.com/tanzania-flag-colors.php) <br> [![Blue](https://img.shields.io/badge/Blue-%2300A3DD?style=for-the-badge&link=https://www.schemecolor.com/tanzania-flag-colors.php)](https://www.schemecolor.com/tanzania-flag-colors.php) |


## Requirements
- Python 3.6+
- Matplotlib
- NumPy

Install dependencies with:
```bash
pip install matplotlib numpy
```

## Project Structure
```
tanzania-flag/
├── generate_flag.py    # Main flag generation script
├── tanzania_flag.png   # Example output image
├── README.md           # This documentation
└── requirements.txt    # Dependency list
```

## Usage
Run the script to generate and display the flag:
```bash
python generate_flag.py
```

To save the flag as a PNG file, uncomment the save line in the script:
```python
plt.savefig('tanzania_flag.png', dpi=300, bbox_inches='tight')
```

## Technical Implementation
The flag is constructed using four calculated diagonal lines that define the color regions:

1. **Geometric Calculations**:
   - Diagonal slope = height/width (2/3)
   - Band offsets derived from diagonal length (√(width² + height²))
   - Four parallel diagonals define band boundaries

2. **Color Regions**:
   - Upper green triangle: Above top yellow border
   - Yellow borders: Above and below black band
   - Black central band: Between inner boundaries
   - Lower blue triangle: Below bottom yellow border

3. **Precision Techniques**:
   - `np.linspace` for high-resolution x-values
   - `fill_between` with interpolation for smooth edges
   - Aspect ratio locking for correct proportions

## Output
The script generates a vector-accurate representation of the Tanzanian flag:
- 2:3 width-height ratio
- Diagonal band at 30-degree angle
- Correct band widths and color positioning
- High-resolution output suitable for scaling

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
