#11420340 莊佳臻
#11420345 魏宇嫻

import tkinter as tk
from tkinter import filedialog
import pandas as pd


# ============================================================
# Bubble Sort
# ============================================================
def bubble_sort(data, ascending=True):

    arr = data.copy()

    compare_count = 0
    swap_count = 0

    n = len(arr)

    for i in range(n - 1):

        for j in range(n - 1 - i):

            # 比較次數 +1
            compare_count += 1

            if ascending:

                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swap_count += 1

            else:

                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swap_count += 1

    return arr, compare_count, swap_count


# ============================================================
# Selection Sort
# ============================================================
def selection_sort(data, ascending=True):

    arr = data.copy()

    compare_count = 0
    swap_count = 0

    n = len(arr)

    for i in range(n - 1):

        target = i

        for j in range(i + 1, n):

            # 比較次數 +1
            compare_count += 1

            if ascending:

                if arr[j] < arr[target]:
                    target = j

            else:

                if arr[j] > arr[target]:
                    target = j

        # 找到新的位置才交換
        if target != i:

            arr[i], arr[target] = arr[target], arr[i]

            swap_count += 1

    return arr, compare_count, swap_count


# ============================================================
# Insertion Sort
# ============================================================
def insertion_sort(data, ascending=True):

    arr = data.copy()

    compare_count = 0
    move_count = 0

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0:

            # 比較次數 +1
            compare_count += 1

            if ascending:

                if arr[j] > key:

                    arr[j + 1] = arr[j]

                    move_count += 1

                    j -= 1

                else:

                    break

            else:

                if arr[j] < key:

                    arr[j + 1] = arr[j]

                    move_count += 1

                    j -= 1

                else:

                    break

        arr[j + 1] = key

    return arr, compare_count, move_count


# ============================================================
# 手動輸入數值
# ============================================================
def input_numbers():

    while True:

        try:

            print("\n請輸入數值")
            print("數值之間請使用空格分隔")

            text = input("例如：8 3 7 1 9 2 5\n")

            numbers = list(map(float, text.split()))

            if len(numbers) == 0:

                print("請至少輸入一個數值！")

                continue

            return numbers

        except ValueError:

            print("輸入格式錯誤！")
            print("請確認全部都是數字。")


# ============================================================
# 上傳 CSV
# ============================================================
def upload_csv():

    root = tk.Tk()

    root.withdraw()

    file_path = filedialog.askopenfilename(

        title="請選擇 CSV 檔案",

        filetypes=[
            ("CSV files", "*.csv")
        ]

    )

    root.destroy()

    if not file_path:

        print("\n沒有選擇檔案。")

        return None

    try:

        # 讀取 CSV
        # 第一列會被視為欄位名稱
        df = pd.read_csv(file_path)

        # 取得第一欄
        values = df.iloc[:, 0].dropna()

        # 將資料轉成數字
        numbers = pd.to_numeric(values).tolist()

        print("\n======================================")
        print("CSV 檔案讀取成功！")
        print("======================================")

        print("檔案位置：")
        print(file_path)

        print("\n數值個數：", len(numbers))

        print("\n讀取到的數值：")

        print(numbers)

        return numbers

    except Exception as e:

        print("\n======================================")
        print("讀取 CSV 時發生錯誤")
        print("======================================")

        print(e)

        return None


# ============================================================
# 選擇排序方向
# ============================================================
def choose_order(data, sort_function):

    while True:

        print("\n======================================")
        print("請選擇排序方向")
        print("======================================")

        print("1. 小 → 大（升冪）")
        print("2. 大 → 小（降冪）")
        print("3. 返回")

        print("======================================")

        choice = input("請輸入選項：")

        # ----------------------------------
        # 升冪
        # ----------------------------------
        if choice == "1":

            result, compare_count, operation_count = \
                sort_function(data, ascending=True)

            return result, compare_count, operation_count, "小 → 大（升冪）"

        # ----------------------------------
        # 降冪
        # ----------------------------------
        elif choice == "2":

            result, compare_count, operation_count = \
                sort_function(data, ascending=False)

            return result, compare_count, operation_count, "大 → 小（降冪）"

        # ----------------------------------
        # 返回
        # ----------------------------------
        elif choice == "3":

            return None

        else:

            print("無效的選項，請重新輸入！")


