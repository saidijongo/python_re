import re

text = "5	피치 크러시	88	403	피치,보드카,사워,크랜베리쥬스	쉐이킹"

# Split the text by tabs to get individual fields
fields = text.split('\t')

# Extract the information from the fields
cocktail_id = fields[0]
cocktail_name = fields[1]
quantity = fields[2]
ingredients = fields[3]
preparation_method = fields[4]

# Display the extracted information
print(f"Cocktail ID: {cocktail_id}")
print(f"Cocktail Name: {cocktail_name}")
print(f"Quantity: {quantity}")
print(f"Ingredients: {ingredients}")
print(f"Preparation Method: {preparation_method}")
