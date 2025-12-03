import time

# ==========================================
# 第一部分：定義主角類別 (Player)
# ==========================================
class Player:
    def __init__(self, name, hp, mp, p_atk, m_atk):
        self.name = name        # 角色名稱
        self.max_hp = hp        # 最大血量 (用於限制補血上限，選做)
        self.hp = hp            # 當前血量
        self.mp = mp            # 當前魔力
        self.p_atk = p_atk      # 物理攻擊力
        self.m_atk = m_atk      # 魔法攻擊力
        print(f"✨ 英雄 [{self.name}] 誕生了！ (HP: {self.hp}, MP: {self.mp})")

    # TODO 1: 實作【回復血量】的方法
    # 提示：將傳入的 amount 加到 self.hp 上
    # 進階挑戰：確保加血後不會超過 self.max_hp
    def heal(self, amount):
        print(f"🥤 {self.name} 喝了一瓶藥水...")
        # --- 請在下方編寫你的程式碼 ---
        pass 
        # -----------------------------
        print(f"   目前 HP: {self.hp}")

    # TODO 2: 實作【受到傷害】的方法
    # 提示：從 self.hp 中減去 damage
    def take_damage(self, damage):
        # --- 請在下方編寫你的程式碼 ---
        pass
        # -----------------------------
        print(f"💥 {self.name} 受到 {damage} 點傷害！ (剩餘 HP: {self.hp})")

    # TODO 3: 實作【物理攻擊】的方法
    # 提示：呼叫 target (怪物) 的 take_damage 方法，傳入 self.p_atk
    def physical_attack(self, target):
        print(f"⚔️ {self.name} 對 {target.name} 使用物理攻擊！")
        # --- 請在下方編寫你的程式碼 ---
        pass
        # -----------------------------

    # TODO 4: 實作【魔法攻擊】的方法
    # 提示：
    # 1. 檢查 self.mp 是否足夠 (假設消耗 10 點 MP)
    # 2. 如果足夠，扣除 MP，並呼叫 target.take_damage，傳入 self.m_atk
    # 3. 如果不足，印出 "魔力不足"
    def magic_attack(self, target):
        cost = 10
        print(f"🔥 {self.name} 嘗試詠唱火球術 (消耗 MP: {cost})...")
        # --- 請在下方編寫你的程式碼 ---
        pass
        # -----------------------------

# ==========================================
# 第二部分：定義怪物類別 (Monster)
# ==========================================
class Monster:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk
        print(f"💀 野生的 [{self.name}] 出現了！ (HP: {self.hp})")

    def take_damage(self, damage):
        self.hp -= damage
        print(f"   -> {self.name} 痛得大叫，受傷 {damage} 點！ (剩餘 HP: {self.hp})")

    def attack(self, target):
        print(f"👾 {self.name} 攻擊了 {target.name}！")
        target.take_damage(self.atk)

# ==========================================
# 第三部分：遊戲主程式 (測試區)
# 學生完成上面代碼後，執行這裡應該要能正常運作
# ==========================================

# 1. 創建角色與怪物
hero = Player("勇者", hp=100, mp=50, p_atk=15, m_atk=30)
slime = Monster("哥布林", hp=80, atk=10)

print("-" * 30)

# 2. 測試物理攻擊
hero.physical_attack(slime)

# 3. 測試怪物反擊
slime.attack(hero)

# 4. 測試魔法攻擊
hero.magic_attack(slime)

# 5. 測試補血
hero.heal(20)

# 6. 測試魔力不足的情況
hero.mp = 0
hero.magic_attack(slime)