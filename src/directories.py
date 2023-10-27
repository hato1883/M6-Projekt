import os
# Get the directory of the current script
script_directory = os.path.dirname(__file__)

# Get the parent directory (the directory containing the script)
parent_directory = os.path.dirname(script_directory)

#asset directory


asset_path = os.path.join(parent_directory, "assets")



image_path = os.path.join(parent_directory, "images", "your_image.png")
# Print the parent directory

print(f"The parent directory of the current script is: {parent_directory}")
print(f'The asset directory is {asset_path}')