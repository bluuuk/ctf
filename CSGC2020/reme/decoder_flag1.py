"""
public static string Encrypt(string clearText)
	{
		string password = "A_Wise_Man_Once_Told_Me_Obfuscation_Is_Useless_Anyway";
		byte[] bytes = Encoding.Unicode.GetBytes(clearText);
		using (Aes aes = Aes.Create())
		{
			Rfc2898DeriveBytes rfc2898DeriveBytes = new Rfc2898DeriveBytes(password, new byte[13]
			{
				73,
				118,
				97,
				110,
				32,
				77,
				101,
				100,
				118,
				101,
				100,
				101,
				118
			});
			aes.Key = rfc2898DeriveBytes.GetBytes(32);
			aes.IV = rfc2898DeriveBytes.GetBytes(16);
			using (MemoryStream memoryStream = new MemoryStream())
			{
				using (CryptoStream cryptoStream = new CryptoStream(memoryStream, aes.CreateEncryptor(), CryptoStreamMode.Write))
				{
					cryptoStream.Write(bytes, 0, bytes.Length);
					cryptoStream.Close();
				}
				clearText = Convert.ToBase64String(memoryStream.ToArray());
			}
		}
		return clearText;
	}
"""

from Crypto.Protocol.KDF import PBKDF2
import base64
from Crypto.Cipher import AES


key = b'A_Wise_Man_Once_Told_Me_Obfuscation_Is_Useless_Anyway'
salt = bytes([73,
				118,
				97,
				110,
				32,
				77,
				101,
				100,
				118,
				101,
				100,
				101,
				118])

# default is 1000 iterations with hmac sha 1 (in python crypto & .net crypto)
# net is statefull with pbkdf2, python is not
gen_bytes = PBKDF2(key, salt, 48) # We need 16, but we're compensating for .NETs 'already called' awesomeness on the GetBytes method
key = gen_bytes[:32]
iv = gen_bytes[32:]

cipher = base64.b64decode("D/T9XRgUcKDjgXEldEzeEsVjIcqUTl7047pPaw7DZ9I=")

aes = AES.new(key=key,iv=iv,mode=AES.MODE_CBC)
plain = aes.decrypt(cipher)

flag = plain.decode('utf-8')
print(flag.replace(" ",""))

