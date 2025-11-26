from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 實作部分
        records = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in records:
                return [records[diff], idx]
            records[val] = idx
        return []
    
# --- 測試執行區 ---
if __name__ == "__main__":
    # 1. 實例化類別
    sol = Solution()
    
    # 2. 準備測試資料
    test_cases = [
        {"nums": [2, 7, 11, 15], "target": 9, "expect": [0, 1]},
        {"nums": [3, 2, 4], "target": 6, "expect": [1, 2]},
        {"nums": [3, 3], "target": 6, "expect": [0, 1]},
    ]

    print(f"{'期望結果':<10} | {'實際結果':<10} | {'狀態':<5}")
    print("-" * 35)

    for case in test_cases:
        # 使用實例 sol 來呼叫方法
        result = sol.twoSum(case["nums"], case["target"])
        
        # 排序後比較
        is_pass = sorted(result) == sorted(case["expect"])
        status = "✅ 通過" if is_pass else "❌ 失敗"
        
        print(f"{str(case['expect']):<10} | {str(result):<10} | {status}")