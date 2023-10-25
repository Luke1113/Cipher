package Cipher;

import java.util.Scanner;

public class MonoalphabeticSubstitution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String pl = sc.nextLine();
		String key = sc.nextLine();
		String ci = "";
		char[][] keyl = new char[26][2];
		String alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		for(int i = 0; i < alpha.length(); i++) {
			keyl[i][0] = alpha.charAt(i);
			keyl[i][1] = key.charAt(i);
		}
		for(int i = 0; i < pl.length(); i++) {
			for(int j = 0; j < key.length(); j++) {
				if(pl.charAt(i) == keyl[j][0]) {
					ci+=keyl[j][1];
					break;
				}
			}
		}
		System.out.println(ci);
	}
}
