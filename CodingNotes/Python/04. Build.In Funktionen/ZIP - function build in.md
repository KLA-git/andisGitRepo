# ZIP
- Die ZIP Funktion "zipped" Listen zusammen 
- Kriterium für das Zippen ist die Länger der kürzesten List siehe Beispiel:

```python

myList1=[1,2,3,4,5,6]
myList2=['a','b','c']
myList3=[100,200,300]

for item in zip(myList1, myList2, myList3):
	print(item)
	##RESULT:	(1,'a',100)
	##			(2,'b',200)
	##			(3,'c',300)
```

-Zwei Listen zu einer zusammen zippen - Tuple Unpacking
![[Bildschirmfoto 2021-03-21 um 10.20.14.png]]