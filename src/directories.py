import os
# Get the directory of the current script
script_directory = os.path.dirname(__file__)

# Get the parent directory (the directory containing the script)
parent_directory = os.path.dirname(script_directory)

#Get the asset directory (the directory containing assets in this project)

asset_path = os.path.join(parent_directory, "assets")

#Image path to the black pawn 'bp.png'
image_path = os.path.join(parent_directory, "assets", "bp.png")

# Print the parent directory
print(f"The parent directory of the current script is: {parent_directory}")
print(f'The asset directory is {asset_path}')