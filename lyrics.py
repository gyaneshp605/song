import sys
import time
# Google se "Channa Mereya full lyrics Hinglish" search karein aur baaki ki lines yahan add karein
full_lyrics = """
Acha chalta hoon

Duaon mein yaad rakhna
Mere zikr ka zubaan pe swaad rakhna

Acha chalta hoon
Duaon mein yaad rakhna
Mere zikr ka zubaan pe swaad rakhna

Dil ke sandookon mein
Mere ache kaam rakhna
Chitthi taaron mein bhi
Mera tu salaam rakhna

Andhera tera maine le liya
Mera ujla sitaara tere naam kiya

Channa mereya mereya
Channa mereya mereya
Channa mereya mereya beliya
O piya..

Channa mereya mereya
Channa mereya mereya
Channa mereya mereya beliya
O piya..


O piyaa.. piya.. piya..
O Piyaa.. Oohh..

Mm.. mehfil me teri hum naa reh jo
Gham toh nahi hai, gham toh nahi hai
Qisse humare nazdeekiyon ke
Kam to nahi hai, kam to nahi hai
Kitni dafaa subah ko meri
Tere aangan mein baithe shaam kiya

Channa mereya mereya
Channa mereya mereya
Channa mereya mereya beliya
O piya..

Channa mereya mereya
Channa mereya mereya
Channa mereya mereya beliya
O piyaaaaaaaaa..

O Piyaa.. piyaa..

(Channa mereya mereya
Channa mereya mereya
Channa mereya mereya o piya

Channa mereya mereya
Channa mereya mereya
Channa mereya mereya beliya
O piya..

Tere rukh se apna raasta mod ke chala
Chandan hoon main
Apni khushboo chodke chala

Mann ki maya rakhke tere takiye tale

(Channa mereya mereya
Channa mereya mereya
Channa mereya mereya)

O Piya..
"""

def play_lyrics():
    print("\n--- Playing Lyrics ---\n")
    
    for line in full_lyrics.strip().split('\n'):
        # Agar line khali hai toh seedha agli line par jayein, bina ruke
        if line.strip() == "":
            print()
            continue
            
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.08)  # Sirf letters ki slow typing yahan chalegi
        
        print()  # Line complete hote hi turant agli line shuru hogi (koi delay nahi)

    print("\n--- The End ---\n")

if __name__ == "__main__":
    play_lyrics()
