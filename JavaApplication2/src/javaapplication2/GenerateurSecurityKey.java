/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package javaapplication2;

import java.security.Key;
import java.security.NoSuchAlgorithmException;
import javax.crypto.KeyGenerator;
/**
 *
 * @author azhar
 */
public class GenerateurSecurityKey {


    public static void main(String[] args) {
        try {
            KeyGenerator keyGen = KeyGenerator.getInstance("HmacSHA256");
            Key secretKey = keyGen.generateKey();
            byte[] secretKeyBytes = secretKey.getEncoded();
            String secretKeyString = java.util.Base64.getEncoder().encodeToString(secretKeyBytes);

            System.out.println("Secret Key: " + secretKeyString);
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
    }
}
