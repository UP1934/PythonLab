sent = input('Enter a sentence:\n')

print("sentence is:\n",sent)

n = sent.find('not') 
p = sent.find('poor') 

if n == -1 and p== -1:
	print('there is no not and poor in the sentence')
else:
	print('not is at {} position'.format(n))
	print('poor is at {} position'.format(p))


if sent[p+5:p+8] == 'bad':
	if n > -1 and p>n:
		sent = sent.replace(sent[n:p+4],'good')
		print('New sentence:\n',sent)
else:
	print('There is no bad after poor')
	
Output:


C:\Users\Admin>cd Desktop

C:\Users\Admin\Desktop>python 2b.py
Enter a sentence:
not poor bad amazing
sentence is:
 not poor bad amazing
not is at 0 position
poor is at 4 position
New sentence:
 good bad amazing

C:\Users\Admin\Desktop>
