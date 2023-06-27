import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        #perulangan di tiap iterasi
        for j in range(n - i - 1):
            #membandingkan elemen berikutnya dan elemen sekarang
            if arr[j] > arr[j + 1]:
                #menukarkan elemen jika elemen lebih besar
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def print_iteration(iteration, arr):
    print(f"Iter"
          f""
          f""
          f"ation {iteration}: {arr}")

# nomor inputan
numbers = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
           26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
           17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]

# pilihan di tentukan oleh pengguna
choice = input("Pilih algoritma Sorting (bubble/insertion): ")

if choice.lower() == "bubble":
    print("sebelum proses BubbleSort: ", numbers)
    start_time = time.time()
    bubble_sort(numbers)
    end_time = time.time()
    print("setelah proses BubbleSort: ", numbers)

elif choice.lower() == "insertion":
    print("sebelum proses Insertion Sort: ", numbers)
    start_time = time.time()
    insertion_sort(numbers)
    end_time = time.time()
    print("setelah proses Insertion Sort: ", numbers)

else:
    print("pilihan anda tidak valid. pilih antara 'bubble' atau 'insertion'.")

# Print 5 iterasi pertama
print("\n5 iterasi pertama:")
for i in range(min(5, len(numbers))):
    print_iteration(i + 1, numbers)

# Print 5 iterasi terakhir
print("\n5 iterai terakhir:")
for i in range(max(len(numbers) - 5, 0), len(numbers)):
    print_iteration(i + 1, numbers)

# Print waktu komputasi
computation_time = end_time - start_time
print("\nwaktu komputasi:", computation_time, "seconds")

