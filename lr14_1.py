import matplotlib.pyplot as plt
from collections import Counter
import tkinter.filedialog as fd

filename = fd.askopenfilename(title="Виберіть текстовий файл",
                              filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
if filename:
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower()

    letters = [ch for ch in text if ch.isalpha()]

    freq = Counter(letters)

    letters_sorted = [ch for ch, _ in freq.most_common()]
    counts = [freq[ch] for ch in letters_sorted]

    plt.figure(figsize=(10, 6))
    plt.bar(letters_sorted, counts, color="skyblue", edgecolor="black")
    plt.xlabel("Літери")
    plt.ylabel("Частота")
    plt.title("Гістограма частоти появи літер у тексті")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.savefig("letters_histogram.png", dpi=300)
    plt.show()
else:
    print("Файл не обрано")
