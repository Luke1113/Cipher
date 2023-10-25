package Cipher;

import java.util.Scanner;

public class VigenereCipher {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String pl = sc.nextLine();
		pl = pl.toUpperCase();
		String key = sc.nextLine();
		key = key.toUpperCase();
		String tmp = "";
		for(int i = 0; i <= Math.ceil(pl.length()/key.length());i++) {
			tmp += key;
		}
		key = tmp;
		String cil = "";
		for(int i = 0; i < pl.length(); i ++) {
			if(pl.charAt(i)!=' ') {
				cil += (char)(((((int)pl.charAt(i)-(int)'A')+((int)key.charAt(i)-(int)'A'))%26)+(int)'A');
			}
		}
		System.out.println(cil);
	}
}
