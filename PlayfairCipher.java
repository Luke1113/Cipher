package Cipher;

import java.util.Scanner;

public class PlayfairCipher {
	private static int[] GetLocation(char cha, char[][] gri) {
		int[] tmp = new int[2];
		bre:
		for(int i = 0; i < 5; i++) {
			for(int j = 0; j < 5; j++) {
				if(gri[i][j] == cha) {
					tmp[0] = i;
					tmp[1] = j;
					break bre;
				}
			}
		}
		return tmp;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		char[][] grid = new char[5][5];
		String pl = sc.nextLine();
		String key = sc.nextLine();
		String inGrid = "";
		String pk = key + "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		String tpl = "";
		String ttpl = "";
		String[] pll;
		String ci = "";
		int count = -1;
		for(int i = 0; i < 5; i++) {
			for(int j = 0; j < 5; j++) {
				while(true) {
					count += 1;
					char tmp = pk.charAt(count);
					if(inGrid.contains("" + tmp) == false) {
						if(tmp == 'J' || tmp == 'I') {
							inGrid += "IJ";
							grid[i][j] = 'I';
							break;
						}
						inGrid += tmp;
						grid[i][j] = tmp;
						break;
					}
					
				}
			}
		}
		for(int i = 0; i < pl.length(); i++) {
			if(pl.charAt(i) != ' ') {
				tpl += pl.charAt(i);
			}
		}
		for(int i = 0; i < tpl.length() - 1; i += 2) {
			if(tpl.charAt(i) == tpl.charAt(i + 1)) {
				ttpl += tpl.charAt(i) + "X" + tpl.charAt(i + 1);
			}
			else {
				ttpl += "" + tpl.charAt(i) + tpl.charAt(i + 1);
			}
		}
		if(ttpl.length() % 2 == 1) {
			ttpl += "X";
		}
		pll = new String[ttpl.length()/2];
		for(int i = 0; i < pll.length; i++) {
			pll[i] = "" + ttpl.charAt(i * 2) + ttpl.charAt(i * 2 + 1);
		}
		for(int i = 0; i < pll.length; i++) {
			if(GetLocation(pll[i].charAt(0),grid)[0] == GetLocation(pll[i].charAt(1),grid)[0]) {
				ci += grid[GetLocation(pll[i].charAt(0),grid)[0]][(GetLocation(pll[i].charAt(0),grid)[1] + 1) % 5];
				ci += grid[GetLocation(pll[i].charAt(1),grid)[0]][(GetLocation(pll[i].charAt(1),grid)[1] + 1) % 5];
			}
			else if(GetLocation(pll[i].charAt(0),grid)[1] == GetLocation(pll[i].charAt(1),grid)[1]) {
				ci += grid[(GetLocation(pll[i].charAt(0),grid)[0] + 1) % 5][GetLocation(pll[i].charAt(0),grid)[1]];
				ci += grid[(GetLocation(pll[i].charAt(1),grid)[0] + 1) % 5][GetLocation(pll[i].charAt(1),grid)[1]];
			}
			else {
				ci += grid[GetLocation(pll[i].charAt(0),grid)[0]][GetLocation(pll[i].charAt(1),grid)[1]];
				ci += grid[GetLocation(pll[i].charAt(1),grid)[0]][GetLocation(pll[i].charAt(0),grid)[1]];
			}
			
		}
//		for(int i = 0; i < 5; i++) {
//			for(int j = 0; j < 5; j++) {
//				System.out.print(grid[i][j]);
//			}
//			System.out.println();
//		}
//		System.out.println(pl);
//		System.out.println(tpl);
//		System.out.println(ttpl);
//		for(int i = 0; i < pll.length; i++) {
//			System.out.print(pll[i]);
//		}
//		System.out.println();
		System.out.println(ci);
	}
	
	
}
