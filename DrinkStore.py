

#===========================
#主程式區
#===========================

print("=== 製作飲料中 ===")
# 1. 這裡呼叫了 Drink 類別，傳入了三個資料（點飲料）
# 暗示：你的 __init__ 需要接收哪三個參數？
order1 = Drink("珍珠奶茶", "半糖", "少冰") 
print(f"成功建立訂單：{order1.name} ({order1.sugar}/{order1.ice})")

print("\n=== 加料階段 ===")
# 2. 這裡呼叫了 add_topping 方法
# 暗示：這個方法需要接收配料名稱和價格，並更新總金額
order1.add_topping("珍珠", 10)
order1.add_topping("椰果", 5)

print("\n=== 最終結帳單 ===")
# 3. 這裡呼叫了 print_label 方法
# 暗示：這個方法負責把所有資訊印得漂漂亮亮
order1.print_label()