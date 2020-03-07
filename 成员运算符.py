username=input('请输入你的用户名:')
assert len(username)==3,"用户名长度不符"
numbers='1234567890'
alphas='qwertyuiopasdfghjklzxcvbnm'
symbols='!@#$%^&*_-<>,.?/\;:'
validity=username[0] in numbers and username[1] in numbers+alphas and username[2] in numbers+alphas+symbols
print(validity)
