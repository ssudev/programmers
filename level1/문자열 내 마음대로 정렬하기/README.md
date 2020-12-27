
# https://programmers.co.kr/learn/courses/30/lessons/12915

예시
strings	            n	return
[sun, bed, car]	    1	[car, bed, sun]
[abce, abcd, cdx]	2	[abcd, abce, cdx]

쉽게 정렬하는 법
sorted(strings, key=lambda string: string[n:n+1])

