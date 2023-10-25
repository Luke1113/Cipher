package Cipher;

import java.util.Scanner;

public class CaesarCipher {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		String pl = sc.nextLine();
		pl = pl.toUpperCase();
		char key = sc.nextLine().charAt(0);
		key = Character.toUpperCase(key);
		String cil = "";
		for(int i = 0; i < pl.length(); i ++) {
			if(pl.charAt(i)!=' ') {
				cil += (char)(((((int)pl.charAt(i)-(int)'A')+((int)key-(int)'A'))%26)+(int)'A');
			}
		}
		System.out.println(cil);
	}
}

