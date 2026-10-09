import sys
import time

# Yahan Google se "Channa Mereya full lyrics" search karke baaki ki lines add karein
full_lyrics = """
Achha chalta hoon
Duaaon mein yaad rakhna
Mere zikr ka zubaan pe swaad rakhna
Dil ke sandookon mein mere achhe kaam rakhna
"""

def play_lyrics():
    print("\n--- Playing Lyrics ---\n")
    
    for line in full_lyrics.strip().split('\n'):
        if line.strip() == "":
            print()
            time.sleep(0.5)
            continue
            
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.08)  # Typing speed
        print()
        time.sleep(1.5)  # Line delay

    print("\n--- The End ---\n")

if __name__ == "__main__":
    play_lyrics()
