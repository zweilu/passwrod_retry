p = input('請輸入密碼')
i = 3
pw = 'a123456'
while i > 1 :
	i = i - 1
	if p != pw:
		print('密碼錯誤!還有' , i ,'次機會')
		
		input('請輸入密碼')
	else:
		print('登入成功')
		break
