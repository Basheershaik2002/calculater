import streamlit as st

st.title("Simple Calculator")

# Input numbers
num1 = st.number_input("Enter first number", format="%f")
num2 = st.number_input("Enter second number", format="%f")

# Operation selection
operation = st.selectbox("Select operation", ["Add (+)", "Subtract (-)", "Multiply (*)", "Divide (/)"])

result = None

if st.button("Calculate"):
    if operation == "Add (+)":
        result = num1 + num2
    elif operation == "Subtract (-)":
        result = num1 - num2
    elif operation == "Multiply (*)":
        result = num1 * num2
    elif operation == "Divide (/)":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Error: Division by zero is undefined.")
            result = None

    if result is not None:
        st.success(f"Result: {result}")
