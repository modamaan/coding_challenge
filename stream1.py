import streamlit as st
import ast

def max_occur_chance(arr, lookup):
    dic_count = {}

    for key in lookup:
        count = 0
        for num in arr:
            if num in lookup[key]:
                count += 1
        dic_count[key] = count

    max_key = None
    max_count = -1
    for key in dic_count:
        if dic_count[key] > max_count:
            max_count = dic_count[key]
            max_key = key

    return max_key

def main():
    st.title("Max Occurrence Chance Finder")

    # Input for array
    arr_input = st.text_input("Enter array (comma-separated):")

    if not arr_input:
        st.warning("Please enter an array.")
        return

    try:
        arr = ast.literal_eval(arr_input)
        if not isinstance(arr, list):
            raise ValueError("Input is not a list")
        arr = [int(x) for x in arr]
    except ValueError as ve:
        st.error(f"Error processing the array: {ve}")
        return
    except SyntaxError as se:
        st.error("Invalid syntax in the array input. Please enter a valid list representation.")
        return

    # Input for lookup dictionary
    lookup_input = st.text_area("Enter lookup dictionary (in JSON format):")

    # Submit button
    if st.button("Submit"):
        try:
            lookup = ast.literal_eval(lookup_input)
        except (SyntaxError, ValueError) as e:
            st.error(f"Error processing the lookup dictionary: {e}")
            return

        # Display result
        if arr and lookup:
            result = max_occur_chance(arr, lookup)
            st.success(f"The key with the maximum occurrences is: {result}")

if __name__ == "__main__":
    main()