import csv
import sys

def parse_log(file_path):
    warnings = []
    
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            
            if not line:
                continue
            
            # doxygen format: $file:$line: $text
            parts = line.split(':', 2)
            if len(parts) < 3:
                continue
                
            file_name = parts[0].strip()
            line_num = parts[1].strip()
            message = parts[2].strip()
            
            # Check line num
            if not line_num.isdigit():
                continue
            
            warnings.append({
                'Line': line_num,
                'File': file_name,
                'Message': message
            })
    
    return warnings

def save_csv(warnings, output):
    with open(output, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Line', 'File', 'Message'])
        writer.writeheader()
        for w in warnings:
            writer.writerow(w)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python parser.py <log_file>")
        sys.exit(1)
    
    log_file = sys.argv[1]
    output_file = 'warnings.csv'
    
    warnings = parse_log(log_file)
    save_csv(warnings, output_file)
    
    print(f"Done! Found {len(warnings)} warnings")
    print(f"Saved to {output_file}")