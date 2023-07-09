# Tuples are commonly used for Unchanging data:
months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

# Tuple can be used as keys in dictionaries
locations = {
    (35.68995, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New York Office",
    (37.7749, 122.4194): "San Francisco Office"
}
# Some dictionary method like .items() return tuples
cat = {'name': 'biscuit', 'age': 0.5, 'favorite_toy': 'my chapstic'}
print(cat.items())
