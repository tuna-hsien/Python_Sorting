# Python 排序演算法測試程式

對話連結：https://chatgpt.com/share/6ab38b7e-ad78-83ee-92ce-497f825f324a

## 一、程式功能

本程式使用 Python 實作三種基本排序演算法：

1. Bubble Sort（氣泡排序）
2. Selection Sort（選擇排序）
3. Insertion Sort（插入排序）

使用者可以：
- 自由選擇排序方法並重複測試
- 選擇升冪或降冪
- 手動輸入任意數量的數值
- 上傳任意名稱的 `.csv` 檔案
- 自動計算 CSV 數值個數
- 顯示排序前與排序後資料
- 顯示比較次數
- Bubble Sort、Selection Sort 顯示交換次數
- Insertion Sort 顯示移動次數

## 二、使用環境

建議使用 **Spyder** 執行。

需要：
```python
import tkinter
import pandas
```

若沒有 pandas，可執行：
```bash
pip install pandas
```

## 三、CSV 格式

例如：
```csv
value
374
3652
78239
45273
```

第一列 `value` 會被視為欄位名稱，不會被當成數值。

程式目前會讀取 CSV 的**第一欄**作為排序資料。

## 四、操作流程

### 1. 選擇資料來源

```text
1. 手動輸入數值
2. 上傳 CSV 檔案
3. 結束程式
```

### 2. 選擇排序方法

```text
1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. 更換資料
5. 結束程式
```

### 3. 選擇排序方向

```text
1. 小 → 大（升冪）
2. 大 → 小（降冪）
3. 返回
```

## 五、次數統計

### 比較次數

代表排序過程中進行大小比較的次數。

### 交換次數

Bubble Sort 與 Selection Sort 使用交換次數。

### 移動次數

Insertion Sort 使用資料移動次數，因為它的主要操作是將資料向後移動。

## 六、三種排序法比較

| 排序法 | 比較次數 | 操作次數 |
|---|---|---|
| Bubble Sort | 比較次數 | 交換次數 |
| Selection Sort | 比較次數 | 交換次數 |
| Insertion Sort | 比較次數 | 移動次數 |

## 七、設計重點

每個排序函式都使用：

```python
arr = data.copy()
```

因此排序不會改變原始資料。同一組資料可以依序測試三種排序方法，確保比較時使用相同的原始資料。

## 八、注意事項

1. CSV 第一列會被視為欄位名稱。
2. 程式目前使用 CSV 的第一欄。
3. CSV 資料必須能轉換成數字。
4. 手動輸入的數值之間請使用空格。
5. 可以重複測試不同排序方法。
6. Insertion Sort 顯示「移動次數」，不是交換次數。
