import random

def split_train_val(train_all_file, train_file, val_file, val_ratio=0.2):
    with open(train_all_file, 'r') as f:
        lines = f.readlines()
    
    random.shuffle(lines)
    val_count = int(len(lines) * val_ratio)
    
    val_lines = lines[:val_count]
    train_lines = lines[val_count:]
    
    with open(train_file, 'w') as f:
        f.writelines(train_lines)
    
    with open(val_file, 'w') as f:
        f.writelines(val_lines)

# 파일 경로 설정
train_all_file = 'datasets/kaist-rgbt/train-all-04.txt'
train_file = 'datasets/kaist-rgbt/train.txt'
val_file = 'datasets/kaist-rgbt/val.txt'

# train-all-04.txt 파일을 train과 val로 나누기
split_train_val(train_all_file, train_file, val_file)
