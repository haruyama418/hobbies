input_price=input("税抜価格を入力してください")
price=int(input_price)
#print(price)ここまでの動作確認
former_price=int(price*1.08)
later_price=int(price*1.1)
# print(former_price)
# print(later_price)

print("増税前の価格は"+str(former_price)+"円")
print("増税後の価格は"+str(later_price)+"円")

gap=(later_price-former_price)
# print(gap)
print("その差額は"+str(gap)+"円となります")
