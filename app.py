import streamlit as st 

def convert_units(category, from_unit, to_unit, value):
    conversion_factors = {
        "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701},
        "Weight": {"Kilogram": 1, "Gram": 1000, "Milligram": 1e6, "Pound": 2.20462, "Ounce": 35.274},
        "Temperature": {"Celsius": 1, "Fahrenheit": 1, "Kelvin": 1},
        "Time": {"Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400},
        "Speed": {"Meter per second": 1, "Kilometer per hour": 3.6, "Miles per hour": 2.23694, "Foot per second": 3.28084},
        "Volume": {"Liter": 1, "Milliliter": 1000, "Cubic meter": 0.001, "Gallon": 0.264172, "Pint": 2.11338},
        "Area": {"Square meter": 1, "Square kilometer": 0.000001, "Square mile": 3.861e-7, "Acre": 0.000247105, "Hectare": 0.0001},
        "Energy": {"Joule": 1, "Kilojoule": 0.001, "Calorie": 0.239006, "Kilocalorie": 0.000239006, "Watt-hour": 0.000277778},
        "Pressure": {"Pascal": 1, "Bar": 1e-5, "PSI": 0.000145038, "Atmosphere": 9.8692e-6},
        "Power": {"Watt": 1, "Kilowatt": 0.001, "Horsepower": 0.00134102},
        "Data Storage": {"Byte": 1, "Kilobyte": 0.001, "Megabyte": 1e-6, "Gigabyte": 1e-9, "Terabyte": 1e-12},
        "Fuel Efficiency": {"Kilometer per liter": 1, "Miles per gallon": 2.35215},
        "Force": {"Newton": 1, "Kilonewton": 0.001, "Pound-force": 0.224809},
        "Angle": {"Degree": 1, "Radian": 0.0174533},
    }
    
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        return value  # Same unit conversion
    
    return value * conversion_factors[category][to_unit] / conversion_factors[category][from_unit]

# Streamlit UI
st.set_page_config(page_title="Unit Converter", layout="centered")

# Styled Header
st.markdown("<h2 style='text-align: center; color: white; background-color: black; padding: 10px; border-radius: 10px;'> Unit Converter</h2>", unsafe_allow_html=True)

categories = [
    "Length", "Weight", "Temperature", "Time", "Speed", "Volume", "Area", "Energy",
    "Pressure", "Power", "Data Storage", "Fuel Efficiency", "Force", "Angle"
]
category = st.selectbox("Select Category", categories)

units = {
    "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
    "Weight": ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Time": ["Second", "Minute", "Hour", "Day"],
    "Speed": ["Meter per second", "Kilometer per hour", "Miles per hour", "Foot per second"],
    "Volume": ["Liter", "Milliliter", "Cubic meter", "Gallon", "Pint"],
    "Area": ["Square meter", "Square kilometer", "Square mile", "Acre", "Hectare"],
    "Energy": ["Joule", "Kilojoule", "Calorie", "Kilocalorie", "Watt-hour"],
    "Pressure": ["Pascal", "Bar", "PSI", "Atmosphere"],
    "Power": ["Watt", "Kilowatt", "Horsepower"],
    "Data Storage": ["Byte", "Kilobyte", "Megabyte", "Gigabyte", "Terabyte"],
    "Fuel Efficiency": ["Kilometer per liter", "Miles per gallon"],
    "Force": ["Newton", "Kilonewton", "Pound-force"],
    "Angle": ["Degree", "Radian"],
}

with st.container():
    col1, col2, col3 = st.columns([3, 1, 3])

    with col1:
        from_unit = st.selectbox("From", units[category])

    with col2:
        st.markdown("<h3 style='text-align: center;'> = </h3>", unsafe_allow_html=True)

    with col3:
        to_unit = st.selectbox("To", units[category])

value = st.number_input("Enter Value", value=0.0, step=0.1)

if st.button("Convert"):
    result = convert_units(category, from_unit, to_unit, value)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
