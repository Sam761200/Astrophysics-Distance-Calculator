# Astrophysics Distance Calculator

This project is a simple Python script to calculate the distance to a star from its parallax using the `Astropy` library.

## Requirements

- Python 3.x
- Astropy

## Installation

1. Install Python from [python.org](https://www.python.org/).
2. Install Astropy using pip:

   ```bash
   pip install astropy
   ```

## Usage

Clone the repository to your local machine:

git clone https://github.com/your-username/Astrophysics-Distance-Calculator.git
Navigate to the project directory:

```bash
cd Astrophysics-Distance-Calculator
```

Run the script using Python:

```bash
python astrophysics.py
```

The script calculates the distance to a star given its parallax in milliarcseconds (mas).

```bash
from astropy import units as u
from astropy.coordinates import Distance
```

# Define the parallax in milliarcseconds

```bash
parallax_mas = 50.0  # Example value
```

# Calculate the distance in parsecs

```bash
distance_pc = Distance(parallax=parallax_mas * u.mas).pc
```

# Print the result

```bash
print(f"The distance to the star is {distance_pc:.2f} parsecs")
```

### Explanation

#### Parallax:

The angle measured to determine the distance to nearby stars.
A larger parallax indicates a closer star.

Parsec: A unit of distance equal to approximately 3.26 light-years. One parsec is the distance at which one astronomical unit subtends an angle of one arcsecond.
