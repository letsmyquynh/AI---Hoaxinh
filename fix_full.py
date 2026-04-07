import csv

input_file = "data.csv"
output_file = "data_clean.csv"

rows = []

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        # bỏ dòng rỗng
        if not line:
            continue

        # bỏ header lặp
        if line.lower() == "comment,label":
            continue

        # tách label từ cuối
        parts = line.rsplit(",", 1)

        if len(parts) != 2:
            continue  # bỏ dòng lỗi

        comment, label = parts

        # clean label
        label = label.strip().lower()

        if label not in ["positive", "negative", "neutral"]:
            continue

        rows.append([comment.strip(), label])

# ghi lại file chuẩn
with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["comment", "label"])
    writer.writerows(rows)

print("✅ DONE: data_clean.csv sạch 100%")