# ============================================================
# 顯示排序結果
# ============================================================
def print_result(
        original,
        result,
        method,
        direction,
        compare_count,
        operation_count):

    print("\n")
    print("======================================")
    print("              排序結果")
    print("======================================")

    print("資料個數：", len(original))

    print("排序方法：", method)

    print("排序方向：", direction)

    print("\n--------------------------------------")

    print("\n排序後：")

    print(result)

    print("\n--------------------------------------")

    print("比較次數：", compare_count)

    # Insertion Sort 使用「移動次數」
    if method == "Insertion Sort":

        print("移動次數：", operation_count)

    else:

        print("交換次數：", operation_count)

    print("======================================")


# ============================================================
# 選擇排序方法
# ============================================================
def choose_sort_method(data):

    while True:

        print("\n")
        print("======================================")
        print("           請選擇排序方法")
        print("======================================")

        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. 更換資料")
        print("5. 結束程式")

        print("======================================")

        choice = input("請輸入選項：")

        # ----------------------------------
        # Bubble Sort
        # ----------------------------------
        if choice == "1":

            method = "Bubble Sort"

            result = choose_order(
                data,
                bubble_sort
            )

            if result is not None:

                sorted_data, compare_count, \
                    operation_count, direction = result

                print_result(
                    data,
                    sorted_data,
                    method,
                    direction,
                    compare_count,
                    operation_count
                )

        # ----------------------------------
        # Selection Sort
        # ----------------------------------
        elif choice == "2":

            method = "Selection Sort"

            result = choose_order(
                data,
                selection_sort
            )

            if result is not None:

                sorted_data, compare_count, \
                    operation_count, direction = result

                print_result(
                    data,
                    sorted_data,
                    method,
                    direction,
                    compare_count,
                    operation_count
                )

        # ----------------------------------
        # Insertion Sort
        # ----------------------------------
        elif choice == "3":

            method = "Insertion Sort"

            result = choose_order(
                data,
                insertion_sort
            )

            if result is not None:

                sorted_data, compare_count, \
                    operation_count, direction = result

                print_result(
                    data,
                    sorted_data,
                    method,
                    direction,
                    compare_count,
                    operation_count
                )

        # ----------------------------------
        # 更換資料
        # ----------------------------------
        elif choice == "4":

            return "change"

        # ----------------------------------
        # 結束程式
        # ----------------------------------
        elif choice == "5":

            return "exit"

        else:

            print("無效的選項，請重新輸入！")


# ============================================================
# 主程式
# ============================================================
def main():

    print("\n")
    print("======================================")
    print("          排序演算法測試程式")
    print("======================================")

    while True:

        print("\n")
        print("請選擇資料來源：")

        print("1. 手動輸入數值")
        print("2. 上傳 CSV 檔案")
        print("3. 結束程式")

        print("======================================")

        choice = input("請輸入選項：")

        # ==================================
        # 手動輸入
        # ==================================
        if choice == "1":

            data = input_numbers()

            print("\n資料輸入完成！")

            print("數值個數：", len(data))

            print("資料：")

            print(data)

            result = choose_sort_method(data)

            if result == "exit":

                break

        # ==================================
        # CSV
        # ==================================
        elif choice == "2":

            data = upload_csv()

            if data is not None and len(data) > 0:

                result = choose_sort_method(data)

                if result == "exit":

                    break

        # ==================================
        # 結束
        # ==================================
        elif choice == "3":

            break

        else:

            print("無效的選項，請重新輸入！")

    print("\n======================================")
    print("程式結束，謝謝查怡美女老師和帥哥助教！")
    print("======================================")


# ============================================================
# 執行主程式
# ============================================================
if __name__ == "__main__":

    main()