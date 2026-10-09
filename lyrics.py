import sys
import time

# Yahan Google se "Channa Mereya full lyrics" search karke baaki ki lines add karein
full_lyrics = """
Get VIP
Login
Arijit Singh
Channa Mereya-Ae Dil Hai Mushkil
Published by
MeetShukla22
Lyrics
Recordings
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
        if line.strip() == "अच्छा चलता हूँ, दुआओं में याद रखना
मेरे ज़िक्र का ज़ुबाँ पे स्वाद रखना
अच्छा चलता हूँ, दुआओं में याद रखना
मेरे ज़िक्र का ज़ुबाँ पे स्वाद रखना
दिल के संदूक़ों में मेरे अच्छे काम रखना
चिट्ठी-तारों में भी मेरा तू सलाम रखना
अँधेरा तेरा मैंने ले लिया
मेरा उजला सितारा तेरे नाम किया
चन्ना मेरेया-मेरेया, चन्ना मेरेया-मेरेया
चन्ना मेरेया-मेरेया बेलीਆ, ਓ ਪਿਆ
चन्ना मेरेया-मेरेया, चन्ना मेरेया-मेरेया
चन्ना मेरेया-मेरेया बेलीਆ, ਓ ਪਿਆ
ओ पिया... पिया... पिया... ओ पिया...
म्म... महफ़िल में तेरी हम ना रहे जो
ग़म तो नहीं है, ग़म तो नहीं है
क़िस्से हमारे नज़दीकियों के
कम तो नहीं है, कम तो नहीं है
कितनी दफ़ा, सुबाह को मेरी
तेरे आँगन में बैठे मैंने शाम किया
चन्ना मेरेया-मेरेया, चन्ना मेरेया-मेरेया
चन्ना मेरेया-मेरेया बेलीਆ, ਓ ਪਿਆ
चन्ना मेरेया-मेरेया, चanna मेरेया-मेरेया
चन्ना मेरेया-मेरेया ओ पिया...
तेरे रुख से अपना रास्ता मोड़ के चला
चंदन हूँ मैं, अपनी ख़ुश्बू छोड़ के चला
मन की माया रख के तेरे तकिए तले
बैरागी, बैरागी का सूती चोला ओढ़ के चला
चन्ना मेरेया-मेरेया, चन्ना मेरेया-मेरेया
चन्ना मेरेया-मेरेया ओ पिया...
सच्ची मोहब्बत शायद वही है
जिसमें जूनून है, जिसमें जूनून है
पर दो दिलों की यारी में भी तो
कितना सुकून है, कितना सुकून है
देके मुझे तेरी जुदाई
मेरे रब ने मुझे पैग़ाम दिया
चन्ना मेरेया-मेरेया, चन्ना मेरेया-मेरेया
चन्ना मेरेया-मेरेया बेलियाँ":
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
