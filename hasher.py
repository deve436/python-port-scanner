import hashlib
import os

def calculate_sha256(file_path):
    """Reads a file and returns its SHA-256 hash."""
    sha256_hash = hashlib.sha256()
    
    try:
        with open(file_path, "rb") as f:
            # Read the file in chunks so we don't crash RAM with large files
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def main():
    print("--- File Integrity Checker (SHA-256) ---")
    file_path = input("Enter the path of the file to check: ").strip().strip('"')
    
    # Check if file exists
    if not os.path.isfile(file_path):
        print("Error: File not found.")
        return

    print("Calculating hash...")
    file_hash = calculate_sha256(file_path)
    
    print("\n" + "="*60)
    print(f"File: {file_path}")
    print(f"SHA-256 Hash: {file_hash}")
    print("="*60)
    
    print("\nCopy the hash above. If the file changes even slightly,")
    print("this hash will look completely different.")

if __name__ == "__main__":
    main()