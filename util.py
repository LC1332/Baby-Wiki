
def parsing_word_list( words_file ):
    print("parsing word list")
    word2data = {}
    import json
    with open(words_file, "r", encoding = "utf-8") as f:
        # load each line in json format
        for line in f:
            try:
                data = json.loads(line)
                if "description" not in data or data["description"] == "":
                    continue
                input_word = data["input_word"]
                data["edge_node"] = []
                word2data[input_word] = data
            except:
                pass

    print(len(word2data), ' words loaded')

    # create all edge nodes

    for word in word2data:
        data = word2data[word]
        related_words = data["related_words"]

        for w in related_words:
            if w not in word2data:
                continue

            if w not in data["edge_node"]:
                data["edge_node"].append(w)

            if word not in word2data[w]["edge_node"]:
                word2data[w]["edge_node"].append(word)

    # print(word2data["苹果"]["edge_node"])


import os
import cv2
import numpy as np
import random

def render_image( word ):
    temp_folder = "./temp"
    if not os.path.exists(temp_folder):
        os.mkdir(temp_folder)
    temp_save_name = os.path.join(temp_folder, word + ".jpg")
    if os.path.exists(temp_save_name):
        return temp_save_name
    
    image_folder = "./data/image"
    # 尝试读取 image_folder + word + "_" + part_id + ".jpg" 对应的图片
    # 并存储到 list , imgs 中
    # 如果len(imgs) == 1, 则result_img = imgs[0]
    # 如果len(imgs) > 1， 则把至多6张图片，resize到300*300，用2*3的阵列，拼成一张600*900的图片，不到6张则补足黑色
    # 如果len(imgs) == 0，生成一张600*900的黑色图片，在中间用白色字体写上 word
    # 请补全这段代码，并在最后返回temp_save_name
    imgs = []
    for i in range(10):
        img_path = os.path.join(image_folder, word + "_" + str(i) + ".jpg")
        if os.path.exists(img_path):
            img = cv2.imread(img_path)
            imgs.append(img)

    if len(imgs) == 1:
        result_img = imgs[0]
    elif len(imgs) > 1:
        result_img = np.zeros((600, 900, 3), np.uint8)
        cell_w, cell_h = 300, 300
        rows, cols = 2, 3
        random.shuffle(imgs)
        for i in range(min(len(imgs), rows*cols)):
            img = cv2.resize(imgs[i], (cell_w, cell_h)) 
            row = i // cols 
            col = i % cols
            x = col * cell_w
            y = row * cell_h
            result_img[y:y+cell_h, x:x+cell_w] = img
    else:
        result_img = np.zeros((600, 900, 3), np.uint8)
        cv2.putText(result_img, word, (300,450), cv2.FONT_HERSHEY_SIMPLEX, 
                   2, (255,255,255), 2)
    
    cv2.imwrite(temp_save_name, result_img)
    return temp_save_name