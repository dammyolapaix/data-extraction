from PyPDF2 import PdfReader
import re

file_path = './file.pdf'
reader = PdfReader(file_path)

# Initialize an empty string to store the extracted text
text = ''
print(len(reader.pages))

with open('file.txt', 'w') as f:
    # Iterate through each page in the PDF
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()

    # Use regular expressions to extract information
    user_id_info = re.findall(r'User ID\n(\d+)', text)
    full_name_info = re.findall(r'Full Name\n(.+)', text)
    gender_info = re.findall(r'Gender\n(.+)', text)
    # age_info = re.findall(r'Age:\s*(\d+)', text)
    phone_info = re.findall(r'Phone No.\n(.+)', text)
    position_info = re.findall(r'Position\n(.+)', text)

    # Combine extracted information into the desired format
    formatted_results = []
    for i in range(len(user_id_info)):
        user_id = user_id_info[i]
        full_name = full_name_info[i].strip()
        gender = gender_info[i].strip()
        # age = age_info[i]
        phone_number = phone_info[i]
        position = position_info[i].strip()

        formatted_results.append(f"User ID: {user_id}")
        formatted_results.append(f"Full Name: {full_name}")
        formatted_results.append(f"Gender: {gender}")
        # formatted_results.append(f"Age: {age}")
        formatted_results.append(f"Phone No.: {phone_number}")
        formatted_results.append(f"Position: {position}")
        formatted_results.append("")  # Add a blank line for separation

    # Join the formatted results into a single string
    formatted_output = '\n'.join(formatted_results)

    f.write(formatted_output)
    # f.write(text)
    f.close()
