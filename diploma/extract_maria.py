import json

def get_text(msg):
    if 'text' not in msg:
        return ""
    text = msg['text']
    if isinstance(text, str):
        return text
    elif isinstance(text, list):
        # Sometimes text is a list of objects/strings
        full_text = ""
        for part in text:
            if isinstance(part, str):
                full_text += part
            elif isinstance(part, dict) and 'text' in part:
                full_text += part['text']
        return full_text
    return ""

def main():
    input_file = 'diploma/result.json'
    output_file = 'diploma/maria_advice.md'
    
    print(f"Loading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    messages = data.get('messages', [])
    print(f"Total messages: {len(messages)}")
    
    # Index messages by ID for quick lookup
    msg_by_id = {msg['id']: msg for msg in messages}
    
    maria_messages = []
    
    # Filter for the last year (assuming current date is Nov 23, 2025)
    cutoff_date = "2024-11-23"
    print(f"Filtering messages after {cutoff_date}...")

    for msg in messages:
        if msg.get('from') == 'Maria':
            if msg.get('date', '') >= cutoff_date:
                maria_messages.append(msg)
            
    print(f"Found {len(maria_messages)} messages from Maria since {cutoff_date}.")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Maria's Advice & Q&A\n\n")
        
        for msg in maria_messages:
            date = msg.get('date', 'Unknown Date')
            answer_text = get_text(msg)
            
            if not answer_text.strip():
                continue
                
            reply_id = msg.get('reply_to_message_id')
            if reply_id and reply_id in msg_by_id:
                original_msg = msg_by_id[reply_id]
                question_text = get_text(original_msg)
                
                f.write(f"> {question_text.replace(chr(10), chr(10) + '> ')}\n\n")
                f.write(f"{answer_text}\n")
            else:
                f.write(f"{answer_text}\n")
            
            f.write("\n---\n\n")

    print(f"Extraction complete. Saved to {output_file}")

if __name__ == "__main__":
    main()
