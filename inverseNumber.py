#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""
CCF-CSP201403-1 相反数

问题描述
　　有 N 个非零且各不相同的整数。请你编一个程序求出它们中有多少对相反数(a 和 -a 为一对相反数)。
输入格式
　　第一行包含一个正整数 N。(1 ≤ N ≤ 500)。
　　第二行为 N 个用单个空格隔开的非零整数,每个数的绝对值不超过1000,保证这些整数各不相同。
输出格式
　　只输出一个整数,即这 N 个数中包含多少对相反数。
样例输入
5
1 2 3 -1 -2
样例输出
2

"""

def main():
	number = int(input())
	sequence = input().split()
	count = 0
	for i in range(number):
		for j in range(i+1, number):
			if int(sequence[i]) == -int(sequence[j]):
				count += 1
				break
	print(count)

main()