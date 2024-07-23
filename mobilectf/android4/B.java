import java.security.MessageDigest;
import java.util.Arrays;
import java.util.Calendar;
import java.util.Objects;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;

/* loaded from: classes3.dex */
public class B {
    static final /* synthetic */ boolean $assertionsDisabled = false;
    public String key_1 = "";
    public String key_2 = "";
    public String flag_1 = "1fI9wJ1OG++uTPACK0qmibKk98xRknYSE0c6BOoozbM=";
    public String flag_2 = "w96ZjUymmZVJUbVIdUgcD/jpu7O8HJHMmUnXVev4T6w=";

    public B(){
        getKeys();
    }

    public String flag() {
        String real_Flag1 = "Flag{Try_again}";
        String real_Flag2 = "Flag{Try_again}";
        try {
            real_Flag1 = decrypt(getFlag_1(), getKey_1());
        } catch (Exception e) {
            e.printStackTrace();
            try {
                real_Flag2 = decrypt(getFlag_2(), getKey_2());
            } catch (Exception e2) {
                e.printStackTrace();
            }
        }
        return real_Flag1 + " " + real_Flag2;
    }

    private void getKeys() {
        Calendar calendar = Calendar.getInstance();
        int date = calendar.getWeekYear();
        setKey_1(String.valueOf(date));
        setKey_2("Intent { }");
    }

    private void encrypt(String data) throws Exception {
        byte[] key = getKey_1().getBytes("UTF-8");
        MessageDigest sha = MessageDigest.getInstance("SHA-1");
        SecretKeySpec secretKeySpec = new SecretKeySpec(Arrays.copyOf(sha.digest(key), 16), "AES");
        Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
        cipher.init(1, secretKeySpec);
        byte[] encryptedBytes = cipher.doFinal(data.getBytes("UTF-8"));
        setFlag_1(Base64.getEncoder().encodeToString(encryptedBytes, 0));
        byte[] key2 = getKey_2().getBytes("UTF-8");
        MessageDigest sha2 = MessageDigest.getInstance("SHA-1");
        SecretKeySpec secretKeySpec2 = new SecretKeySpec(Arrays.copyOf(sha2.digest(key2), 16), "AES");
        Cipher cipher2 = Cipher.getInstance("AES/ECB/PKCS5Padding");
        cipher2.init(1, secretKeySpec2);
        byte[] encryptedBytes2 = cipher2.doFinal(data.getBytes("UTF-8"));
        setFlag_2(Base64.getEncoder().encodeToString(encryptedBytes2, 0));
    }

    public String decrypt(String encryptedData, String key) throws Exception {
        byte[] keyBytes = key.getBytes("UTF-8");
        MessageDigest sha = MessageDigest.getInstance("SHA-1");
        SecretKeySpec secretKeySpec = new SecretKeySpec(Arrays.copyOf(sha.digest(keyBytes), 16), "AES");
        Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
        cipher.init(2, secretKeySpec);
        byte[] encryptedBytes = Base64.getDecoder().decode(encryptedData, 0);
        byte[] decryptedBytes = cipher.doFinal(encryptedBytes);
        return new String(decryptedBytes, "UTF-8");
    }

    public String getFlag_1() {
        return this.flag_1;
    }

    public void setFlag_1(String flag_1) {
        this.flag_1 = flag_1;
    }

    public String getKey_2() {
        return this.key_2;
    }

    public void setKey_2(String key_2) {
        this.key_2 = key_2;
    }

    public String getKey_1() {
        return this.key_1;
    }

    public void setKey_1(String key_1) {
        this.key_1 = key_1;
    }

    public String getFlag_2() {
        return this.flag_2;
    }

    public void setFlag_2(String flag_2) {
        this.flag_2 = flag_2;
    }
}