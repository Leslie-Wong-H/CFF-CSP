#!/user/bin/env python3
# -*- coding: utf-8 -*-


"""
CCF-CSP201312-1 出现次数最多的数

问题描述
　　给定n个正整数，找出它们中出现次数最多的数。如果这样的数有多个，请输出其中最小的一个。
输入格式
　　输入的第一行只有一个正整数n(1 ≤ n ≤ 1000)，表示数字的个数。
　　输入的第二行有n个整数s1, s2, …, sn (1 ≤ si ≤ 10000, 1 ≤ i ≤ n)。相邻的数用空格分隔。
输出格式
　　输出这n个次数中出现次数最多的数。如果这样的数有多个，输出其中最小的一个。
样例输入
6
10 1 10 20 30 20
样例输出
10

"""
# use index to indicate number, while value to stand for times


def main():
	n = int(input())
	num = []
	for i in range(10001):
		num += [0]
	s = input().split()
	for i in range(n):
		s[i] = int(s[i])
		num[s[i]] += 1
	max_num = [0,0]
	for i in range(10001):
		if num[i] > max_num[0]:
			max_num[0], max_num[1] = num[i], i

	print(max_num[1])


main()
