from hashlib import sha256

def check(video, h0):
	h = []
	with open(video, 'rb') as f:
		while True:
			b = f.read(1024)
			if b:
				h.append(b)
			else:
				numBlocks = len(h)
				break
	i = numBlocks - 1
	while (i>0):
		h[i-1] = h[i-1] + bytes.fromhex(sha256(h[i]).hexdigest())
		i = i - 1
	# print(bytes.fromhex(sha256(h[0]).hexdigest()))
	m = sha256(h[0]).hexdigest()
	if(m == h0):
		print("Authenticated")
	else:
		print("Wrong!!!")

check("birthday.mp4","03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8")