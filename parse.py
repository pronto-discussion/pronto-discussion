import json

def parse_chat(file_path):
    with open(file_path, 'r') as file:
        chat_data = file.read()
    
    # Split the chat data into lines
    lines = chat_data.split('\n')
    
    # Parse each line and format it
    formatted_chat = []
    for line in lines:
        if ': ' in line:
            username, message = line.split(': ', 1)
            formatted_chat.append({'username': username, 'message': message})
    
    return formatted_chat

def save_to_json(data, output_path):
    with open(output_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    input_file = '/home/paul/Desktop/pronto-discussion/Pronto_Discussion_AC_Text_Chat.json'
    output_file = '/home/paul/Desktop/pronto-discussion/formatted_chat.json'
    
    chat_data = parse_chat(input_file)
    save_to_json(chat_data, output_file)
    print(f"Formatted chat saved to {output_file}")
