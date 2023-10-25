package Cipher;

import java.util.Scanner;

public class StreamCipher {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		String[][] chl = 
				{{".","11011"},{",","01000"},{"a","00011"},{"b","11001"},{"c","01110"},{"d","01001"},
			     {"e","00001"},{"f","01101"},{"g","11010"},{"h","10100"},{"i","00110"},{"j","01011"},
			     {"k","01111"},{"l","10010"},{"m","11100"},{"n","01100"},{"o","11000"},{"p","10110"},
			     {"q","10111"},{"r","01010"},{"s","00101"},{"t","10000"},{"u","00111"},{"v","11110"},
			     {"w","10011"},{"x","11101"},{"y","10101"},{"z","10001"}};
		String seed;
		seed = "1011100110";
//		seed = sc.nextLine();
		String pl;
		pl = "iloveanapple";
//		pl = sc.nextLine();
		String plb = "";
		String cib = "";
		String ci = "";
		for(int i = 0; i < pl.length(); i++) {
			for(int j = 0; j < chl.length; j++) {
				if(pl.charAt(i) == chl[j][0].charAt(0)) {
					plb += chl[j][1];
					break;
				}
			}
		}
		int count = 0;
		
		for(int i = 0; i < 100; i++) {
			if(seed.length() >= plb.length()) {
				break;
			}
			if(((int)(seed.charAt(count)) + (int)(seed.charAt(count + 3)) + (int)(seed.charAt(count + 4))) % 2 == 0) {
				seed += "0";
			}
			else {
				seed += "1";
			}
			count++;			
		}
		for(int i = 0; i < plb.length(); i++) {
			if(((int)(seed.charAt(i)) + (int)(plb.charAt(i))) % 2 == 0) {
				cib += "0";
			}
			else {
				cib += "1";
			}
		}
		for(int i = 0; i < pl.length(); i++) {
			String tmp = "";
			for(int j = i; j < i + 5; j++) {
				tmp += cib.charAt(j);
			}
			for(int j = 0; j < chl.length; j++) {
				if(tmp.equals(chl[j][1])) {
					ci += chl[j][0];
				}
			}
		}
		System.out.println(ci);
	}
}
