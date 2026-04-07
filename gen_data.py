import random
import csv

subjects = ["hoa", "bó hoa", "shop", "dịch vụ", "giao hàng"]

adj_positive = ["xịn", "đẹp", "ưng", "okela", "ổn áp", "đỉnh", "tốt"]
adj_negative = ["dở", "lỗi", "chán", "xấu", "fail", "tệ", "chậm"]
adj_neutral = ["bình thường", "tạm ổn", "cũng được"]

adverbs = ["lắm", "thiệt", "vãi", "ghê", "luôn", "quá" , "vkl" "gớm"]

emoji_pos = [" 😍", " 🔥", " 💖", " ✨", " 🫶", ""]
emoji_neg = [" 😡", " 💀", " 🤡", " 👎", " 🙃", ""]
emoji_neu = ["", " 🙂"]

# ===== TEMPLATE ĐA DẠNG =====
def generate_sentence(label):
    subject = random.choice(subjects)
    adverb = random.choice(adverbs)

    if label == "positive":
        adj = random.choice(adj_positive)
        emoji = random.choice(emoji_pos)

        templates = [
            f"{subject} {adj} {adverb}{emoji}",
            f"{adj} {adverb} luôn á, {subject} quá ok{emoji}",
            f"mê {subject} {adj} {adverb}{emoji}",
            f"{subject} {adj} ghê, sẽ ủng hộ tiếp{emoji}"
        ]

    elif label == "negative":
        adj = random.choice(adj_negative)
        emoji = random.choice(emoji_neg)

        templates = [
            f"{subject} {adj} {adverb}{emoji}",
            f"{adj} {adverb}, {subject} chán thật sự{emoji}",
            f"{subject} bị {adj}, thất vọng ghê{emoji}",
            f"không đáng tiền, {subject} {adj} quá{emoji}"
        ]

    else:
        adj = random.choice(adj_neutral)
        emoji = random.choice(emoji_neu)

        templates = [
            f"{subject} {adj}",
            f"{adj}, không có gì đặc biệt",
            f"{subject} {adj} thôi",
            f"thấy {subject} nên mua thử"
        ]

    return random.choice(templates)


# ===== GHI FILE =====
with open("data_xin.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["comment", "label"])

    for _ in range(500):
        label = random.choice(["positive", "negative", "neutral"])
        comment = generate_sentence(label)

        writer.writerow([comment, label])

print("Dataset xịn hơn rồi!")