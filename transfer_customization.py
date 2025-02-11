import json
import sys

def load_json(filename):
    """Load JSON from a file."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def build_old_customization_index(old_data):
    """
    Build a dictionary mapping channel names (exact string)
    to their 'Customization' dictionary from the old JSON.
    """
    index = {}
    for group in old_data.get("Groups", []):
        for channel in group.get("Channels", []):
            name = channel.get("Name")
            if name:
                index[name] = channel.get("Customization")
    return index

def transfer_customization(new_data, old_index):
    """
    For each channel in the new JSON data, if its Name exists in the old index,
    replace its 'Customization' field with the one from the old data.
    """
    for group in new_data.get("Groups", []):
        for channel in group.get("Channels", []):
            name = channel.get("Name")
            if name and name in old_index:
                channel["Customization"] = old_index[name]
    return new_data

def main():
    if len(sys.argv) != 4:
        print("Usage: python transfer_customization.py <old_json_file> <new_json_file> <output_json_file>")
        sys.exit(1)
        
    old_file = sys.argv[1]
    new_file = sys.argv[2]
    output_file = sys.argv[3]
    
    # Load both JSON files.
    old_data = load_json(old_file)
    new_data = load_json(new_file)
    
    # Build an index from old JSON mapping channel names to customization.
    old_index = build_old_customization_index(old_data)
    
    # Transfer the customization from old JSON into the new JSON structure.
    merged_data = transfer_customization(new_data, old_index)
    
    # Write the merged JSON to the output file.
    with open(output_file, "w", encoding="utf-8") as f:
        # Using ensure_ascii=False preserves non-ASCII characters (e.g. ñ) as-is.
        json.dump(merged_data, f, indent=2, ensure_ascii=False)
    
    print(f"Merged JSON written to {output_file}")

if __name__ == "__main__":
    main()
