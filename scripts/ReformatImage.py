import re

def replace_images(input_path, output_path):
    with open(input_path, 'r') as input_file:
        content = input_file.read()

    # Define the regular expression pattern for finding image references
    pattern = r'!\[\[Pasted image (\d+)\.png\]\]'

    # Find all matches of the pattern in the content
    matches = re.findall(pattern, content)

    # Replace each match with the desired format
    replaced_content = content
    for match in matches:
        old_reference = f'![[Pasted image {match}.png]]'
        new_reference = f'{{% include image.html img="Pastedimage{match}.png"%}}'
        replaced_content = replaced_content.replace(old_reference, new_reference)

    with open(output_path, 'w') as output_file:
        output_file.write(replaced_content)

if __name__ == '__main__':
    input_file_path = '/Users/atlas/Desktop/Projects/BastianReality.github.io/_posts/2023-08-19-FirstApp.markdown'
    output_file_path = '/Users/atlas/Desktop/2023-08-19-FirstApp.markdown'

    replace_images(input_file_path, output_file_path)
    print('Images replaced successfully!')
